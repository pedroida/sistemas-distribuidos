import socket
import threading
from common import port

from common import get_user_message

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', port))

should_listen = True


def listen_server(sock):
    while should_listen:
        expected_data_size = int(sock.recv(4).decode())

        received_data = ''
        while len(received_data) < expected_data_size:
            received_data += sock.recv(4).decode()

        print(received_data)
        print("\nDigite sua mensagem:")


listener = threading.Thread(target=listen_server, args=(sock,))
listener.setDaemon(True)
listener.start()

self_message = ''

while self_message != 'see ya':
    message, send_data_size, self_message = get_user_message()

    sock.sendall(str(send_data_size).zfill(4).encode())

    sock.sendall(message.encode())

should_listen = False
sock.close()
