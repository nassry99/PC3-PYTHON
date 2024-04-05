from EJERCICIO10Operaciones import Circulo, Rectangulo

def mostrar_menu():
    print("Menú de Importación:")
    print("1. Importar clase Circulo")
    print("2. Importar clase Rectangulo")
    print("3. Salir")

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print("El área del círculo es:", area)

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print("El área del rectángulo es:", area)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()


