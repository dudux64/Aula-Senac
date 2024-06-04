# Especificar o nome do arquivo a ser lido
nome_arquivo = 'exemplo.txt'

# Tentar abrir o arquivo no modo de leitura e ler o conteúdo
try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
