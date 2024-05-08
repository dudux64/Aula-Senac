cat = int(input("Qual o numero da categoria do Carro?"))

if cat == 1:
    resultado = ("Você acabou de pedir um Carro BLACK")
elif cat == 2:
    resultado = ("Você acabou de pedir um Carro CONFORT")
elif cat == 3:
     resultado = ("Você acabou de pedir um Carro CONVENCIONAL")
elif cat == 4:
    resultado = ("Você acabou de pedir um Carro TAXI")
else:
    resultado = ("Você selecionou a opção errada")

print(resultado)
