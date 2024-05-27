print("Sistema de Avaliação!")
valorcarro = int (input("Qual o valor do carro:"))
avaliacao = int (input("Qual a Avaliação?"))

if avaliacao <= 50:
    valorcarro -= (valorcarro*30/100)
    print(f"O valor final ficou de {valorcarro}:")
elif avaliacao <= 80:
    valorcarro == valorcarro
    print(f"O valor final ficou de {valorcarro}:")
elif avaliacao <= 100:
    valorcarro += (valorcarro*20/100)
    print(f"O valor final ficou de {valorcarro}:")
else:
    print("Avaliação Incorreta!")

