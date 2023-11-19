import socket, sys, os
#----------------------------------------------------------------------------------------------------------------------------
# Definindo diretorio atual
DIR_ATUAL = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(DIR_ATUAL, 'protocolos.csv')

# Tratamento de arquivo
try:
    arquivo = open(arquivo_csv, 'r', encoding='utf-8')
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo_csv} não foi encontrado.")
    sys.exit(1)
except:
    print(f'\nERRO.... \033[91m{sys.exc_info()[0]}\033[0m')
    sys.exit(1)
#----------------------------------------------------------------------------------------------------------------------------

linhasformatadas = []

# Formatação do arquivo
for linha in arquivo:
    elementos = linha.split('", "')
    linhaformatada = []

    for item in elementos:
        itemformatado = item.strip('"\n')
        linhaformatada.append(itemformatado)
    linhasformatadas.append(linhaformatada)
arquivo.close()

for porta in linhasformatadas: porta[0] = int(porta[0]) # Converte as portas para números inteiros
TCP, UDP, TCPUDP = [], [], []

# Tratamento de Host
try:
    strHost = input("Insira o nome do host: ")
except:
    print(f'\nERRO.... \033[91m{sys.exc_info()[0]}\033[0m')
    sys.exit(1)

# Tratamento de IP do host
try:
    ipHost = socket.gethostbyname(strHost)
except:
    print(f'\nERRO.... \033[91m{sys.exc_info()[0]}\033[0m')
    sys.exit(1)

for linha in linhasformatadas: # Organiza as portas de acordo com seus protocolos
    if linha[1] == "TCP,UDP":
        TCPUDP.append(linha[0])
    elif linha[1] == "TCP":
        TCP.append(linha[0])
    elif linha[1] == "UDP":
        UDP.append(linha[0])

for porta in linhasformatadas: # Itera através das portas e verifica se estão abertas ou fechadas
    port = porta[0]

    try: # Verifica se a porta pertence a TCP, UDP, ou as duas e cria um socket para cada porta
        if port in TCP: 
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Responde \033[92m(Aberta)\033[0m')
            else:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Não Responde \033[91m(Fechada)\033[0m')

        elif port in TCPUDP:
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Responde \033[92m(Aberta)\033[0m')
            else:
                print(f'Porta {port}: Protocolo: TCP: {porta[2]}/ Status: Não Responde \033[91m(Fechada)\033[0m')

            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Responde \033[92m(Aberta)\033[0m')
            else:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Não Responde \033[91m(Fechada)\033[0m')

        elif port in UDP:
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Responde \033[92m(Aberta)\033[0m')
            else:
                print(f'Porta {port}: Protocolo: UDP: {porta[2]}/ Status: Não Responde \033[91m(Fechada)\033[0m')

        else: # Verifica se a porta está aberta ou fechada para um protocolo desconhecido
            sock.settimeout(1)
            if sock.connect_ex((ipHost, port)) == 0:
                print(f'Porta {port}: Protocolo: : {porta[2]}/ Status: Responde \033[92m(Aberta)\033[0m')
            else:
                print(f'Porta {port}: Protocolo: : {porta[2]}/ Status: Não Responde \033[91m(Fechada)\033[0m')
    except:
        print(f'\nERRO.... \033[91m{sys.exc_info()[0]}\033[0m')
    finally:
        sock.close()