import random

# Cria uma matriz 5x5 = Mapa do JOGO
matriz = [[' ' for _ in range(5)] for _ in range(5)]

numerodesub = 5

# Preenchendo a matriz com os submarinos
for _ in range(numerodesub):
    while True:
        linha_aleatoria = random.randint(0, 4)
        coluna_aleatoria = random.randint(0, 4)
        if matriz[linha_aleatoria][coluna_aleatoria] == ' ':
            matriz[linha_aleatoria][coluna_aleatoria] = 'S'
            break

# Substituindo espaços por zeros
for linha in range(5):
    for coluna in range(5):
        if matriz[linha][coluna] == ' ':
            matriz[linha][coluna] = 0

# Mostrando a matriz atualizada
for linha in matriz:
    print(linha)

# Loop para solicitar as coordenadas do usuário de linha e coluna
while True:
    try:
        linha_especifica = int(input("Qual a linha do Submarino?: (0-4)? "))
        coluna_especifica = int(input("Qual a coluna do Submarino?: (0-4)? "))
        
        if 0 <= linha_especifica < 5 and 0 <= coluna_especifica < 5:
            valor = matriz[linha_especifica][coluna_especifica]
            print(f"\nValor na linha {linha_especifica}, coluna {coluna_especifica} é {valor}")
            
            if valor == 'S':
                print("Parabéns! Você achou um Submarino.")
            else:
                print("Você errou! Não tem Submarino no local")
        else:
            print("Coordenadas fora dos limites! Tente novamente.")
    except:
        print("Entrada inválida! Por favor, insira números inteiros.")
