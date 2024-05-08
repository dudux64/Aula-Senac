# Cria uma matriz 9x9 representando um armário escolar vazio, onde cada slot inicialmente contém 'vazio'
armario = [["vazio"] * 9 for linha in range(9)]
while True:
    # Solicita ao usuário as coordenadas e o item
    linha = int(input("Digite a linha (0-8): "))
    coluna = int(input("Digite a coluna (0-8): "))
    item = input("Digite o nome do item a ser colocado: ")
    # Verifica se as coordenadas estão dentro dos limites
    if 0 <= linha < 9 and 0 <= coluna < 9:
        # Coloca o item no slot correspondente
        armario[linha][coluna] = item
        print(f"Item '{item}' adicionado na posição ({linha}, {coluna}).")
    else:
        print("Coordenadas inválidas! Por favor, digite valores entre 0 e 8 para linha e coluna.")
        
    remover = input("Deseja remover algum item? (s/n): ").lower()
    if remover == 's':
        linha = int(input("Digite a linha (0-8): "))
        coluna = int(input("Digite a coluna (0-8): "))
        armario[linha][coluna] = "vazio"
        print(f"Item '{item}' foi removido da posição ({linha}, {coluna}).")    
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja adicionar outro item? (s/n): ")
    if continuar.lower() != 's':
        break   

# Mostra o estado final do armário
print("Estado final do armário:")
for linha in armario:
    print(linha)