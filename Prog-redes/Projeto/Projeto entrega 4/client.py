import threading
import socket
SERVER = 'localhost'
PORT = 5678
PROMPT = 'Insira sua msg > '

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((SERVER, PORT))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    print('Conectado \n')
    username = input('Insira um nome de usuário>')

    recebendo = threading.Thread(target=recebMensagens, args=[client])
    mandando = threading.Thread(target=mandMensages, args=[client, username])

    recebendo.start()
    mandando.start()

    recebendo.join()
    mandando.join()


def recebMensagens(client):
    while True:
        try:
            msg = client.recv(512).decode('utf-8')
            print("\n"+msg+"\n"+PROMPT)
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            client.close()
            break
            

def mandMensages(client, username):
    while True:
        try:
            msg = input(PROMPT)
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return

main()
