import threading, platform, subprocess
import socket, os, time
from LinuxFun import *
from funcoeswin import *
from browser_history.browsers import Chrome, Edge, Firefox
import os, sqlite3


SERVER = 'localhost'
PORT = 5678
SO = platform.system()

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
            try:
                funçao = criar_respostaW(msg)
            except: 
                funçao = criar_respostaL(msg)
            finally: print('deu n')

            client.send(f'{funçao}'.encode('utf-8'))
        except socket.timeout:
            print('\nNão foi possível receber dados do servidor.\n')



           
def criar_respostaW(comando):
    dictopcoes = {
    '/infoH': informacoes_hardwareW(),
    '/infoP'   : lista_programas_instaladosW(),              '/infoU': informacoes_usuario_logadoW(),
    '/historic': historico_navegacaoW(),                '/listclient': lista_agentes_onlineW(), }

    try:
        return dictopcoes[comando]
    except: 
        return 'comando invalido'


def criar_respostaL(comando):
    dictopcoes = {
    '/infoH': informacoes_hardwareL(),
    '/infoP'   : lista_programas_instaladosL(),              '/infoU': informacoes_usuario_logadoL(),
    '/historic': historico_navegacaoL(),                '/listclient': lista_agentes_onlineL(), }

    try:
        return dictopcoes[comando]
    except: 
        return 'comando invalido'


# LINUX

def informacoes_hardwareL():
    informacoes = infohardwareL()
    return informacoes 

def lista_programas_instaladosL():
    informacoes = proglinux()
    return informacoes

def historico_navegacaoL(navegador):
    return "Histórico de navegação em diferentes navegadores."

def informacoes_usuario_logadoL():
    informacoes = ipagentes()
    return informacoes

def lista_agentes_onlineL():
    return "Lista dos agentes online com informações básicas."


# WINDOWS
def informacoes_hardwareW():
    return infohardwareW()

def lista_programas_instaladosW():
    return progwindows()

def historico_navegacaoW():
    return 'historicos de navegação'

def informacoes_usuario_logadoW():
    return ipagentes()

def lista_agentes_onlineW():
    return "Lista dos agentes online com informações básicas."



def ipagentes():
    try:
        informacoes_agente = f'''
        ---- INFORMAÇÕES DO AGENTE ----

        Nome do host: {socket.gethostname()}
        Usuário logado: {os.getlogin()}
        IP do Host: {socket.gethostbyname(socket.gethostname())}
        '''
        return informacoes_agente
    except:
        return 'Não foi possível obter as informações do Agente'





main()