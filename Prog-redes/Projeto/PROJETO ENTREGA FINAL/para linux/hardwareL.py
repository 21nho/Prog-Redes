import platform, subprocess

def infohardwareL():
    def memoria_linux():
        try:
            cabeçalho = subprocess.run('free | grep "total"', capture_output=True, text=True)
            memoria = subprocess.run('free -m | grep "Mem:"', capture_output=True, text=True)

            informacoes = f"\nInformações detalhadas sobre a memória física:\n{cabeçalho.stdout}\n{memoria.stdout}"

            return informacoes
        except:
            return f"Erro ao obter informações de memória"

    def disco_linux():
        try:
            cabeçalho = subprocess.run('df -h | grep -i "File"', shell=True, capture_output=True, text=True)
            discos = ["/dev/sda", "/dev/root", "/dev/mapper", "/dev/nvme0n1p1"]

            for disco in discos:
                try:
                    armazenamento = subprocess.run(f'df -h | grep -i "{disco}"', capture_output=True, text=True)
                    break
                except: continue 

            informacoes = f"\nInformações detalhadas sobre o disco:\n{cabeçalho.stdout}\n{armazenamento.stdout}"

            return informacoes
        except:
            return f"Erro ao obter informações de disco"

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
        f"\n----- INFORMAÇÕES DE DISCO -----\n{disco_linux()}\n"
        f"\n----- INFORMAÇÕES DE MEMÓRIA -----\n{memoria_linux()}"
    )

    return informacoes



        
