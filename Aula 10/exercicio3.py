lista = []
alunos = int(input("Quantos alunos tem na turma?: "))
quantidaideal = 0
for quantidadeideal in range(alunos,0,-1):
    nome = input("Qual o nome do proximo aluno?: ").lower()
    lista.append (nome)
aluno1 = "enzo"
aluno2 = "valentina"
quantidade1 = lista.count(aluno1)
quantidade2 = lista.count(aluno2)
print(f"Existem {quantidade1} {aluno1}")
print(f"Existem {quantidade2} {aluno2}")
print(lista)
