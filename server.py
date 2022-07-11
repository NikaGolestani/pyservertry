import socket
from time import sleep


HOST = '127.0.0.1'
PORT = 1401


server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
server_socket.bind((HOST , PORT))
server_socket.listen(1)

print('Start listening on {} : {}'.format(HOST , PORT))
while True:
    print('waiting for new connection...')
    client_socket , client_address = server_socket.accept()
    print('Accepted new connection...')
    client_socket.send(b'I will send back a reversed version of your input :-)\n \n')
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                client_socket.send(data[::-1])
                client_socket.send(b'\n \n')
                continue
        except Exception as reason:
            print('client connection closed: {}'.format(reason))
        client_socket.close()
        break