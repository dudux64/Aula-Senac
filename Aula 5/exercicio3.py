nome = input("Qual o nome do clinte?: ")
metro = int(input("Quantos metros de tapete?: "))
tapete = input("Qual a qualidade do tapete")

if tapete == "convencional":
   orçamento = metro * 10
   print(f"Olá {nome} o valor do seu orçamento ficou {orçamento}")
elif tapete == "premium":
   orçamento = metro * 20
   print(f"Olá {nome} o valor do seu orçamento ficou {orçamento}")
elif tapete == "maxpremium":
   orçamento = metro * 30
   print(f"Olá {nome} o valor do seu orçamento ficou {orçamento}")
   
else:
   print("ORÇAMENTO INCORRETO")





















