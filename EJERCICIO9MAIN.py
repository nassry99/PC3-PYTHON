


import EJERCICIO9OPERACIONES

def main():
    try:
        # Solicitar al usuario que ingrese dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Ejecutar las funciones del módulo operaciones con los números ingresados
        print("Suma:", EJERCICIO9OPERACIONES.suma(num1, num2))
        print("Resta:", EJERCICIO9OPERACIONES.resta(num1, num2))
        print("Producto:", EJERCICIO9OPERACIONES.producto(num1, num2))
        print("División:", EJERCICIO9OPERACIONES.division(num1, num2))
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()

