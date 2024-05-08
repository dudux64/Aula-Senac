import time

# Menu de seleção de café
print("Selecione o tipo de café:")
print("1 - Expresso")
print("2 - Cappuccino")
print("3 - Latte")
print("4 - Descafeinado")

# Recebendo a escolha do usuário
escolha = int(input("Digite o número correspondente ao café desejado: "))

# Definindo o tempo de preparo baseado na escolha
if escolha == 1:
    tempo = 10
    tipo = "Expresso"
elif escolha == 2:
    tempo = 15
    tipo = "Cappuccino"
elif escolha == 3:
    tempo = 18
    tipo = "Latte"
elif escolha == 4:
    tempo = 20
    tipo = "Descafeinado"
else:
    print("Opção inválida.")
    quit()  # Sai do programa se a opção for inválida

# Iniciando a contagem regressiva
print(f"Preparando seu {tipo}... Por favor, aguarde.")
for i in range(tempo, 0, -1):
    print(f"{i} segundos restantes...")
    time.sleep(1)  # Espera 1 segundo

# Mensagem de sucesso
print(f"Seu {tipo} está pronto! Aproveite!")
