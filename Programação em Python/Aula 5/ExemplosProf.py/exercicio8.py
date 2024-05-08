categoria = int(input("Digite o numero da categoria desejada:"))
distancia = float(input("Digite a distancia que irá percorrer:"))
#Condicional para determinar a categoria
if categoria == 1:
    precofinal = distancia*2
    print(f"o valor da corrida Black será de {precofinal} reais")
elif categoria == 2:
    precofinal = distancia*1.5
    print(f"o valor da corrida confort será de {precofinal} reais")
elif categoria == 3:
   print(f"o valor da corrida convencional será de {distancia} reais")
elif categoria == 4:
    precofinal = distancia*3
    print(f"o valor da corrida de táxi será de {precofinal} reais")
else:
    print("dados invalidos")


