#faça um programa que mostre a simulação de um emprestimo, onde a taxa de juros de 8.333%ao mês(juros simples) e monstre quanto o usuario deverá em 1 ano.

valor = int(input("Qual o valor da Fatura?: "))
juros = float(8.3)
valor1 = valor * juros / 100 * 12
valor2 = valor + valor1

print(f"Simulação com a taxa de juros depois de 1 ano {valor2}")