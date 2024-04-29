# Cria uma matriz 9x9 representando um armário escolar vazio, onde cada slot inicialmente contém 'vazio'
armario = [["vazio"] * 9 for linha in range(9)]

while True:
    # Solicita ao usuário as coordenadas
    linha = int(input("Digite a linha (0-8): "))
    coluna = int(input("Digite a coluna (0-8): "))
    # Verifica se as coordenadas estão dentro dos limites
    if 0 <= linha < 9 and 0 <= coluna < 9:
        # Pergunta se deseja adicionar ou remover um item
        acao = input("Você deseja adicionar ou remover um item? (adicionar/remover): ")
        if acao.lower() == "adicionar":
            item = input("Digite o nome do item a ser colocado: ")
            armario[linha][coluna] = item
            print(f"Item '{item}' adicionado na posição ({linha}, {coluna}).")
        elif acao.lower() == "remover":
            if armario[linha][coluna] != "vazio":
                print(f"Item '{armario[linha][coluna]}' removido da posição ({linha}, {coluna}).")
                armario[linha][coluna] = "vazio"
            else:
                print("Essa posição já está vazia.")
        else:
            print("Ação inválida! Digite 'adicionar' ou 'remover'.")
    else:
        print("Coordenadas inválidas! Por favor, digite valores entre 0 e 8 para linha e coluna")
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        break
# Mostra o estado final do armário
print("Estado final do armário:")
for linha in armario:
    print(linha)

