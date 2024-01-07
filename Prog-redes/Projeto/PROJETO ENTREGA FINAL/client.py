import threading
import socket, os, time
SERVER = 'localhost'
PORT = 5678

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((SERVER, PORT))
        print("Conectado")
        USERNAME = input('Insira o nome de usuário:')
        HOST    = socket.gethostname()
        IP      = socket.gethostbyname(HOST)
        LOGIN = os.getlogin()
        infos = (f'{HOST}, {IP}, {LOGIN}, {USERNAME}')
        infoh = infos.encode('utf-8')

        try:
            client.send(infoh)
        except OSError:
            print(f'Erro ao enviar informações de usuário para o servidor')
            client.close()
            exit()
    except:
        return print('\nNão foi possível se conectar ao servidor!\n')
    
    while True:
        try:
            msg = client.recv(512).decode('utf-8')
            if msg is None:
                print('\nNão foi possível permanecer conectado no servidor!\n')
                client.close()
                return
            print(msg)
            funçao = criar_resposta(msg)
            print(funçao)
            client.send(f'{funçao}'.encode('utf-8'))
        except socket.timeout:
            print('\nNão foi possível receber dados do servidor.\n')

           
def criar_resposta(comando):
    dictopcoes = {
    '/infoH': informacoes_hardware(),
    '/infoP'   : lista_programas_instalados(),              '/infoU': informacoes_usuario_logado(),
    '/historic': historico_navegacao(),                '/listclient': lista_agentes_online(), }

    try:
        return dictopcoes[comando]
    except: 
        return 'comando invalido'


def informacoes_hardware():
    return "Informações do hardware onde o servidor está sendo executado."

def lista_programas_instalados():
    return "Lista de programas instalados no servidor."

def historico_navegacao():
    return "Histórico de navegação em diferentes navegadores."

def informacoes_usuario_logado():
    return "Informações detalhadas do usuário logado."

def lista_agentes_online():
    return "Lista dos agentes online com informações básicas."



main()