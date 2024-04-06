dist = float(input("Quantos KM Irá percorrer?: "))
cat = input("Qual a categoria?: ")


if cat == "black":
   resultado = dist *2
   print(f"O valor da corrida ficou: {resultado}") 
elif cat == "confort":
   resultado = dist *1.5
   print(f"O valor da corrida ficou: {resultado}") 
elif cat == "convencional":
   resultado = dist *1
   print(f"O valor da corrida ficou: {resultado}") 
elif cat == "taxi":
   resultado = dist *3
   print(f"O valor da corrida ficou: {resultado}") 
else:
   resultado = ("Você Escolheu a opção invalida")

print(resultado)


