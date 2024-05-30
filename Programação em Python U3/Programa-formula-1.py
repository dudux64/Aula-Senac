print("Bem vindo ao Programa de Classificação")

lista_classificacion,lista_tempo = [], []
lista_classificacion1,lista_tempo1 = [], []
lista_classificacion2,lista_tempo2 = [], []

print("Digite o nome dos 7 primeiros pilotos e tempo da Q1")
for i in range(7):
    nome = input(f"Q1 Piloto {i+1}:")
    tempo = input(f"Q1 Tempo {i+1}:")
    lista_classificacion.append(nome)
    lista_tempo.append(tempo)
    print(f"O {lista_classificacion[i]} Ficou com o Tempo de {lista_tempo[i]}m")

print("Digite o nome dos 5 primeiros pilotos e tempo da Q2 ")
for i in range(5):
    nome = input(f"Q2 Piloto {i+1}:")
    tempo = input(f"Q2 Tempo {i+1}:")
    lista_classificacion1.append(nome)
    lista_tempo1.append(tempo)
    print(f"O {lista_classificacion1[i]} Ficou com o Tempo de {lista_tempo1[i]}m")

print("Digite o nome dos 3 primeiros pilotos e tempo da Q3 ")
for i in range(3):
    nome = input(f"Q3 Piloto {i+1}:")
    tempo = input(f"Q3 Tempo {i+1}:")
    lista_classificacion2.append(nome)
    lista_tempo2.append(tempo)
    print(f"O {lista_classificacion2[i]} Ficou com o Tempo de {lista_tempo2[i]}m")

print("\nResultados da Primeira Classificatória:")
print("Pilotos: ")
for nome in lista_classificacion:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in lista_tempo:
    print(f"{tempo:.2f} segundos", end=", ")

print("\nResultados da Segunda Classificatória:")
print("Pilotos: ")
for nome in lista_classificacion1:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in lista_tempo1:
    print(f"{tempo:.2f} segundos", end=", ")

print("\nResultados da Terceira Classificatória:")
print("Pilotos: ")
for nome in lista_classificacion2:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in lista_tempo2:
    print(f"{tempo:.2f} segundos", end=", ")