numero = int(input("Digite o primeiro numero da calculadora: "))
numero2 = int(input("Digite o segundo numero da calculadora: ")) 
somatorio = 0  

while x <= 5 and x > 0 :

    if x == 1 :
        numero = int(input("Digite o numero que gostaria de somar: "))
        x = int(input("Digite 1 pra somar, 2 para multiplicar, 3 para dividir,4 para subtrair e 5 para encerrar"))
        somatorio = somatorio + numero
    elif x == 2 :
        numero = int(input("Digite o numero que gostaria de : "))
        x = int(input("Digite 1 pra somar, 2 para multiplicar, 3 para dividir,4 para subtrair e 5 para encerrar"))
        somatorio = somatorio * numero
    elif x == 3 :
        numero = int(input("Digite o numero que gostaria de somar: "))
        x = int(input("Digite 1 pra somar, 2 para multiplicar, 3 para dividir,4 para subtrair e 5 para encerrar"))
        somatorio = somatorio * numero
    elif x == 4 :
        numero = int(input("Digite o numero que gostaria de somar: "))
        x = int(input("Digite 1 pra somar, 2 para multiplicar, 3 para dividir,4 para subtrair e 5 para encerrar"))
        somatorio = somatorio * numero
    elif x == 5 :
         print(f"O resuldado deu {somatorio}")
         break
    else:
         print("Erro")

print("Erro")