# Criando o dicionário de inventário
inventario = {"maçãs": 30, "bananas": 45, "laranjas": 25}

while True:
    acao = input("Digite 'adicionar' para acrescentar o estoque,'subtrair' para remover as quantidades, 'mostrar' para ver o inventário,'adiçao' para adicionar um novo produto, 'remover' para remover um produto ou 'sair' para sair: ")
    
    if acao == 'sair':
        break
    elif acao == 'adicionar':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade (use número negativo para saída de estoque): "))
        
        if produto in inventario:
            inventario[produto] += quantidade
            print(f"Estoque de {produto} atualizado para {inventario[produto]}.")
        else:
            print("Produto não encontrado no inventário.")
    elif acao == 'subtrair':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade (use número negativo para saída de estoque): "))
        
        if produto in inventario:
            inventario[produto] -= quantidade
            print(f"Estoque de {produto} atualizado para {inventario[produto]}.")
        else:
            print("Produto não encontrado no inventário.")
    elif acao == 'remover':
        produto = input("Digite o nome do produto que deseja remover completamente do inventário: ")
        if produto in inventario:
            del inventario[produto]
            print(f"{produto} foi removido do inventário.")
        else:
            print("Produto não encontrado no inventário.")
    elif acao == 'mostrar':
        print("Inventário Atualizado:")
        for produto, estoque in inventario.items():
            print(f"{produto}: {estoque} unidades")
    elif acao == 'adiçao':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do estoque: "))
        inventario[produto] = quantidade  
        print(f"Estoque de {produto} atualizado para {inventario[produto]} unidades.")


# Exibindo o inventário final
print("Inventário Final:")
for produto, estoque in inventario.items():
    print(f"{produto}: {estoque} unidades")