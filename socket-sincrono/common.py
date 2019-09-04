def get_user_message():
    message = raw_input("Digite sua mensagem: ").strip()
    message_length = len(message)
    return message, message_length, message
