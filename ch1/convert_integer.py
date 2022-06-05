#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket

def convert_integer ():
    data = 1234
    # 32-bit
    print('Original: %s => Long host byte order: %s, Network byte order: %s'\
        %(hex(data), hex(socket.ntohl(data)), hex(socket.htonl(data))))
    # 16-bit
    print('Original: %s => Short host byte order: %s, Network byte order: %s'\
        %(hex(data), hex(socket.ntohs(data)), hex(socket.htons(data))))

if __name__ == '__main__':
    convert_integer()
