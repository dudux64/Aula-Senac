idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você ainda não está elegível para votar.")
elif 18 <= idade < 70:
    print("Seu voto é obrigatório.")
else:
    print("Você está elegível para votar, mas não é obrigatório.")
