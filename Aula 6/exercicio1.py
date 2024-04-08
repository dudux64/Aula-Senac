cartblack = input("Você tem o cartão black de acesso? (Sim/Não)").lower()
ingvip = input("Você tem o Ingresso vip de acesso ao lounge? (Sim/Não)").lower()

if cartblack == "sim" or ingvip == "sim":
    print("Você tem acesso a sala vip!")
else:
    print("Você não tem acesso a sala vip!")
