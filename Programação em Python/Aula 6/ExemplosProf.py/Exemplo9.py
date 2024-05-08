idade = int(input("Digite sua idade: "))
assinante = input("Você é assinante do game pass? (sim/não): ").lower()

if idade >= 18 and assinante == "sim":
    print("Você tem acesso ao game pass!")
else:
    print("Você não tem acesso ao game pass.")
