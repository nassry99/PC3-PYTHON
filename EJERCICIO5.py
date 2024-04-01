#Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
#para:
#1. Display - Debe mostrar toda la información del estudiante (nombre y número de registro).
#2. setAge - Debe asignar la edad al estudiante
#3. setNota - Debe asignar las notas al estudiante.

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", self.notas)
        print()

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

# Ejemplo de uso
nombre_alumno = input("Ingrese el nombre del alumno: ")
numero_registro_alumno = input("Ingrese el número de registro del alumno: ")

alumno = Alumno(nombre_alumno, numero_registro_alumno)

alumno.display()

edad_alumno = int(input("Ingrese la edad del alumno: "))
alumno.set_age(edad_alumno)

notas_alumno = input("Ingrese las notas del alumno separadas por comas: ").split(',')
notas_alumno = [float(nota.strip()) for nota in notas_alumno]
alumno.set_notas(notas_alumno)

alumno.display()