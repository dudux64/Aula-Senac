print("Bem Vindo ao Criador de Curriculo")

local = input("Qual o nome do aquivo: .txt:")

while True:
    nome = input(f"Coloque seu Nome: " ) 
    idade = input(f"Coloque sua Idade: ")
    endereco = input(f"Coloque seu endereço: ")
    telefone = input("Coloque seu telefone: ")
    email = input("Coloque seu email: ")                   

    with open(local, 'w') as arquivo:
        arquivo.write(f"Nome:{nome}""\n")
        arquivo.write(f"Idade:{idade}""\n")
        arquivo.write(f"Endereco:{endereco}""\n")
        arquivo.write(f"Telefone:{telefone}""\n")
        arquivo.write(f"Email:{email}""\n")
    print(f"Conteúdo foi adicionado ao Curriculo")
    resposta = input("Se adicionar mais uma informação do Curriculo digite 1 se quiser Parar digite 2:")
    if  resposta == 2:
        print("Você Saiu do Programa de Curriculo")
        break