#!/usr/bin/env python
# -*- coding: utf-8 -*-


import select
import socket
import sys
import signal
import struct
import argparse


SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'


def marshal(data: str, encoding: str = 'utf-8') -> bytes:
    if encoding == 'pickle':
        import pickle
        return pickle.dumps(data)
    else:  # utf-8
        return bytes(data, encoding)


def unmarshal(data: bytes, encoding: str = 'utf-8') -> str:
    if encoding == 'pickle':
        import pickle
        return pickle.loads(data)[0]
    else:  # utf-8
        return data.decode()

# workaournd, bytes() require parameter type is string instead of tuple
# def send(channel, *args):


def send(channel, args: str):
    buffer = marshal(args)
    value = socket.htonl(len(buffer))
    size = struct.pack('L', value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    size = struct.calcsize('L')
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack('L', size)[0])
    except struct.error:
        return ''
    buf = channel.recv(size)
    while not buf or len(buf) < size:
        buf += channel.recv(size - len(buf))
    return unmarshal(buf)


class ChatServer(object):
    def __init__(self, port, backlog=5):
        self.clientCount = 0
        self.clientMap = {}
        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print('Sever listening to port %d' % port)
        self.server.listen(backlog)
        # catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        print('Shutdown server...')
        for client in self.clients:
            client.close()
        self.server.close()

    def get_client_name(self, client):
        info = self.clientMap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        inputs = [self.server, sys.stdin]
        self.clients = []
        running = True
        while running:
            try:
                readable, writable, exceptional = select.select(
                    inputs, self.clients, [])
            except select.error:
                break
            for sock in readable:
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print(
                        'Chat server: got connection %d from %s' %
                        (client.fileno(), address))

                    # read and login name
                    cname = receive(client).split('NAME: ')[1]

                    # compute client name and send back
                    self.clientCount += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientMap[client] = (address, cname)

                    # send joining info to other client
                    msg = '\n(Connected: New client (%d) from %s' % (
                        self.clientCount, self.get_client_name(client))
                    for other in self.clients:
                        send(other, msg)
                    self.clients.append(client)

                elif sock == sys.stdin:
                    junk = sys.stdin.readline()
                    running = False

                else:
                    # handle all other sockets
                    try:
                        data = receive(sock)
                        if data:
                            # send as new client's message
                            msg = '\n#[' + \
                                self.get_client_name(sock) + ']>>' + data
                            # send data to all, except ourself
                            for output in self.clients:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print('Chat server: %d hung up' % sock.fileno())
                            self.clientCount -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.clients.remove(sock)

                            # sending client leaving info to other
                            msg = '\n(Now huang up: Client from %s)' % self.get_client_name(
                                sock)
                            for client in self.clients:
                                send(client, msg)
                    except socket.error:
                        inputs.remove(sock)
                        self.clients.remove(sock)
        self.server.close()


class ChatClient(object):
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        self.prompt = '[' + '@'.join((name,
                                      socket.gethostname().split('.')[0])) + ']>'
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print('Now connected to chat server@ port %d' % self.port)
            self.connected = True
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']>'
        except socket.error:
            print('Failed to connect to chat server @ port %d' % self.port)
            sys.exit(1)

    def run(self):
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                readable, writable, exceptional = select.select(
                    [0, self.sock], [], [])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data:
                            send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print('Client shutting down.')
                            self.connected = False
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print('Client interruped...')
                self.sock.close()
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Socket Server Example with Select')
    parser.add_argument('--name', action='store', dest='name', required=True)
    parser.add_argument(
        '--port',
        action='store',
        dest='port',
        type=int,
        required=True)
    args = parser.parse_args()
    if args.name == CHAT_SERVER_NAME:
        server = ChatServer(args.port)
        server.run()
    else:
        client = ChatClient(name=args.name, port=args.port)
        client.run()
