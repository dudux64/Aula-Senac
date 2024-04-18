soma = 0  # Inicializa a soma dos números
while True:
    print("\nMenu:")
    print("1 - Adicionar um número à soma")
    print("2 - Exibir soma atual")
    print("3 - Sair")
    opcao = input("Escolha uma opção (1, 2 ou 3): ")  # Recebe a opção do usuário

    if opcao == "1":
        numero = input("Digite um número para adicionar à soma: ")
        if numero > "0":
            soma += float(numero)  # Adiciona o número à soma total
            print(f"Número {numero} adicionado à soma.")
        else:
            print("Numero invalido")
    elif opcao == "2":
        print(f"Soma atual: {soma}")  # Exibe a soma atual
    elif opcao == "3":
        break 
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")  # Mensagem para opção inválida

print("Programa encerrado. Soma final:", soma)  # Exibe a soma final quando o loop termina
