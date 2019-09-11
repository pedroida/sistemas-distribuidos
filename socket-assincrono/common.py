def get_user_message():
    message = raw_input("Digite sua mensagem: \n").strip()
    message_length = len(message)
    return message, message_length, message


port = 9001


class SockConnection:
    connection = ''
    address = ''

    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
