# Solicita o nome da pessoa e prepara o nome do arquivo
nome_pessoa = input("Digite o nome da pessoa para criar o arquivo: ").strip().replace(" ", "_").lower()
diretorio = r"C:\Users\62129532024.1\Documents\GitHub\ExemplosAulaPython\Programação Backend\curriculo"
arquivo = f"{diretorio}\\{nome_pessoa}_curriculo.txt"
# Dicionário com os campos do currículo
campos = [
    "Nome completo",
    "Endereço",
    "Telefone",
    "Email",
    "Resumo",
    "Formação acadêmica",
    "Experiências profissionais",
    "Habilidades",
    "Idiomas"
]
# Coleta os dados do usuário
dados_curriculo = {campo: input(f"Digite seu {campo.lower()}: ") for campo in campos}
# Salva os dados no arquivo
with open(arquivo, 'w') as f:
    for campo, conteudo in dados_curriculo.items():
        f.write(f"{campo}: {conteudo}\n")
print(f"Currículo salvo em {arquivo}")
