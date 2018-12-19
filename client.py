from __future__ import print_function
import socket
import threading
import sys
import time
import os


class Client:
    userName = ""
    chat_history = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    user_established = False

    def __init__(self, address):

        self.clearScrn()
        self.userName = raw_input("Username: ").encode('utf-8')
        self.sock.connect((address, 10000))
        self.sock.send(bytes(self.userName))
        data = self.sock.recv(1024)
        self.user_established = (data == 'Connection Success\n')

        inputThread = threading.Thread(target=self.sendMsg)
        inputThread.daemon = True
        inputThread.start()

        while True:
            data = self.sock.recv(1024)
            self.chat_history.append(data)
            if not data:
                break
            self.clearScrn()
            for i in self.chat_history:
                print(i + '-->')
            print('  --> ', end='')

    def sendMsg(self):
        while True:
            msg = bytes(raw_input(" --> ").encode('utf-8'))
            self.sock.send("\n" + msg)

    def clearScrn(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')




















