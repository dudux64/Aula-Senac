vip = input("o usuario contém cartão vip? (sim/não)").lower()
ingresso = input("O usuario comprou ingresso? (sim/não): ").lower()

if vip == "sim" or ingresso == "sim":
    print("Você tem acesso a sala vip!")
else:
    print("Você não tem acesso a sala vip.")
