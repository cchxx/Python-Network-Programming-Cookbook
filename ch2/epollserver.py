#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import select
import argparse
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

'''
!!! Only support epoll on Linux platform !!!
'''

SERVER_HOST = 'localhost'

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'

SERVER_RESPONSE = b'''HTTP/1.1 200 OK\r\nData: Mon, 1 Apr 2013 01:01:01 GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\nHello from Epoll Server!'''


class EpollServer(object):
    '''A socket server using Epoll'''

    def __init__(self, host: str = SERVER_HOST, port: int = 0):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen()
        self.sock.setblocking(0)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        print('Started Epoll Server')
        self.epoll = select.epoll()
        self.epoll.register(self.sock.fileno(), select.EPOLLIN)
        logging.debug('Register sock fileno {}'.format(self.sock.fileno()))

    def run(self):
        '''execute epoll server operation'''
        try:
            connections, requests, responses = {}, {}, {}
            while True:
                events = self.epoll.poll(1)
                for fileno, event in events:
                    '''
                    EPOLLIN        1
                    EPOLLPRI       2
                    EPOLLOUT       4
                    EPOLLERR       8
                    EPOLLHUP       16
                    EPOLLRDNORM    64
                    EPOLLRDBAND    128
                    EPOLLWRNORM    256
                    EPOLLWRBAND    512
                    EPOLLMSG       1024
                    EPOLLRDHUP     8192
                    EPOLL_CLOEXEC  524288
                    EPOLLEXCLUSIVE 268435456
                    EPOLLONESHOT   1073741824
                    EPOLLET        2147483648
                    '''
                    logging.debug('Received fileno {}, event {}'.format(fileno, event))
                    if fileno == self.sock.fileno():
                        # step 1
                        conn, addr = self.sock.accept()
                        conn.setblocking(0)
                        self.epoll.register(conn.fileno(), select.EPOLLIN)
                        logging.debug('register connection fileno {}'.format(conn.fileno()))
                        connections[conn.fileno()] = conn
                        requests[conn.fileno()] = b''
                        responses[conn.fileno()] = SERVER_RESPONSE
                    elif event & select.EPOLLIN:
                        # step 2
                        requests[fileno] += connections[fileno].recv(1024)
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            self.epoll.modify(fileno, select.EPOLLOUT)
                            print( '-' * 40 + '\n' + requests[fileno].decode()[:-2])
                    elif event & select.EPOLLOUT:
                        # step 3
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                        if len(responses[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        # step 4
                        self.epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            self.epoll.unregister(self.sock.fileno)
            self.epoll.close()
            self.sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Socket Server Example with Epoll')
    parser.add_argument(
        '--port',
        action='store',
        dest='port',
        type=int,
        required=True)
    args = parser.parse_args()
    server = EpollServer(host=SERVER_HOST, port=args.port)
    server.run()
