from multiprocessing.sharedctypes import Value
import random
elementos = []

while True:
    try:
        n = int(input("Insira um número inteiro: "))
        if n <= 0: raise ValueError  
    except ValueError:
        print("Insira um número inteiro positivo")
        continue
    else:
        break


for num in range(n):
    x = random.randint(1,100000000)
    elementos.append(x)

arquivo = open('arq01.txt','w')
arquivo.write(f"{elementos}")
arquivo.close()
