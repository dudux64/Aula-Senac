from utils import dobro

# Entrada do usuário
salario_mensal = float(input("Digite o seu salário mensal: R$"))

# Calcula o valor a receber no mês do 13º
valor_recebido = dobro(salario_mensal) 

# Imprime o resultado
print(f"Seu salário mensal é R${salario_mensal:.2f}. Você receberá R${valor_recebido:.2f}como 13º salário.")
