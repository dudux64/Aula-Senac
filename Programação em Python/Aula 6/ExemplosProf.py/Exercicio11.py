total = 0
while True:
    preco = float(input("Digite o preço do produto (digite 0 para encerrar): "))
    if preco == 0:
        break
    total += preco

print("Total acumulado:", total)
