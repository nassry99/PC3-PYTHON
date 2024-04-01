#Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
#“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.

import math
#definimos la clase
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

# Ejemplo de uso y aplicacion
radio_circulo = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio_circulo)
area_circulo = circulo.area()
print("El área del círculo es:", area_circulo)
