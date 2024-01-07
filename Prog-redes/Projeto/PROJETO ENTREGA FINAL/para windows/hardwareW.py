import platform, subprocess

def infohardwareW():
    def memoria_windows():
        try:
            resultado = subprocess.run(['systeminfo'], capture_output=True, text=True)
            systeminfo = resultado.stdout
            memoria_total = [linha for linha in systeminfo.split('\n') if 'Mem¢ria f¡sica total:' in linha]
            total = memoria_total[0].split(':')[-1].strip()
            memoria_dis = [linha for linha in systeminfo.split('\n') if 'Mem¢ria f¡sica dispon¡vel:' in linha]
            disponivel = memoria_dis[0].split(':')[-1].strip()

            final = f"Memória Total: {total}\nMemória Disponível: {disponivel}"
            return final
        except:
            return "Não foi possível receber a informação de memória"

    def disco_windows():

        try:
            resultado = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'], capture_output=True, text=True)
            linhas = resultado.stdout.strip().split('\n')
            dados = linhas[2].split()
            vazio = int(dados[1]) / (1024 ** 3)
            total = int(dados[2]) / (1024 ** 3)

            informacoes_discos = f"Espaço livre em disco: {vazio:.2f} GB\nEspaço total em disco: {total:.2f} GB"
            return informacoes_discos
        except:
            return "Não foi possível receber a informação de disco"

    try:
        sistema_operacional = platform.system()
        processador = platform.processor()
        arquitetura = platform.architecture()
    except:
        return 'Não foi possível obter as informações de Hardware'

    informacoes = (
        f"\n----- INFORMAÇÕES DE CPU -----\n"
        f"Sistema Operacional: {sistema_operacional}\n"
        f"Processador: {processador}\n"
        f"Arquitetura: {arquitetura[0]} {arquitetura[1]}\n"
        f"\n----- INFORMAÇÕES DE DISCO -----\n{disco_windows()}\n"
        f"\n----- INFORMAÇÕES DE MEMÓRIA -----\n{memoria_windows()}"
    )

    return informacoes

print(infohardwareW())