#imports
import requests
from time import sleep

#variaveis
aposta = 1.7
cont = 0

with open("banca.txt", "r") as arquivo:
    banca = arquivo.read()
    banca = float(banca)

while True:

    try:
        url = "https://blaze.com/api/crash_games/recent"
        response = requests.get(url)
        r = response.json()
        val1 = r[0]["id"]
        crash = r[0]["crash_point"]

        while True:
            sleep(4)
            response = requests.get(url)
            r = response.json()
            val2 = r[0]["id"]
            if val1 != val2:
                crash = r[0]["crash_point"]
                break
        #Aposta
        crash = float(crash)

        if aposta > banca:
            print("FALIU")
            break

        if crash >= 4:
            banca += aposta*4 - aposta
            aposta = 1.7
            with open("banca.txt", "w") as arquivo:
                arquivo.write(str(banca))
                banca = float(banca)
            cont = 0
        else:
            banca -= aposta
            aposta *= 1.35
            with open("banca.txt", "w") as arquivo:
                arquivo.write(str(banca))
                banca = float(banca)
            cont += 1

        print(
            f"banca: \033[32m{banca:.2f}\033[m - crash: \033[33m{crash}\033[m - sequencia de perca: \033[31m{cont}\033[m")

    except:
        continue