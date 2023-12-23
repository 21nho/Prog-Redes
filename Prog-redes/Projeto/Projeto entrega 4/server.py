import threading
import socket
SERVER = '0.0.0.0'
PORT = 5678

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((SERVER, PORT))
        server.listen(5)
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=cliInteraction, args=[client, addr])
        thread.start()

def cliInteraction(client, addr):
    while True:
        try:
            msg = client.recv(512)
            broadcast(msg, client, addr)
        except:
            deleteClient(client)
            break


def broadcast(msg, client, addr):
    msg = f"{addr}: {msg.decode('utf-8')}"
    print (msg)
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg.encode('utf-8'))
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)

main()