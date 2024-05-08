x  = int(input("Digite 1 pra somar, 2 para mostrar somatorio OU 3 para encerar: "))
numero= 0 
somatorio = 0  

while x <= 3 and x > 0 :

    if x == 1 :
        numero = int(input("Digite o numero que gostaria de somar: "))
        x = int(input("Digite 1 pra somar , 2 para mostrar somatorio OU 3 para encerar: "))
        somatorio = somatorio + numero
    elif x == 2 :
        print(somatorio)
        x = int(input("Digite 1 pra somar , 2 para mostrar somatorio OU 3 para encerar: "))
    elif x == 3 :
         print(f"O resuldado deu {somatorio}")
         break
    else: 
         print("Erro")

print("Erro")

















