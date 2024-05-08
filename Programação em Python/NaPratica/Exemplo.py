vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

def soma_vetores(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        return "Os vetores devem ter o mesmo tamanho."
    
    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] + vetor2[i])
    
    return resultado
print(soma_vetores(vetor1, vetor2))
