lista_atletas = []
numeroAtleta = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(10):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas.append(distancia)

for distanciaporatleta in lista_atletas:
    print(f"O atleta {numeroAtleta} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta += 1

lista_atletas.sort()
lista_atletas.reverse()
print("Lançamentos ordenados:", lista_atletas)

lista_atletas1 = []
numeroAtleta1 = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(7):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas1.append(distancia)

for distanciaporatleta in lista_atletas1:
    print(f"O atleta {numeroAtleta1} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta1 += 1
lista_atletas1.sort()
lista_atletas1.reverse()
print("Lançamentos ordenados:", lista_atletas1)

lista_atletas3 = []
numeroAtleta1 = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(4):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas3.append(distancia)

for distanciaporatleta in lista_atletas1:
    print(f"O atleta {numeroAtleta1} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta1 += 1
lista_atletas3.sort()
lista_atletas1.reverse()
print("Lançamentos ordenados:", lista_atletas1)

resposta = input("Você deseja ver as listas dos atletas? Sim ou Não? ").lower()

if resposta == "sim":
    print(f"A Primeira lista de atletas é {lista_atletas} \n") 
    print(f"A Segunda lista de atletas é {lista_atletas1} \n")
    print(f"A Terceira lista de atletas é {lista_atletas3} \n")

else:
    print("Fim do programa")
