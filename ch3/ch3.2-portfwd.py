#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import asyncore
import socket


LOCAL_SERVER_HOST = 'localhost'
REMOTE_SERVER_HOST = 'www.sohu.com'
BUFSIZE = 4096


class PortForwarder(asyncore.dispatcher):
    def __init__(self, ip: str, port: int, remoteip: str,
                 remoteport: str, backlog: int = 5) -> None:
        asyncore.dispatcher.__init__(self)
        self.remoteip = remoteip
        self.remoteport = remoteport
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip, port))
        self.listen(backlog)

    def handle_accept(self) -> None:
        conn, addr = self.accept()
        print('Connected to {}'.format(addr))
        Sender(Receiver(conn), self.remoteip, self.remoteport)


class Receiver(asyncore.dispatcher):
    def __init__(self, conn) -> None:
        asyncore.dispatcher.__init__(self, conn)
        self.fromRemoteBuffer = ''
        self.toRemoteBuffer = ''
        self.sender = None

    def handle_connect(self) -> None:
        pass

    def handle_read(self) -> None:
        read = self.recv(BUFSIZE)
        self.fromRemoteBuffer += read

    def writable(self) -> bool:
        return len(self.toRemoteBuffer) > 0

    def handle_write(self) -> None:
        sent = self.send(self.toRemoteBuffer)
        self.toRemoteBuffer = self.toRemoteBuffer[sent:]

    def handle_close(self) -> None:
        self.close()
        if self.sender:
            self.sender.close()


class Sender(asyncore.dispatcher):
    def __init__(self, receiver, remoteip: str, remoteport: int) -> None:
        self.receiver = receiver
        receiver.sender = self
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((remoteip, remoteport))

    def handle_connect(self) -> None:
        pass

    def handle_read(self) -> None:
        read = self.recv(BUFSIZE)
        self.receiver.toRemoteBuffer += read

    def writable(self) -> bool:
        return len(self.receiver.fromRemoteBuffer) > 0

    def handle_write(self) -> None:
        sent = self.send(self.receiver.fromRemoteBuffer)
        self.receiver.fromRemoteBuffer = self.receiver.fromRemoteBuffer[sent:]

    def handle_close(self) -> None:
        self.close()
        self.receiver.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stackless socket server')
    parser.add_argument(
        '--local-host',
        action='store',
        dest='local_host',
        default=LOCAL_SERVER_HOST)
    parser.add_argument(
        '--local-port',
        action='store',
        dest='local_port',
        type=int,
        required=True)
    parser.add_argument(
        '--remote-host',
        action='store',
        dest='remote_host',
        default=REMOTE_SERVER_HOST)
    parser.add_argument(
        '--remote-port',
        action='store',
        dest='remote_port',
        type=int,
        default=80)
    args = parser.parse_args()
    print('Starting port forwarding local {}:{} => remote {}:{}'.format(
        args.local_host, args.local_port, args.remote_host, args.remote_port))
    PortForwarder(args.local_host, args.local_port,
                  args.remote_host, args.remote_port)
    asyncore.loop()
