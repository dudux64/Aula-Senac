from utils import dobro

# Entrada do usuário
valor_emprestado = float(input("Digite o valor que deseja emprestar: R$"))

# Calcula o total a pagar com juros de 100% ao ano
total_pagar = dobro(valor_emprestado)

# Imprime o resultado
print(f"Valor emprestado: R${valor_emprestado:.2f}. 
Total a pagar após um ano: R${total_pagar:.2f}.")
