#Programação Orientada a Objetos (POO)

# Exemplo de programação orientada a objetos
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo}")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.exibir_informacoes()  # Saída: Carro: Toyota Corolla
