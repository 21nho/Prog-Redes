import os, sqlite3

def hisfirefoxL():
    firefox = f"/home/{os.getlogin()}/.mozilla/firefox/"
    diretorio = [folder for folder in os.listdir(firefox) if folder.endswith(".default-esr")][0]
    caminho = os.path.join(firefox, diretorio, "places.sqlite")

    con = sqlite3.connect(caminho)
    cur = con.cursor()

    cur.execute("select url, title, visit_count from moz_places")

    resultado = cur.fetchall()

    for item in resultado:
        url, title, visit_count = item
        print(f"URL: {url}\nTitle: {title}\nVisit Count: {visit_count}\n")

    con.close()

def hisgoogleL():
    con = sqlite3.connect(f"/home/{os.getlogin()}/.config/google-chrome/Default/History")
    cur = con.cursor()
    cur.execute("select url, title, visit_count from urls")
    results = cur.fetchall()
    for result in results:
        print(result)

def hisedgeL():
    con = sqlite3.connect(f"/home/{os.getlogin()}/.config/microsoft-edge/Default/History")
    cur = con.cursor()
    cur.execute("select url, title, visit_count from urls")
    results = cur.fetchall()
    for result in results:
        print(result)

def operaL():
    con = sqlite3.connect(f"/home/{os.getlogin()}/.config/opera/Default/History")
    cur = con.cursor()
    cur.execute("select url, title, visit_count from urls")
    results = cur.fetchall()
    for result in results:
        print(result)