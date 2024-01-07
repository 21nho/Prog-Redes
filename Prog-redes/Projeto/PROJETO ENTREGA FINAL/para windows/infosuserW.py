import subprocess,os

def infouserW():
    def gruposusuariowin():
        try:
            # Usa subprocess para utilizar o comando como se estivesse no cmd
            resultado = subprocess.run(['net', 'user', os.getlogin()], capture_output=True, text=True, encoding='cp437')
            linhas = resultado.stdout.strip().splitlines()

            imprimir = False
            inicio = 'AssociaçΣes de Grupo Local'
            fim = 'Comando concluído com êxito.'
            informações = ""

            # Vai de linha em linha e quando achar a string de inicio define "imrpimir" como TRUE e começa a armazenar na variável vazia,
            # quando acha a string de fim quebra o loop
            for linha in linhas:
                if fim in linha:
                    break
                if inicio in linha:
                    imprimir = True
                if imprimir:
                    linha = linha.replace('AssociaçΣes', 'Associações')
                    informações += linha + '\n'
            return informações
        except:
            return 'Não foi possível obter as informações do Agente'

    def usersid():
        try:    
            user = os.getlogin()
            result = subprocess.run([f"wmic useraccount where name='{user}' get sid"], capture_output=True, text=True)
            lines = result.stdout.split('\n')

            for line in lines:
                if "S-1" in line:
                    return line
        except:
            return 'Não foi possível obter as informações do Agente'

    usuario = os.environ['USERNAME']
    print(f"\n---------------- INFORMAÇÕES DE USUÁRIO ----------------\n\nO Diretório Inicial do Usuário {usuario} é: '{os.environ['USERPROFILE']}'\n")
    print(f"O SID do usuário {usuario} é: {usersid()}\n")
    print(f"Os grupos que o usuário {usuario} está associado são:\n{gruposusuariowin()}")
    print(f"Nome do Executável do usuário {usuario} é: {os.path.basename(os.environ['ComSpec'])}")

infouserW()
