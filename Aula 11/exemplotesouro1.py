lista_tesouro = [1,2,3,4,5,6,7,8,9,10] # ÍNDICES = 0 a 9


TESOURO = 5
tentativas = 3


for contagem in lista_tesouro:
    escolha = int(input("Informe a posição que deseja tentar: "))
    tentativas -= 1
    if escolha == TESOURO:
        print("Parabéns, você achou o tesouro!")
        exit()

    else:
        print(f"Você errou. {tentativas} chances sobrando!")

    if tentativas == 0: 
        print("Você esgotou suas chances. Programa encerrando...")
        quit()
