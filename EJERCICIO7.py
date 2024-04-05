





import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

def main():
    x = float(input("Ingrese la coordenada x del centro del círculo: "))
    y = float(input("Ingrese la coordenada y del centro del círculo: "))
    radio = float(input("Ingrese el radio del círculo: "))

    centro = Punto(x, y)
    circulo = Circulo(centro, radio)
    
    print("Área del círculo:", circulo.area())
    print("Perímetro del círculo:", circulo.perimetro())

if __name__ == "__main__":
    main()
