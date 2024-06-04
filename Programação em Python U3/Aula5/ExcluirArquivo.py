import os

# Especificar o nome do arquivo a ser excluído
nome_arquivo = 'exemplo.txt'

# Tentar excluir o arquivo
try:
    os.remove(nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' excluído com sucesso.")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
