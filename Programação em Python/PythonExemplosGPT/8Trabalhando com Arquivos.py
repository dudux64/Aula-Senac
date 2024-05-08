#Trabalhando com Arquivos

# Exemplo de manipulação de arquivos
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())  # strip() remove espaços em branco e quebras de linha
