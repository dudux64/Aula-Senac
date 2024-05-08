# Solicita ao usuário a quantidade de números de Fibonacci que deseja
n = int(input("Quantos números da sequência de Fibonacci você deseja? "))

# Inicializa as variáveis para os dois primeiros números de Fibonacci
a, b = 0, 1
fibonacci = []

# Gera a sequência de Fibonacci
for _ in range(n):
    fibonacci.append(b)
    a, b = b, a + b

print("Sequência de Fibonacci:", fibonacci)

# Lista para armazenar números primos
primos = []

# Loop para verificar quais números na sequência de Fibonacci são primos
for num in fibonacci:
    # Um número primo é definido como tendo exatamente dois divisores: 1 e ele mesmo
    divisor_count = 0  # Contador para o número de divisores
    for i in range(1, num + 1):  # Loop de 1 até o número incluindo ele mesmo
        if num % i == 0:  # Verifica se 'num' é divisível por 'i'
            divisor_count += 1  # Incrementa o contador de divisores
    if divisor_count == 2:  # Se o número tem exatamente dois divisores, então é primo
        primos.append(num)

print("Números primos na sequência de Fibonacci:", primos)
print("Total de números primos na sequência:", len(primos))
