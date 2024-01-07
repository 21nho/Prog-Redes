import os, socket
def ipagentes():
    try:
        print(f"\n---- INFORMAÇÕES DO AGENTE ----\n\nNome do host: {socket.gethostname()}")
        print(f"Usuário logado: {os.getlogin()}")
        print(f"IP do Host: {socket.gethostbyname(socket.gethostname())}")
        print(f"Tempo de conexão ativa com o servidor: {calcular_conexao()}")
    except:
        return 'Não foi possível obter as informações do Agente'
ipagentes()