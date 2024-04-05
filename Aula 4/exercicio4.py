nome = input("Qual o nome do cliente: ")
sobrenome = input("Qual o sobrenome do cliente: ")
assento = input("Qual a Cadeira do Cliente?")
idade = int(input("Entre com a idade: "))

if idade > 16:
    print(f"Ticket para o filme Velozes e Furiosos\nCliente: {nome}{sobrenome}\nAssento:{assento}")
else:
    print("Ingresso não poderá ser emitido")


#print ("Bem vindo ao Cinema " + nome + " " + sobrenome + " Sua cadeira é " + assento) [Feito por mim]
