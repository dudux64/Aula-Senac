from utils import soma
from utils import subtracao
from utils import multi
from utils import divisao
x = int(input("Digite 1 para somar,2 para multiplicar, 3 para dividir,4 para subtrair,5 para encerrar: "))
numero = int(input("Digite o primeiro numero da calculadora: "))
numero1 = int(input("Digite o segundo numero da calculadora: "))
resultado = 0
y = 0
    
while y <= 5 and x > 0 :   
        if x == 1:
                resultado = soma(numero,numero1)
                print(resultado)
                x = int(input("Digite 1 para somar,2 para multiplicar, 3 para dividir,4 para subtrair,5 para encerrar: "))

        elif x == 2:
                resultado = multi(numero,numero1)
                print(resultado)
                x = int(input("Digite 1 para somar,2 para multiplicar, 3 para dividir,4 para subtrair,5 para encerrar: "))
        elif x == 3:
                resultado = divisao(numero,numero1)
                print(resultado)
                x = int(input("Digite 1 para somar,2 para multiplicar, 3 para dividir,4 para subtrair,5 para encerrar: "))
        elif x == 4:
                resultado = subtracao(numero,numero1)
                print(resultado)
                x = int(input("Digite 1 para somar,2 para multiplicar, 3 para dividir,4 para subtrair,5 para encerrar: "))
        elif x == 5:
                print("OPERAÇÃO ENCERRADA!")
                break
        else:
                print("ERRO")
                break

    

