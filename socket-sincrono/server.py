import socket
from common import get_user_message

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = sock.bind(('localhost', 9001))

sock.listen(1)

last_message = ''

print("Aguardando conexao")
connection, address_client = sock.accept()

while last_message != 'see ya':

    message, message_length, last_message = get_user_message()
    connection.sendall(str(message_length).zfill(4).encode())

    connection.sendall(message.encode())

    if last_message == 'see ya':
        break

    expected_data_size = ''
    while expected_data_size == '':
        expected_data_size += connection.recv(4).decode()
    expected_data_size = int(expected_data_size)

    received_data = ''
    while len(received_data) < expected_data_size:
        received_data += connection.recv(4).decode()

    print(received_data)

    last_message = received_data

sock.close()
connection.close()

