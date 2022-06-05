#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import sys
import time
# from scapy.all import *

NTP_SERVER = '0.uk.pool.ntp.org'
TIME1970 = 2208988800

def sntp_client ():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    '''
    rfc 1361 & rfc 2030
                        1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |LI | VN  |Mode |    Stratum    |     Poll      |   Precision   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    Leap Indicator (LI): This is a two-bit code warning of an impending
    leap second to be inserted/deleted in the last minute of the current
    day, with bit 0 and bit 1, respectively, coded as follows:
       LI       Value     Meaning
       -------------------------------------------------------
       00       0         no warning
       01       1         last minute has 61 seconds
       10       2         last minute has 59 seconds)
       11       3         alarm condition (clock not synchronized)

    Version Number (VN): This is a three-bit integer indicating the NTP
    version number, currently 3.

    Mode: This is a three-bit integer indicating the mode, with values
    defined as follows:
       Mode     Meaning
       ------------------------------------
       0        reserved
       1        symmetric active
       2        symmetric passive
       3        client
       4        server
       5        broadcast
       6        reserved for NTP control message
       7        reserved for private use

    Stratum: This is a eight-bit unsigned integer indicating the stratum
    level of the local clock, with values defined as follows:
       Stratum  Meaning
       ----------------------------------------------
       0        unspecified or unavailable
       1        primary reference (e.g., radio clock)
       2-15     secondary reference (via NTP or SNTP)
       16-255   reserved
    '''
    data = '\x1b' + 47 * '\0'
    from scapy.all import NTP
    print(NTP(bytes(data, 'utf-8')).show())
    '''
    ###[ NTPHeader ]###
    leap      = no warning
    version   = 3
    mode      = client
    stratum   = 0
    poll      = 0
    precision = 0
    delay     = 0
    dispersion= 0
    ref_id    = ''
    ref       = 0
    orig      = 0
    recv      = 0
    sent      = 0
    '''
    client.sendto(bytes(data, 'utf-8'), (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)
    if data:
        print('Response received from:', address)
    print(struct.unpack('!12I', data))
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__ == '__main__':
    sntp_client()
