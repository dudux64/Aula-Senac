def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Para evitar divisão por zero, vamos retornar None se b for zero.
    if b == 0:
        return None
    else:
        return a / b

def subtrair(a, b):
    return a - b