vendas = int(input("Digite o número de vendas: "))

# Condicional para determinar o nível
if vendas <= 50:
    nivel = 1
elif vendas <= 100:
    nivel = 2
elif vendas <= 150:
    nivel = 3
elif vendas <= 200:
    nivel = 4
else:
    nivel = 5

# Exibindo o resultado
print(f"Com {vendas} vendas, você está no Nível {nivel} de desempenho.")