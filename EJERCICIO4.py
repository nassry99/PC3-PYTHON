#Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
#ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
#atributos de la clase.

#definimos la clase
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho

    def area(self):
        return self.largo * self.ancho

# Ejemplo de uso y aplicacion
largo_recta = float(input("Ingrese el largo del rectangulo: "))
ancho_recta = float(input("Ingrese el ancho del rectangulo: "))
rectangulo=Rectangulo(largo_recta,ancho_recta)
area_rectangulo = rectangulo.area()
print("El área del círculo es:", area_rectangulo)