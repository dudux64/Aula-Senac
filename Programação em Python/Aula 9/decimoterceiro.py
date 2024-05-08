from utils import dobro

salario_mensal = float(input("Digite o seu salário mensal:R$"))

valor_recebibo = dobro(salario_mensal)

print(f"Seu salário mensal é R$ {salario_mensal: .2f}. Você receberá R${salario_mensal: .2f} Como 13º Salário.")
