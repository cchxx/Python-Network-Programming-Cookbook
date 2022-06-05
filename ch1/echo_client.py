#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import argparse

host = 'localhost'

def echo_client (port):
    '''
    a simple echo client
    '''

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    server_address = (host, port)
    print('Connecting to %s port %s' % server_address)
    s.connect(server_address)

    try:
        # send data
        message = 'Test message. This will be echoed'
        print('Sending %s' % message)
        s.sendall(bytes(message, 'utf-8'))
        # look for response
        amount_received = 0
        while amount_received < len(message):
            data = s.recv(16)
            amount_received += len(data)
            print('Received: %s' % data)
    except socket.error as e:
        print('Socket error: %s' % e)
    except Exception as e:
        print('Other exception: %s' % e)
    finally:
        print('Closing connection to the server')
        s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    args = parser.parse_args()
    echo_client(args.port)
