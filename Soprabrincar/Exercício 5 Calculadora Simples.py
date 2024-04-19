num1 = int(input("Digite o primeiro numero da calculadora: "))
num2 = int(input("Digite o segundo numero da calculadora: "))

mult = int(input("Digite 1 para soma,2 para subtração, 3 para divisão, 4 para multiplicação: "))

if mult ==1:
    resultado = num1 + num2
    print(f"O Resultado é {resultado}")
elif mult ==2:
    resultado = num1 - num2
    print(f"O Resultado é {resultado}")
elif mult ==3:
    resultado = num1 / num2
    print(f"O Resultado é {resultado}")
elif mult ==4:
    resultado = num1 * num2
    print(f"O Resultado é {resultado}")
else:
    print("ERRO")
