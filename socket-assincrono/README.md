# CHATIDA o chat do IDA

## Utilização

1. Inicie o servidor: `python server.py`
2. Para cada cliente que desejar conectar, em uma nova aba digite: `python client.py`
3. Pronto! Você já pode desfrutar do chat.
4. Para desconectar um cliente, basta digitar: `see ya` na aba do cliente.
5. Obrigado pela preferência :D

## multithreads

Utilizei multithreads pensando que cada cliente será executado
em um desktop distinto, e cada conexão do cliente no servidor deve
utilizar uma thread para replicação de sua mensagem pensando em 
economia de espaço de memória, já que pode haver x conexões 