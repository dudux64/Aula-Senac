nome_turma = input("Digite o nome da turma: ")
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

if quantidade_alunos >= 5:
    print(f"A turma {nome_turma} foi cadastrada com sucesso!")
else:
    print("Não é possível cadastrar a turma. A quantidade mínima de alunos é 5.")
