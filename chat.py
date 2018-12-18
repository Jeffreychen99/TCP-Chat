import socket
import threading
import sys
import time
import random
import os

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    user_connection_dict = {}

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            print(a, c)
            if a not in self.user_connection_dict:
                self.user_connection_dict[a] = data
                data = "\n*" + data + "* has joined the chat\n"
            else:
                data = data.replace("\n", "")
                data = ">> " + self.user_connection_dict[a] + " : " + data

            print(data)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break

    def run(self):
        print('server running...\n')
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)

class Client:
    userName = ""
    chat_history = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address):

        self.clearScrn()
        self.userName = raw_input("Username: ").encode('utf-8')
        self.sock.connect((address, 10000))
        self.sock.send(bytes(self.userName))

        inputThread = threading.Thread(target=self.sendMsg)
        inputThread.daemon = True
        inputThread.start()

        while True:
            data = self.sock.recv(1024)
            print('got here 2')
            print('*' + str(data) + '*')
            self.chat_history.append(data)
            if not data:
                break
            self.clearScrn()
            for i in self.chat_history:
                print(i)

    def sendMsg(self):
        while True:
            print("got here")
            msg = bytes(raw_input(" --> ").encode('utf-8'))
            self.sock.send("\n" + msg)

    def clearScrn(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

if len(sys.argv) > 1:
    client = Client(sys.argv[1])
else:
    server = Server()
    print('\nserver created...')
    server.run()





















