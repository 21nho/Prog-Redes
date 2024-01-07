import subprocess

def proglinux():
    try:
        resultado = subprocess.run(['apt', 'list', '--installed'], capture_output=True, text=True)
        linhas = resultado.stdout.splitlines()

        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except:
        return f'Não foi possível obter as informações de programas instalados:'

proglinux()
