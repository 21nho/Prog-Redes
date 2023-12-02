import socket, os
from socket_constants import *

#--- Criando o socket TDP -----------------------------------------------------------------------------------------#
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                     #
try:tcp_socket.connect((HOST_SERVER, SOCKET_PORT))                                                                 #
except:print('\nNão foi possívvel se conectar ao servidor!\n')                                                     #
username = input('Insira o nome de usuário: ')                                                                     #
print('\nConectado')                                                                                               #
#--- Obtendo informações de usuário -------------------------------------------------------------------------------#
HOST    = socket.gethostname()                                                                                     #
IP      = socket.gethostbyname(HOST)                                                                               #
USUARIO = os.getlogin()                                                                                            #
infos = (f'{HOST}, {IP}, {USUARIO}')                                                                               #
infoh = infos.encode(CODE_PAGE)                                                                                    #
tcp_socket.send(infoh)                                                                                             #
#------------------------------------------------------------------------------------------------------------------#

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
    


# Fechando o socket
tcp_socket.close()
