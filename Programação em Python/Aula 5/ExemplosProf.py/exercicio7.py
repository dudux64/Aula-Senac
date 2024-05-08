categoria = int(input("Digite o numero da categoria desejada:"))

#Condicional para determinar a categoria
if categoria == 1:
    nomeCategoria = "black"
elif categoria == 2:
    nomeCategoria = "Confort"
elif categoria == 3:
   nomeCategoria = "Convencional"
elif categoria == 4:
    nomeCategoria = "taxi"
else:
    nomeCategoria = "invalida:"
    #Exibindo o resultado
print(f"voce selecionou a categoria {nomeCategoria}")

