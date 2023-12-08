import requests, time

while True:
    token = "6731238648:AAF0nfYufZRsi9MgkGor1AcCoaxol8jJ9tk"
    strURL = f"https://api.telegram.org/bot{token}/getUpdates"
    resultado = requests.get(strURL)
    print(resultado.json())
    time.sleep(10)