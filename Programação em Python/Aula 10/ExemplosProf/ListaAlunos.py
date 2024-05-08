# Perguntar quantos alunos tem na turma
numero_alunos = int(input("Quantos alunos tem na turma? "))

# Criar uma lista para armazenar os nomes dos alunos
lista_alunos = []

# Inserir os nomes dos alunos na lista
print("Por favor, insira os nomes dos alunos:")
for i in range(numero_alunos):
    nome = input(f"Nome do aluno {i + 1}: ").lower() # Convertendo para minúsculas antes de adicionar
    lista_alunos.append(nome)

# Contar quantos "Enzo" e "Valentina" estão na lista
contagem_enzo = lista_alunos.count("enzo")
contagem_valentina = lista_alunos.count("valentina")

# Exibir resultados
print(f"Total de alunos na turma: {numero_alunos}")
print(f"Quantidade de alunos chamados Enzo: {contagem_enzo}")
print(f"Quantidade de alunos chamados Valentina: {contagem_valentina}")
