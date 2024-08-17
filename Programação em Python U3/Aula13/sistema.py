import random

matriz = [['vazio'] * 3 for linha in range(3)]

for i in range(100):
    numero_aleatorio = random.randint(0, 2)
    numero_aleatorio1 = random.randint(0, 2)
    matriz[numero_aleatorio][numero_aleatorio1] = random.randint(0,20)

numeros_maiores_que_10 = []

for linha in matriz:
    for elemento in linha:
        if isinstance(elemento, int) and elemento > 10:
            numeros_maiores_que_10.append(elemento)

print(matriz)
print(numeros_maiores_que_10)
