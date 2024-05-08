ano_atual = int(input("Qual é o ano atual? "))
ano_nascimento = int(input("Em que ano você nasceu? "))
for ano in range(ano_nascimento, ano_atual):
    idade = ano - ano_nascimento
    print(f"No ano {ano} você tinha {idade} anos.")
