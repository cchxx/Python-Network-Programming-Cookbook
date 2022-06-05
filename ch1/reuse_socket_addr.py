#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import connection
import socket
import sys

def reuse_socket_addr ():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # old state of SO_REUSEADDR
    old_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print('Old sock state: %s' % old_state)

    # enable SO_REUSEADDR
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print('New sock state: %s' % new_state)

    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print('Listening on port: %s' % local_port)
    while True:
        try:
            connection, addr = srv.accept()
            print('Connected by %s: %s' % (addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as e:
            print('%s' % e)

if __name__ == '__main__':
    reuse_socket_addr()
