#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import socket
import struct
import select
import time
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


'''
RFC 792

Echo or Echo Reply Message
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type      |     Code      |          Checksum             |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Identifier          |        Sequence Number        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Data ...
   +-+-+-+-+-

   Type
      8 for echo message;
      0 for echo reply message.

   Code
      0

   Checksum
      The checksum is the 16-bit ones's complement of the one's
      complement sum of the ICMP message starting with the ICMP Type.
      For computing the checksum , the checksum field should be zero.
      If the total length is odd, the received data is padded with one
      octet of zeros for computing the checksum.  This checksum may be
      replaced in the future.

   Identifier
      If code = 0, an identifier to aid in matching echos and replies,
      may be zero.

   Sequence Number
      If code = 0, a sequence number to aid in matching echos and
      replies, may be zero.
'''

ICMP_ECHO_REQUEST = 8       # Echo Request (Code 8) & Echo reply (code 0)
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 4


class Pinger(object):
    '''pings to a host'''

    def __init__(self, target_host: str, count: int = DEFAULT_COUNT,
                 timeout: int = DEFAULT_TIMEOUT) -> None:
        self.target_host = target_host
        self.count = count
        self.timeout = timeout

    def do_checksum(self, data: bytes) -> int:
        '''verify pkt integritity'''
        summ = 0
        max_count = ((len(data) >> 1) << 1)
        count = 0
        while count < max_count:
            summ += (data[count] + (data[count + 1] << 8))
            # summ += (ord(data[count]) + (ord(data[count + 1]) << 8))
            summ &= 0xffffffff
            count += 2
        if max_count < len(data):
            summ += data[-1]
            # summ += ord(data[-1])

        summ = (summ >> 16) + (summ & 0xffff)
        summ += (summ >> 16)
        answer = ~summ
        answer &= 0xffff
        answer = (answer >> 8) + ((answer << 8) & 0xff00)
        return answer

    def receive_pong(self, sock, pkt_id, timeout: int):
        '''receive ping from the socket'''
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_received = time.time()
            time_spent = time_received - start_time
            if readable[0] == []:       # timeout
                return

            pkt, addr = sock.recvfrom(1024)
            icmp_hdr = pkt[20:28]
            type, code, checksum, id, seq = struct.unpack('bbHHh', icmp_hdr)
            if id == pkt_id:
                bytes_in_double = struct.calcsize('d')
                time_spent = struct.unpack(
                    'd', pkt[28:28 + bytes_in_double])[0]
                return time_received - time_spent

            time_remaining -= time_spent
            if time_remaining <= 0:
                return

    def send_ping(self, sock, identifier):
        '''send ping to target host'''
        target_addr = socket.gethostbyaddr(self.target_host)
        logging.debug('target {}, {}'.format(target_addr, type(target_addr)))

        # create dummy hdr with 0 chsum
        hdr = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, 0, identifier, 1)
        timestamp = struct.calcsize('d')
        payload = (192 - timestamp) * b'Q'
        payload = struct.pack('d', time.time()) + payload
        # get chsum on payload and dummy hdr
        my_cksum = self.do_checksum(hdr + payload)
        hdr = struct.pack( 'bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_cksum), identifier, 1)
        pkt = hdr + payload
        sock.sendto(pkt, (target_addr[2][0], 1))

    def ping_once(self):
        '''return delay in seconds or None on timeout'''
        icmp = socket.getprotobyname('icmp')
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error as xxx_todo_changeme:
            (errno, errmsg) = xxx_todo_changeme.args
            if errno == 1:
                # operation not permitted
                errmsg += 'ICMP message can only be sent from root user process'
                raise socket.error(errmsg)
        my_id = os.getpid() & 0xffff
        self.send_ping(sock, my_id)
        delay = self.receive_pong(sock, my_id, self.timeout)
        sock.close()
        return delay

    def ping(self):
        '''run ping process'''
        for i in range(self.count):
            print('Ping to {} ...'.format(self.target_host))
            try:
                delay = self.ping_once()
            except socket.gaierror as e:
                print('Ping failed. (socket error: "{}")'.format(e[1]))
                break
            if delay is None:
                print('Ping failed. (timeout within {}.'.format(self.timeout))
            else:
                delay = delay * 1000
                print('Get pong in {}ms'.format(delay))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python ping')
    parser.add_argument(
        '--target-host',
        action='store',
        dest='target_host',
        required=True)
    args = parser.parse_args()
    pinger = Pinger(args.target_host)
    pinger.ping()
