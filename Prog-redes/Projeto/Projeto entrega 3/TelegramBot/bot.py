import requests 
from funcoes import *

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
            update_id = mensagem['update_id']
            chat_id = mensagem['message']['from']['id']
            try: comando = mensagem['message']['text']
            except: comando = "..."
            resposta = criar_resposta(comando, chat_id, registros)
            link_de_envio = f"{strURL}sendMessage?chat_id={chat_id}&text={resposta}"
            requests.get(link_de_envio)
    except OSError: print("Ocorreu um erro... ", OSError)
    salvar_registros(registros, arquivo_registros)
