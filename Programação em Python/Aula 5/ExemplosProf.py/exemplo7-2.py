vendas = int(input("Digite o número de vendas: "))

# Condicional para determinar o nível
if vendas <= 50:
    print(f"Com {vendas} vendas, você está no Nível 1 de desempenho.")
elif vendas <= 100:
     print(f"Com {vendas} vendas, você está no Nível 2 de desempenho.")
elif vendas <= 150:
     print(f"Com {vendas} vendas, você está no Nível 3 de desempenho.")
elif vendas <= 200:
    print(f"Com {vendas} vendas, você está no Nível 4 de desempenho.")
else:
     print(f"Com {vendas} vendas, você está no Nível 5 de desempenho.")
