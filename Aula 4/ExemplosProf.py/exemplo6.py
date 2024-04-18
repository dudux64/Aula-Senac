nome = input("Entre com o nome: ")
sobrenome = input("Entre com o sobrenome: ")
assento = input("Entre com o número do assento: ")  
idade = int(input("Entre com a idade: "))  

if idade > 16:
    print(f"Ticket para o filme Velozes e Furiosos\nCliente:
           {nome} {sobrenome}\nAssento: {assento}") 
else:
    print("Ingresso não poderá ser emitido")
