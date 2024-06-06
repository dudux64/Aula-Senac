print("Bem vindo ao meu programa!")
resposta = input("Qual a sua resposta?").lower()
def chake(a):
    if a == "ping":
        return "Pong"
    elif a == "time":
        return "Botafogo"
    elif a == "vivo":
        return "Morto"
    else:
        return "Palavra desconhecida"
    
print(chake(resposta))
