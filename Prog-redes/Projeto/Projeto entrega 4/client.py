import threading
import socket
SERVER = 'localhost'
PORT = 5678


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((SERVER, PORT))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    print('\nConectado')

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
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break
            

def mandMensages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


main()