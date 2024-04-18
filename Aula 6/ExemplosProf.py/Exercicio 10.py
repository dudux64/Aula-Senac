estudante = input("Você é estudante? (sim/não): ").lower()
idade = int(input("Qual a sua idade? "))
dia_semana = input("Qual o dia da semana? (segunda/quinta): ").lower()

if (estudante == "sim" or idade > 65) and (dia_semana in ["segunda", "terça", "quarta", "quinta"]):
    print("Você tem direito a um desconto!")
else:
    print("Você não tem direito a um desconto.")
