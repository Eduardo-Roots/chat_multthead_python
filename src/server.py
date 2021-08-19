# -*- coding: utf-8 -*-

import socket, threading

class ClientThread(threading.Thread):

    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Nova conexão iniciada: ", clientAddress)

    def run(self):
        print ("Connectado com: ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='fui':
              break
            print (msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        print ("Cliente ", clientAddress , " desconnectado...")

LOCALHOST = "127.0.0.1"
PORT = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Servidor Online!")
print("Aguardando Conexão...")

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
