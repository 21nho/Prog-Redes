import os, subprocess

def infouserL():
    def grupos_linux():
        try:
            usuario = os.getlogin()
            resultado = subprocess.run(['groups', usuario], capture_output=True, text=True)
            grupos = resultado.stdout.strip().split()
            secundarios = ('\n'.join(grupos[3:]))

            saida = f"\n--- Grupo Principal ---\n{grupos[2]}\n\n--- Grupos Secundários ---\n{secundarios}"
            return saida
        except:
            return 'Não foi possível obter as informações de grupos do usuário'

    return (f"Usuário: {os.getlogin()}\n"
        f"Diretório Inicial: {os.path.expanduser('~')}\n"
        f"Identificação de usuário: UID = {os.getuid()}\n"
        f"Os grupos do usuário são: {grupos_linux()}\n"
        f"\nO Shell padrão do Usuário é: {os.environ['SHELL']}")

