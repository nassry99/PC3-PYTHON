#Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
#la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
#calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
#cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
#formato. (Los métodos de cadena le serán de utilidad)

def obtener_calif():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones por favor: ")
            calificaciones = calificaciones_str.split(',')
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones]
            if all(0 <= calificacion <= 20 for calificacion in calificaciones_enteros):
                return calificaciones_enteros
            else:
                print("Error: Las calificaciones deben estar de 0 a 20.")                
        except ValueError:
            print("Error: Las calificaciones deben ser números enteros.")
        except Exception as e:
            print(f"Error inesperado: {e}")

calificaciones = obtener_calif()
print("Calificaciones ingresadas:", calificaciones)