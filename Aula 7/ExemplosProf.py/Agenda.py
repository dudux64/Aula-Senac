# Perguntando a hora atual ao usuário
hora_atual = int(input("Digite a hora atual (formato 24h, apenas a hora): "))

# Verificando se está fora do horário de expediente
if hora_atual < 8 or hora_atual >= 18:
    print("Erro: Fora do horário de expediente. O sistema só funciona entre 8h e 18h.")
else:
    # Se estiver dentro do horário de expediente, prosseguir com a agenda
    for hora in range(hora_atual, 18):
        atividade = input(f"O que você fez ou vai fazer às {hora}h? ")

