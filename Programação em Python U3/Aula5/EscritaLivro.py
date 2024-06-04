print("Bem Vindo a Biblioteca Senac")

while True:
    local_solicitado = 'Arquivos-aulas-SENAC\Programação em Python U3\Aula5\exemplo.txt'
    nome = input("Digite o nome do livro: ")
    autor= input("Digite o nome do autor do livro: ")

    with open(local_solicitado, 'a') as arquivo:
        arquivo.writelines(nome + "\n")
        arquivo.writelines(autor +"\n")
    print(f"Conteúdo do arquivo 'exemplo.txt' Foi criado")
    resposta = int(input("Se adicionar mais um livro digite 1 se quiser parar digite 2:"))
    if  resposta == 2:
        print("Obrigado por usar a biblioteca Senac")
        break
        
