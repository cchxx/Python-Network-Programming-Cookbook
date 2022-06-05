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


class ForkingClient ():
    def __init__ (self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run (self):
        curr_pid = os.getpid()
        print('PID %s Sending echo message to the server: %s' % (curr_pid, ECHO_MSG))
        length = self.sock.send(bytes(ECHO_MSG, 'utf-8'))
        print('Sent: %d char, so far ...' % length)
        resp = self.sock.recv(BUF_SIZE)
        # print('PID %d received: %s' % (curr_pid, resp[5:]))
        print('PID %d received: %s' % (curr_pid, resp))

    def shutdown (self):
        self.sock.close()


class ForkingServerRequestHandler (socketserver.BaseRequestHandler):
    def handle (self):
        data = self.request.recv(BUF_SIZE)
        curr_pid = os.getpid()
        resp = '%s: %s' % (curr_pid, data)
        print('Server sending response [curr pid: data] = [%s]' % resp)
        self.request.send(bytes(resp, 'utf-8'))
        return


class ForkingServer (socketserver.ForkingMixIn, socketserver.TCPServer):
    # inherited everything form parents
    pass


def main ():
    # launch server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    # launch client
    client1 = ForkingClient(ip, port)
    client1.run()

    client2 = ForkingClient(ip, port)
    client2.run()

    # shutdown
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()


if __name__ == '__main__':
    main()
