#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import socket
import threading
import socketserver


SERVER_HOST = 'localhost'
SERVER_PORT = 0 # dynamic port
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'


def client (ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'utf-8'))
        resp = sock.recv(BUF_SIZE)
        print('Client received: %s' % resp.decode())
    finally:
        sock.close()


class ThreadTCPRequestHandler (socketserver.BaseRequestHandler):
    def handle (self):
        data = self.request.recv(BUF_SIZE)
        curr_thread = threading.current_thread()
        resp = '%s: %s' % (curr_thread.name, data.decode())
        self.request.sendall(bytes(resp, 'utf-8'))


class ThreadedTCPServer (socketserver.ThreadingMixIn, socketserver.TCPServer):
    # inherited everything form parents
    pass


def main ():
    # launch server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print('Server loop running on thread: %s' % server_thread.name)

    # launch client
    client(ip, port, 'Hello from client 1')
    client(ip, port, 'Hello from client 2')
    client(ip, port, 'Hello from client 3')

    # shutdown
    server.shutdown()


if __name__ == '__main__':
    main()
