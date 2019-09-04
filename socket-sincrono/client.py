import socket

from common import get_user_message

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 9001))

last_message = ''

while last_message != 'see ya':

    expected_data_size = int(sock.recv(4).decode())
    print("Tamanho de dado esperado = {} \n".format(expected_data_size))

    received_data = ''
    while len(received_data) < expected_data_size:
        received_data += sock.recv(4).decode()

    print(received_data)

    last_message = received_data
    if last_message == 'see ya':
        break

    message, send_data_size, last_message = get_user_message()

    sock.sendall(str(send_data_size).zfill(4).encode())

    sock.sendall(message.encode())

sock.close()
