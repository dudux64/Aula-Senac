nome_pessoa = input("Digite o nome da pessoa para criar o arquivo: ").strip().replace(" ", "_").lower()
diretorio = r"C:\Users\62129532024.1\Documents\GitHub\Arquivos-aulas-SENAC\Programação em Python U3\Aula6"
arquivo = f"{diretorio}\\{nome_pessoa}_curriculo.html"

conteudo = int(input("Digite o conteudo: ")) 

with open(arquivo, 'w') as arquivo:
    arquivo.write(conteudo)
