#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import socket
import errno
from time import time as now
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


DEFAULT_TIMEOUT = 120
DEFAULT_SERVER_HOST = 'localhost'
DEFAULT_SERVER_PORT = 80


class NetServiceChecker(object):

    def __init__(self, host, port, timeout=DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def end_wait(self):
        self.sock.close()


    def check(self):
        if self.timeout:
            end_timeout = now() + self.timeout
        while True:
            try:
                if self.timeout:
                    next_timeout = end_timeout - now()
                    if next_timeout < 0:
                        return False
                    else:
                        print('Setting socket next timeout {}'.format(round(next_timeout)))
                        self.sock.settimeout(next_timeout)
                self.sock.connect((self.host, self.port))
            except socket.timeout:
                if self.timeout:
                    return False
            except socket.error as e:
                print('Except: {}'.format(e))
            else:
                self.end_wait()
                return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wait for network service')
    parser.add_argument('--host', action='store', dest='host', default=DEFAULT_SERVER_HOST)
    parser.add_argument('--port', action='store', dest='port', type=int, default=DEFAULT_SERVER_PORT)
    parser.add_argument('--timeout', action='store', dest='timeout', type=int, default=DEFAULT_TIMEOUT)
    args = parser.parse_args()
    service_checker = NetServiceChecker(args.host, args.port, timeout=args.timeout)
    print('check network service for {}:{}...'.format(args.host, args.port))
    if service_checker.check():
        print('service is available again!')

