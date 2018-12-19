import socket
import threading
import sys
import random
import os

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    user_connection_dict = {}
    users_list = []

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            if a not in self.user_connection_dict:
                if not self.valid_name(data):
                    c.send('Invalid name, please remove spaces and invalid characters') 
                elif data not in self.users_list:
                    self.users_list.append(data)
                    self.user_connection_dict[a] = data
                    c.send('Connection Success\n')
                    for connection in self.connections:
                        connection.send(' * ' + data + ' *   has joined the room')
                else:
                    c.send('This username has already been taken, please choose another...')
            else:
                print(data)
                for connection in self.connections:
                    connection.send('>> ' + self.user_connection_dict[a] + ': ' + data.replace("\n", ""))
                if not data:
                    break

    def valid_name(self, name):
        return not (':' in name or "'" in name or ' ' in name or '*' in name or '"' in name)

    def run(self):
        print('server running...\n')
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)




















