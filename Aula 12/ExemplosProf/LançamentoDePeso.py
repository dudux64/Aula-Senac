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

lista_atletas2 = []
numeroAtleta2 = 1
print("Por favor, insira a distância dos lançamentos:")
for i in range(4):
    distancia = float(input(f"O atleta {i + 1} fez o lançamento a qual distância?: "))
    lista_atletas2.append(distancia)

for distanciaporatleta in lista_atletas2:
    print(f"O atleta {numeroAtleta2} lançou a uma distancia de {distanciaporatleta} metros")
    numeroAtleta2 += 1
lista_atletas2.sort()
lista_atletas2.reverse()
print("Lançamentos ordenados:", lista_atletas2)

imprimir = input("deseja ver os resultado finais? (S/N)  ")

if imprimir.lower() == "s":
    print(lista_atletas)
    print(lista_atletas1)
    print(lista_atletas2)
