#!/usr/bin/env python
# -*- coding: utf-8 -*-

import diesel
import argparse
# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

'''
diesel is old framework 8 years ago
will try to recreate a example using other latest popular framework
'''


class EchoServer(object):
    '''
    A echo server using diesel
    '''

    def handler(self, remote_addr):
        '''
        run the echo server
        '''
        host, port = remote_addr[0], remote_addr[1]
        print('Echo client connected from: {}:{}'.format(host, port))

        while True:
            try:
                message = diesel.until_eol()
                your_msg = ': '.join(['You said', message])
                diesel.send(your_msg)
            except Exception as e:
                print('Exception: {}'.format(e))


def main(server_port):
    app = diesel.Application()
    server = EchoServer()
    app.add_service(diesel.Service(server.handler, server_port))
    app.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo server with Diesel')
    parser.add_argument(
        '--port',
        action='store',
        dest='port',
        type=int,
        required=True)
    args = parser.parse_args()
    main(args.port)
