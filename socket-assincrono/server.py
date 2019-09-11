# coding=utf-8
import socket
from common import get_user_message
import multiprocessing
import threading
from common import port, SockConnection

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = sock.bind(('localhost', port))
sock.listen(0)


def send_message_to_clients(message, current_client):
    for socket_connection in connections:
        if socket_connection != current_client:
            socket_connection.connection.sendall(str(len(message)).zfill(4).encode())
            socket_connection.connection.sendall(message.encode())


def listen_client(current_client):
    current_client_last_message = ''

    while current_client_last_message != 'see ya':
        expected_data_size = ''
        while expected_data_size == '':
            expected_data_size += current_client.connection.recv(4).decode()
        expected_data_size = int(expected_data_size)

        received_data = ''
        while len(received_data) < expected_data_size:
            received_data += current_client.connection.recv(4).decode()

        formatted_message = "Cliente {0}: {1}".format(current_client.address, received_data)
        current_client_last_message = received_data
        print(formatted_message)

        send_message_to_clients(formatted_message, current_client)

    connections.remove(current_client)
    current_client.connection.close()


last_message = ''
connections = []

while True:
    print("Aguardando conexão")
    connection, address_client = sock.accept()
    new_connection = SockConnection(connection, address_client)
    connections.append(new_connection)
    print("{} conectado".format(new_connection.address))

    worker = threading.Thread(target=listen_client, args=(new_connection,))
    worker.setDaemon(True)
    worker.start()
    # message, message_length, last_message = get_user_message()
    # connection.sendall(str(message_length).zfill(4).encode())
    #
    # connection.sendall(message.encode())
    #
    # if last_message == 'see ya':
    #     break
    #
    # expected_data_size = ''
    # while expected_data_size == '':
    #     expected_data_size += connection.recv(4).decode()
    # expected_data_size = int(expected_data_size)
    #
    # received_data = ''
    # while len(received_data) < expected_data_size:
    #     received_data += connection.recv(4).decode()
    #
    # print(received_data)
    #
    # last_message = received_data

sock.close()
