# Crie um programa que ao clicar "1" some um número informado pelo usúario.
# A clicar "2", mostre o somatório.
# Ao clicar "3", encerre o programa.
# E se clicar em qualquer outro número, apreça uma mensagem de erro.

#exemplo do professor

soma = 0 

while True:
    print("\nmenu: ")
    print("1 - Adicionar um número á soma")
    print("2 - Exibir soma atual")
    print("3 - sair ")
    opcao = int(input("Escolha um opção (', 2 ou 3): ")) # receba a opçao do usúario

    if opcao == 1:
        numero = input("Digite um número para adicionar à soma: ")
        soma += float(numero)
        print(f"Número {numero} adciona à soma.")

    elif opcao == 2:
        print(f"Soma atual: {soma}") # Exibe a soma atual

    elif opcao == 3:
        break

    else:
        print("Opção invalida. Por favor, escolha 1, 2 ou 3.") #Mensagem para opção invalida
    
print("Programa encerrado. Soma final: ", soma)

