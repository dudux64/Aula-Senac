numero = int(input("Até quantos numeros e para ir?: "))

if numero <= 1:
    print(f"{numero} não é primo")
elif numero <= 3:
    print(f"{numero} é primo")
elif numero % 2 == 0 or numero % 3 == 0:
    print(f"{numero} não é primo")
else:
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            print(f"{numero} não é primo")
            break
        i += 6
    else:
        print(f"{numero} é primo")