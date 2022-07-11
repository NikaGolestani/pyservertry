from logging import exception
import socket
from time import sleep


HOST = '127.0.0.1'
PORT = 1401


server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
server_socket.connect((HOST , PORT))
msg = server_socket.recv(1024)
print(msg.decode())
while True:  
    server_socket.send(bytes ( input('enter:'),encoding='utf-8'))
    m = server_socket.recv(1024)
    print(m.decode())

