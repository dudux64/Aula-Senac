expresso = int(10)
tradicional = int(15)
capuccino = int(20)
latte = int(18)
descafeinado = int(22)

cafe = int(input("Digite 1 Para Expresso,2 Para Tradicional, 3 Para Capuccino, 4 Para Latte, 5 para Descafeinado: "))
if cafe == 1:
        for expresso in range(10,0,-1):
            print(f"Café pronto em:{expresso}")
        print("Café Pronto")
elif cafe == 2:
        for tradicional in range(15,0,-1):
            print(f"Café pronto em:{tradicional}")
        print("Café Pronto")
elif cafe == 3:
        for capuccino in range(20,0,-1):
            print(f"Café pronto em:{capuccino}")
        print("Café Pronto")
elif cafe == 4:
        for latte in range(18,0,-1):
            print(f"Café pronto em:{latte}")
        print("Café Pronto")
elif cafe == 5:
        for descafeinado in range(22,0,-1):
            print(f"Café pronto em:{descafeinado}")
        print("Café Pronto")
else:
    print("Erro")
