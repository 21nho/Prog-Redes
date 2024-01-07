import subprocess

def progwindows():
    try:
        resultado = subprocess.run(['wmic', 'product', 'get', 'name'], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()
        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except:
        return f'Não foi possível obter as informações de programas instalados:'
    
retorno = progwindows()
print(retorno)
