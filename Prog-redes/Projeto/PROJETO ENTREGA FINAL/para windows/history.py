from browser_history.browsers import Chrome, Edge, Firefox
import os, sqlite3

def hisgoogleW():
    try:
        b = Chrome()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)  # Linha separadora
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except:
        return "Erro ao tentar receber histórico de navegação do Google!!!"
    
def hisedgeW():
    try:
        b = Edge()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)  # Linha separadora
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except:
        return "Erro ao tentar receber histórico de navegação do Microsoft Edge!!!"

def hisfirefoxW():
    try:
        b = Firefox()
        outputs = b.fetch_history()

        historico = [outputs.histories[0]]
        for i in range(1, len(outputs.histories)):
            if outputs.histories[i] != outputs.histories[i-1]:
                historico.append(outputs.histories[i])

        for info in historico[-10:]:
            print("=" * 50)  # Linha separadora
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Title: {info[2]}")
    except:
        return "Erro ao tentar receber histórico de navegação do Mozila Firefox!!!"

def hisoperaW():
    try:
        con = sqlite3.connect(fr'C:\Users{os.getlogin()}\AppData\Roaming\Opera Software\Opera Stable\Default\History')
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        results = cur.fetchall()
        for result in results:
            print(result)
    except:
        return "Erro ao tentar receber histórico de navegação do Opera!!!"

