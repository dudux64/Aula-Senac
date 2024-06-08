def jogo():
    escolhas = {
        1: "pedra",
        2: "papel",
        3: "tesoura",
        4: "lagarto",
        5: "spock"
    }
    
    resultados = {
        "tesoura": {"lagarto", "papel"},
        "pedra": {"lagarto", "tesoura"},
        "papel": {"pedra", "spock"},
        "lagarto": {"spock", "papel"},
        "spock": {"pedra", "tesoura"}
    }
    
    def obter_escolha(jogador):
        print(f"Agora escolha a opção do {jogador}")
        print("Digite 1 para pedra")
        print("Digite 2 para papel")
        print("Digite 3 para tesoura")
        print("Digite 4 para lagarto")
        print("Digite 5 para spock")
        
        while True:
            try:
                escolha = int(input("Escolha a opção: "))
                if escolha in escolhas:
                    return escolhas[escolha]
                else:
                    print("Escolha uma opção válida")
            except ValueError:
                print("Escolha uma opção válida")
    
    print("Vamos jogar!")
    
    resposta1 = obter_escolha("P1")
    resposta2 = obter_escolha("P2")
    
    if resposta2 in resultados[resposta1]:
        print("P1 ganha!")
    elif resposta1 in resultados[resposta2]:
        print("P2 ganha!")
    else:
        print("Empate!")

jogo()
