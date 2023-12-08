import requests, json, os

def pegar_atualizacao(update_id, strURL):
    try:
        requisicao = f"{strURL}getUpdates?"
        if update_id:
            requisicao = f"{requisicao}&offset={update_id + 1}"
        resultado = requests.get(requisicao)
        return json.loads(resultado.content)
    except OSError:
        print(f"Ocorreu um erro: ", OSError)

def criar_resposta(comando, chat_id):
    if comando == "/start":
        return lista_de_comandos(chat_id)
    elif comando == '/infoH':
        return informacoes_hardware()
    elif comando == '/infoP':
        return lista_programas_instalados()
    elif comando == '/historic':
        return historico_navegacao()
    elif comando == '/infoU':
        return informacoes_usuario_logado()
    elif comando == '/listclient':
        return lista_agentes_online()
    else:
        return lista_de_comandos(chat_id)

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

def lista_de_comandos(chat_id):
    comandos = (
        "Bem-vindo ao Ambloom Bot!\n\n"
        "Você pode me controlar utilizando os seguintes comandos disponíveis:\n\n"
        "/infoH - Informações do hardware\n"
        "/infoP - Lista de programas instalados\n"
        "/infoU - Informações do usuário logado\n"
        "/historic - Histórico de navegação\n"
        "/listclient - Lista de agentes online com informações básicas\n" 
    )
    return comandos