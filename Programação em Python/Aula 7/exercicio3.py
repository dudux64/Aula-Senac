ano = int(input("Qual o ano que vc nasceu?: "))
anoat = int(input("Qual o ano atual?"))
resultado = (anoat - ano)
atual = 0

for atual in range(1,resultado):
    print(f"No ano de {ano + atual} voce tinha {(atual-1)+ 1}")

