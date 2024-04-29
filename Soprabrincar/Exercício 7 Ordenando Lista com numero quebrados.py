numeros = []
b = int(input("Quantos numeros terá na lista?: "))

for i in range(b):
    n = float(input("Adcione numeros quebrados na lista: "))
    numeros.append(n) 
numeros.sort()

print(f"Lista ordenada: {numeros}")