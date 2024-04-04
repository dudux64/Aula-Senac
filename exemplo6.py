aluno = input("Qual o nome do aluno? ")
disciplina = input("Qual o nome da disciplina? ")
nota1 = int(input("Qual a nota do 1 Bimestre? "))
nota2 = int(input("Qual a nota do 2 Bimestre? "))
nota3 = int(input("Qual a nota do 3 Bimestre? "))
nota4 = int(input("Qual a nota do 4 Bimestre? "))
media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 6:
    print("Parabéns Você Foi APROVADO")
else:
    print("Você Está Reprovado!")
