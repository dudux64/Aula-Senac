class Aluno:
    def cadastro(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def imprimir(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"

# Lista para armazenar os alunos
cadastro_alunos = []

# Loop para coletar os dados de 10 alunos
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    curso = input("Digite o curso do aluno: ")
    aluno = Aluno()
    aluno.cadastro(nome, idade, curso)
    cadastro_alunos.append(aluno)

# Mostrando os dados dos alunos cadastrados
for aluno in cadastro_alunos:
    print(aluno.imprimir())
