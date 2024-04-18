categoria = int(input("Digite o numero da categoria do tapete desejada:"))
metragem = float(input("A metragem:"))
#Condicional para determinar a categoria
if categoria == 1:
    precofinal = metragem*10
    print(f"o valor será de {precofinal} reais")
elif categoria == 2:
    precofinal = metragem*20
    print(f"o valor será de {precofinal} reais")
elif categoria == 3:
    precofinal = metragem*30
    print(f"o valorserá de {precofinal} reais")
else:
    print("dados invalidos")

