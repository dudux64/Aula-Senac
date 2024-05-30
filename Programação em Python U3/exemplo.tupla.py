entrada = input("Entre com 5 nomes de Pessoas: ").lower()
valores = entrada.split(",")
minha_tupla = tuple(valores)
if len(valores) != 5:
    print("A lista não tem os 5 valores!")
else:
    print("Os Nomes foram:")
    for i in minha_tupla:
        print(i)

    print("Qual o nome vc quer selecionar?:")

    entrada = input("Entre com o nome que vc quer selecionar: ").lower()  
    if entrada in minha_tupla:
        print("O nome está na Tupla")
    else:
        print("O nome não está na Tupla")



