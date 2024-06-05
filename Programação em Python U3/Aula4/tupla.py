# Pedindo ao usuário para inserir três valores
entrada = input("Digite três valores separados por vírgulas: ")
valores = entrada.split(",")  # Isso cria uma lista dos valores
minha_tupla = tuple(valores)  # Convertendo a lista em uma tupla

# Mostrando cada elemento da tupla
print("Os valores inseridos foram:")
for elemento in minha_tupla:
    print(elemento)

