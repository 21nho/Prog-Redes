import socket, os
from socket_constants import *

#--- Criando o socket TDP -----------------------------------------------------------------------------------------#
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_socket.connect((HOST_SERVER, SOCKET_PORT))
except OSError:
    print(f'\nNão foi possível se conectar ao servidor!')
    exit()

username = input('Insira o nome de usuário: ')
print('\nConectado')

#--- Obtendo informações de usuário -------------------------------------------------------------------------------#
HOST    = socket.gethostname()
IP      = socket.gethostbyname(HOST)
USUARIO = os.getlogin()
infos = (f'{HOST}, {IP}, {USUARIO}')
infoh = infos.encode(CODE_PAGE)

try:
    tcp_socket.send(infoh)
except OSError:
    print(f'Erro ao enviar informações de usuário para o servidor')
    tcp_socket.close()
    exit()
#------------------------------------------------------------------------------------------------------------------#

try:
    while True:
        mensagem = input("Digite sua mensagem (ou '/exit' para sair): ")
        if mensagem == "/exit":
            break

        if mensagem:
            tcp_socket.send(f'<{username}> {mensagem}'.encode(CODE_PAGE))

            # Recebendo echo do servidor
            dado_recebido     = tcp_socket.recv(BUFFER_SIZE)
            mensagem_recebida = dado_recebido.decode(CODE_PAGE)
            print(f'Echo Recebido: {mensagem_recebida}')

except OSError:
    print(f'Erro durante a execução do cliente')

finally:
    # Fechando o socket
    tcp_socket.close
