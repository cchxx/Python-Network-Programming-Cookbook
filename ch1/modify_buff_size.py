#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('Buffer size [Before]: %d' % bufsize)

    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)

    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('Buffer size [After]: %d' % bufsize)

if __name__ == '__main__':
    modify_buff_size()
