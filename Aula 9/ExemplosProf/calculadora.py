import calculos
a= True
while a==True:
        operacao = input("Escolha a operação (1 para somar, 2 para multiplicar, 3 para dividir, 4 para subtrair, 5 para sair): ")
        
        if operacao == '5':
            print("Saindo do programa...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == '1':
            print("Resultado:", calculos.somar(num1, num2))
        elif operacao == '2':
            print("Resultado:", calculos.multiplicar(num1, num2))
        elif operacao == '3':
            resultado = calculos.dividir(num1, num2)
        elif operacao == '4':
            print("Resultado:", calculos.subtrair(num1, num2))
        elif operacao == '5':
            a=False
        else:
             print("Erro: Opção inválida.")
            

