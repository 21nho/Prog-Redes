import requests, json, os

def carregar_registros(arquivo_registros):
    try:
        print('chamando a função "carregar_registros"')
        arquivo = open(arquivo_registros, "r")
        registros = json.load(arquivo)
        arquivo.close()
        return registros
    except FileNotFoundError:
        return {}

def salvar_registros(registros, arquivo_registros):
    try:
        print('chamando a função "salvar_registros\n')
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
    print('chamando a função "pegar_atualização"')
    return json.loads(resultado.content)

def criar_resposta(comando, chat_id, registros):
    dictopcoes = {
    "/start"   : primeiro_contato(chat_id, registros),      '/infoH': informacoes_hardware(),
    '/infoP'   : lista_programas_instalados(),              '/infoU': informacoes_usuario_logado(),
    '/historic': historico_navegacao(),                '/listclient': lista_agentes_online(), }
    
    try:
        print('chamando a função "criar_resposta"')
        return dictopcoes[comando]
    except: 
        print('chamando a função "criar_resposta"')
        return mensagem_inicial


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


def primeiro_contato(chat_id, registros):
    print('chamando a função "primeiro_contato"')
    if chat_id not in registros:
        registros[chat_id] = {"primeiro_login": True}
        mensagem_inicio = (
            "Bem-vindo ao Ambloom Bot! Esta é a sua primeira vez aqui então eu vou lhe ajudar.\n\n"
            'Para acessar a lista de comandos disponíveis, use o comando "/comandos".'
        )
        return mensagem_inicio
    else:
        return mensagem_inicial

mensagem_inicial = (
    "Eu estou aqui para ajudar você a conferir informações sobre os usuários atualmente logados ao servidor.\n\n"
    "Você pode me controlar utilizando os seguintes comandos disponíveis:\n\n"
    "/infoH - Informações do hardware\n"
    "/infoP - Lista de programas instalados\n"
    "/infoU - Informações do usuário logado\n"
    "/historic - Histórico de navegação\n"
    "/listclient - Lista de agentes online com informações básicas\n" 
    )
