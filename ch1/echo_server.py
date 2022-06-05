#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import server
import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server (port):
    '''
    a simple echo server
    '''

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # enable resue address/port
    # chx: per my understanding, before timeout of resouce, still can use it
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind
    server_address = (host, port)
    print('Starting up echo server on %s port %s' % server_address)
    s.bind(server_address)

    # listen to clients, backlog argument specifies the max no. of queued connections
    s.listen(backlog)

    while True:
        print('Waiting to receive message from client')
        client, address = s.accept()
        data = client.recv(data_payload)
        if data:
            print('Data: %s', data)
            client.send(data)
            print('Send %s bytes back to %s' % (data, address))
        # end connection
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    args = parser.parse_args()
    echo_server(args.port)
