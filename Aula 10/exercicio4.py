numero = int(input("Até que numero a sequencia fibonacci vai?: "))
lista = []
y = 0
b = 1
c = 0
lista.append(b)
b = b + y

for x in range(0,numero):
    c = b + y 
    y = b + c
    lista.append(c)
 

print(lista)
 