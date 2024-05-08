n = int(input("Até qual numero do fibonacci deseja chegar?: "))
a, b = 0, 1

print("Sequência de Fibonacci:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b