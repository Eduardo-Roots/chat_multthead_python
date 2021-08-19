# -*- coding: utf-8 -*-

import socket
SERVER = "127.0.0.1"
PORT = 12000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Do Cliente",'UTF-8'))
while True:
  in_data =  client.recv(1024)
  print("Sua mensagem :" ,in_data.decode())
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  if out_data=='fui':
    break
client.close()
