import random

print("Bem-vindo ao jogo de caça ao tesouro!")
print("Tente encontrar  o tesouro.Você tem 3 tentatvias.")
print("Escolha um número entre 1 e 9 para procurar o tesouro.")

resultado = int(input("Em qual casa está o tesouro? "))
tentativa = 0
aleatorio = random.randint(1, 9)

while resultado != aleatorio:
    if tentativa < 2:
        print("Você Errou!")
        resultado = int(input("Em qual casa está o tesouro? "))
        tentativa += 1
    else:
        print(f"Você expirou suas tentativas! estava no {aleatorio}")
        break

if resultado == aleatorio:
    print("Você Acertou!")
    
