from utils import dobro, multiplicacao

# Entrada do usuário
limite_atual = float(input("Digite o limite atual do seu cartão de crédito: R$"))

# Calcula o novo limite
novo_limite = dobro(limite_atual,limite)

# Imprime os resultados
print(f"Seu limite atual é R${limite_atual:.2f}. Seu novo limite seria R${novo_limite:.2f}.")
