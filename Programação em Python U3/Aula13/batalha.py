import numpy as np

def jogo_batalha_naval():
    tabuleiro = np.zeros((5, 5))
    posicao_navio = (np.random.randint(0, 5), np.random.randint(0, 5))
    posicao_navio2 = (np.random.randint(0, 5), np.random.randint(0, 5))
    tentativas = 0
    acertou = False

    try:
        print("Bem vindo ao jogo da batalha naval!")
        print(f"Você tem 5 tentativas para acertar o navio")
        while not acertou:
            print(f"\nTabuleiro:\n{tabuleiro,posicao_navio,posicao_navio2}")
            print(f"Seu numero de tentativas é: {tentativas}")
            linha = int(input("Adivinhe a linha (0-4): "))
            coluna = int(input("Adivinhe a coluna (0-4): "))
            tentativas += 1
            if (linha, coluna) == posicao_navio and (linha, coluna) == posicao_navio2:
                print(f"Você acertou o navio em {tentativas} tentativas!")
                acertou = True
            elif tentativas > 4:
                print(f"Você atingio o numero maximo de tentativas!")
                acertou = True
            else:
                tabuleiro[linha, coluna] = 1
                print("Errou! Tente novamente.")
    except:print("Error, Você Selecionou o numero errado")

jogo_batalha_naval()
