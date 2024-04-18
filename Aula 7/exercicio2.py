hora = int(input("Qual a hora?: "))

if hora >= 8 and hora <= 17:
    for hora in range(hora,18):
        input(f"Oque vc vai fazer as {hora}?: ")
        
else:
    print("Você está fora do experiente ")