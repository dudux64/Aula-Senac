# Pedindo ao usuário para inserir uma frase
frase = input("Digite uma frase: ")

# Inicializando contadores
cont_letras = 0
cont_espaços = 0
cont_numeros = 0

# Iterando através dos caracteres da frase
for caracter in frase:
    # Verificando se o caracter é uma letra
    if caracter.isalpha():
        cont_letras += 1
    # Verificando se o caracter é um espaço
    elif caracter.isspace():
        cont_espaços += 1
    # Verificando se o caracter é um número
    elif caracter.isdigit():
        cont_numeros += 1

# Imprimindo os resultados
print("Número de letras:", cont_letras)
print("Número de espaços:", cont_espaços)
print("Número de números:", cont_numeros)
