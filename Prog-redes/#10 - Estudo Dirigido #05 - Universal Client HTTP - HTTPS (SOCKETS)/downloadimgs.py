import socket, os, sys

# Função para obter o nome do arquivo a partir da url
def nomearquivo(url):
    url_dividida = url.split('/')
    return url_dividida[-1]

PORT = 80

try:
    # Obtem a url, a divide e separa o host e imagem
    url_completa               = input("Digite a URL completa da imagem: ")
    url                        = url_completa.split('//')
    url_host, BARRA, url_image = url[1].partition('/')
    url_image                  = BARRA + url_image

    # Aqui garante que o final do arquivo não venha sem uma formatação adequada
    arquivo = nomearquivo(url_completa)
    if '.' not in arquivo:
        arquivo += '.png'
     
    # Cria o socket da imagem e faz a requisição
    url_request = f'GET {url_image} HTTP/1.1\r\nHost: {url_host}\r\n\r\n'
    sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_img.connect((url_host, PORT))
    sock_img.sendall(url_request.encode())

    content_length = None
    imagem         = b''

    while True:
        # Recebe os dados em pedaços de 5120 bytes e continua o loop até baixar a imagem
        dados = sock_img.recv(5120)
        if not dados:
            break
        imagem = imagem + dados

        '''Procura pelo Content-Length e se o mesmo tiver conteúdo, seu tamanho será maior que 1 e, então, 
        o programa armazena esse conteúdo e utiliza como delimitador do loop.'''
        content_length_divisao = imagem.split(b'Content-Length:')
        if len(content_length_divisao) > 1:
            content_length = int(content_length_divisao[1].split()[0])

        # Verifica se todos os dados foram recebidos
        if content_length is not None and len(imagem) >= content_length:
            break
    sock_img.close()
    print(f'\nTamanho da Imagem: \033[92m{content_length} bytes\033[0m')

    # Separa os cabeçalhos e os dados da imagem
    delimiter = '\r\n\r\n'.encode()
    position  = imagem.find(delimiter)
    headers   = imagem[:position]
    dadosbin  = imagem[position + 4:]

    # Salva a imagem na pasta do programa
    DIR_ATUAL   = os.path.dirname(os.path.abspath(__file__))
    arquivo     = os.path.join(DIR_ATUAL, arquivo)
    file_output = open(arquivo, 'wb')
    file_output.write(dadosbin)
    file_output.close()
except Exception as error:
    print(f'ERRO.... \033[91m{sys.exc_info()[0]}\033[0m')
#------------------------------------------------------------------------------------------SUGESTÕES DE URLS DE IMAGENS------------------------------------------------------------------------------------------
#https://httpbin.org/image/png
#https://s2-g1.glbimg.com/wpRaLHmy-XmwDArMLmfn2UelIeE=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/8/X/15hbVnQlGAOdDXzBAG9Q/kanye-presidente.jpg
#https://s2-g1.glbimg.com/0LRPk7_alpjSxg2d115dYCrU_pE=/0x0:2000x1336/1008x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2019/o/a/AKU9eiS62UlUR0Cl07PA/kendrick-lamar-2019-04-07-dsc03029-fabio-tito-g1.jpg
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------