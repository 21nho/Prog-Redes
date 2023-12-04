import socket
from socket_constants import *

def main():
    try:
        print('Recebendo Mensagens...\n\n')

        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((HOST_SERVER, SOCKET_PORT)) 
        tcp_socket.listen(MAX_LISTEN)

        while True:
            # Aceita a conexão com o cliente
            conexao, cliente = tcp_socket.accept()
            print('Conectado por: ', cliente)
            
            try:
                infos(conexao)
                
                while True:
                    mensagem = conexao.recv(BUFFER_SIZE)
                    print(mensagem.decode(CODE_PAGE))
                    if not mensagem:
                        break
                    
                    # Devolvendo uma mensagem (echo) ao cliente
                    mensagem_retorno = (f'Devolvendo mensagem recebida... " {mensagem.decode(CODE_PAGE)} "')
                    conexao.send(mensagem_retorno.encode(CODE_PAGE))

            except OSError:
                print(f"Erro durante a comunicação com o cliente")

            finally:
                print('Finalizando Conexão do Cliente ', cliente)
                conexao.close()
                break

    except OSError:
        print(f"Erro durante a execução do servidor")

def infos(conexao):
    try:
        infomsg = conexao.recv(BUFFER_SIZE).decode('utf-8')
        infomsg = infomsg.split(',')
        host, ip, usuario = infomsg[0], infomsg[1], infomsg[2]
        print(f'HOST   : {host} \nIP     :{ip} \nUSUÁRIO:{usuario}\n' )
    except OSError:
        print(f"Erro ao processar informações do cliente")


'''
    FUTUROS COMANDOS DO BOT TELEGRAM

def comandosBOT(comando):
    elif comando == "/info-h":
        # comando para solicitar aos agentes informações do hardware onde estão sendo executados
    elif comando == "/info-p":
        # comando para solicitar aos agentes a lista de programas instalados no computador
    elif comando == "/historic":
        # comando para solicitar aos agentes o histórico de navegação
    elif comando == "/info-u":
        # comando para solicitar aos agentes informações detalhadas do usuário que está logado
    elif comando == "/listclient":
        # comando que lista os agentes que estão on-line trazendo informações '''

main()
