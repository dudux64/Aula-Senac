nome_cadastro = input("Qual o nome do arquivo que será Salvo?! ").strip().replace(" ", "_").lower()
diretorio = r"C:\Users\62129532024.1\Documents\GitHub\Arquivos-aulas-SENAC\Programação em Python U3\Aula8"
arquivo = f"{diretorio}\\{nome_cadastro}.txt"

print("Bem Vindo ao Cadastro de Alunos Do SENAC")

Cliente = input("Qual o Nome e Sobrenome Do Cliente? ")
CPF = int(input("Qual o CPF? "))
Telefone = int(input("Qual o Telefone? "))
Email = input("Qual o Email? ")
Endereco = input("Qual o Endereço? ")
Cidade = input("Qual a Cidade? ")
Estado = input("Qual o Estado? ")
CEP = int(input("Qual o CEP? "))


with open(arquivo, "w") as arquivo:
    arquivo.write(f"Nome:{Cliente}\n")
    arquivo.write(f"CPF:{CPF}\n")
    arquivo.write(f"Telefone:{Telefone}\n")
    arquivo.write(f"Email:{Email}\n")
    arquivo.write(f"Endereço:{Endereco}\n")
    arquivo.write(f"Cidade:{Cidade}\n")
    arquivo.write(f"Estado:{Estado}\n")
    arquivo.write(f"CEP:{CEP}\n")

print(f"O arquivo foi salvo no {diretorio}")


# CPF, Telefone,CEP São Inteiros
# Cliente, Email, Endereço, Cidade e Estado São Strings