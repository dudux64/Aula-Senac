curso = input("Qual o nome do curso: ")
aluno = int(input("Qual a quantidade de aluno? "))

if aluno >= 5:
    print(f"Turma de {curso} Criada Com Sucesso")
else:
    print("A Turma não tem o numero suficiente de alunos")