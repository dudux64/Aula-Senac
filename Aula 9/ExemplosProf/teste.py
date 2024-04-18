from utils import multiplicacao, divisao, soma, subtracao

num1 = float(input("Escolha um número para a operação"))
num2 = float(input("Escolha outro número"))
operacao = int(input("Digite 1 para somar os números \n2 para multiplicar \n3 para dividir \n4 para subtrair."))
adicao = soma(num1, num2)
subt = subtracao(num1, num2)
mult = multiplicacao(num1, num2)
div = divisao(num1, num2)

if operacao == 1:
    print(adicao)
elif operacao == 2:
    print(mult)
elif operacao == 3:
    print(div)
elif operacao == 4:
    print(subt)
elif operacao == 5:
    print("Programa encerrado")
else:
    print("Erro. Escolha entre os números 1 e 5")