#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import socket
import argparse

def main ():
    # parameter
    parser = argparse.ArgumentParser(description='Socket Error Example')
    parser.add_argument('--host', action='store', dest='host', required=True)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Error creating socket: %s' % e)
        sys.exit(1)
    
    # connect to host
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print('Address-related error connecting to server: %s' % s)
        sys.exit(1)
    except socket.error as e:
        print('Connecting error: %s' % e)
        sys.exit(1)
    
    # send data
    try:
        s.sendall(bytes('GET %s HTTP/1.0\r\n\r\n' % filename, 'utf-8'))
    except socket.error as e:
        print('Error Sending error: %s' % e)
        sys.exit(1)

    while True:
        # waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print('Error receiving data: %s' % e)
            sys.exit(1)
        if not buf:
            break
        
        # write received data
        sys.stdout.write(buf.decode())

if __name__ == '__main__':
    main()
