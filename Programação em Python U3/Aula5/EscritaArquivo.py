#Especificar o nome do arquivo e o conteúdo
nome_arquivo = 'exemplo.txt'
conteudo = 'Este é um exemplo de conteudo.'

#Abrir o arquivo no modo de escrita e escrever o conteudo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(conteudo)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
