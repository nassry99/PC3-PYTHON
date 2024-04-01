#Implemente un programa que solicite al usuario una fracción, con
#formato X/Y, donde cada uno de X e Y es un número entero, y luego
#muestra, como un porcentaje redondeado al número entero más
#cercano, donde se indicará la cantidad de combustible en el
#tanque. Se debe tener en cuenta los siguientes casos:
#- Colocar E en caso X/Y sea menor a 1% del total
#- Colocar F en caso X/Y sea mayor a 99%.
#- En otro caso, devolver el valor en porcentaje %
#También debe tomar en cuenta los siguientes casos:
#- X y Y deben ser números enteros
#- X debe ser menor o igual a Y, y Y != 0
#De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
#cualquier excepción como ValueError o ZeroDivisionError.


def obtener_porcentaje(f):
    try:
        numerador, denominador = map(int, f.split('/'))
        if numerador > denominador or denominador == 0:
            raise ValueError
        resultado = numerador / denominador * 100
        if resultado < 1:
            return 'E'
        elif resultado > 99:
            return 'F'
        else:
            return f"{round(resultado)}%"
    except ValueError:
        print("Error: Ingrese una fraccion valida.")
        return obtener_porcentaje(input("Ingrese la fracción (en el formato X/Y): "))
    except ZeroDivisionError:
        print("Error: El denominador no puede ser cero.")
        return obtener_porcentaje(input("Ingrese la fracción (en el formato X/Y): "))

fraccion = input("Ingrese la fracción (en el formato X/Y): ")
print(obtener_porcentaje(fraccion))
