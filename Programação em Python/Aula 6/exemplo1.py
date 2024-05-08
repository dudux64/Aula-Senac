idade = int(input("Digite sua idade: "))
assinante = input("Você é assinante do pass? (Sim/Não): ").lower()

if idade >= 18 and assinante == "sim":
    print("Você Tem Acesso ao Game Pass!")

else:
    print("Você Não Tem Acesso ao Game Pass.")
