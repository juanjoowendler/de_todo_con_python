__author__ = "Wendler Juan Jose"

"""
La oficina regional de la Junta Electoral Provincial ha pedido un programa
que almacene en un archivo los datos del padrón electoral de cierta localidad. Por cada
persona habilitada para votar en esa localidad, se guarda su dni, su nombre, su edad y un
indicador del sexo de esa persona ('v' para varón o 'm' para mujer). El programa debe incluir
un menú de opciones que permita:

1. Cargar datos en el archivo, pero cuidando que no se repita ninguna persona dentro
del mismo.

2. Mostrar los datos del archivo completo.

3. Determinar si en el archivo existe un votante con número de dni igual a x. Si existe,
mostrar todos sus datos. Si no, informar que no existe.

4. Determinar cuántos votantes son varones y cuántos son mujeres en el archivo.

5. Genere un segundo archivo, que contenga sólo los datos de los votantes mayores a 70
años.

6. Mostrar el archivo generado en el punto anterior.
"""

import os.path
import pickle


class Votante:
    def __init__(self, dni, nom, edad, sexo):
        self.dni = dni
        self.nombre = nom
        self.edad = edad
        self.sexo = sexo


def display(votante):

    if votante.sexo == "m":
        votante.sexo = "Mujer"
    else:
        votante.sexo = "Hombre"

    print("{:<20}{:<20}{:<20}{:<20}".format("|Vot.DNI|", "|Vot.Nombre|", "|Vot.Edad|", "|Vot.Sexo|"))
    print("{:<20}{:<20}{:<20}{:<20}".format(votante.dni, votante.nombre, votante.edad, votante.sexo))
    print()


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error ! valor incorrecto.")
    return n


def validar_dni(mensaje):
    print("DNI ejemplo: 11-111-111 (sin guiones)")
    dni = "1"
    while len(dni) < 8:
        dni = input(mensaje)
        if len(dni) < 8:
            print("Dato incorrecto, cargue nuevamente.")

    return dni


def validar_sexo(mensaje):
    sexo = "j"
    while sexo not in ["m", "v"]:
        sexo = input(mensaje)
        if sexo not in ["m", "v"]:
            print("Dato incorrecto, cargue nuevamente.")
    return sexo


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor incorrecto, ingrese nuevamente.")

    return n


def buscar_dni(m, dni, fd):
    t = os.path.getsize(fd)
    while m.tell() < t:
        votante = pickle.load(m)
        if votante.dni == dni:
            return -1
    return dni


def cargar_archivo(fd):
    m = open(fd, "wb")

    n = validar_positivo(0, "Ingrese la cantidad de votantes: ")
    print("Carga de datos del votante: \n")

    for i in range(n):
        dni = -1
        while dni == -1:
            dni = validar_dni("DNI: ")
            buscar_dni(m, dni, fd)
            if dni != -1:
                nombre = input("Nombre: ")
                edad = validar_rango(18, 70, "Edad: ")
                sexo = validar_sexo("Sexo (m|v): ")

                votante = Votante(dni, nombre, edad, sexo)
                pickle.dump(votante, m)

            else:
                print("El DNI", dni, "ya existe. Alta rechazada.")
                dni = validar_dni("DNI: ")


def test():
    v = []
    fd = "padron.dat"

    opc = -1
    while opc != 7:
        print("\t\t----Menu de Opciones----\n")
        print("1. Cargar datos en el archivo.")
        print("2. Mostrar los datos del archivo.")
        print("3. Buscar votante por DNI.")
        print("4. Cantidad de varones y mujeres votantes.")
        print("5. Generar archivo comprendido para mayores de 70.")
        print("6. Mostrar los datos del archivo comprendido.")
        print("7. Salir.")

        opc = int(input("\t\t-> Ingrese su opcion: "))

        if opc == 1:
            cargar_archivo(fd)

        elif opc == 2:
            pass

        elif opc == 3:
            pass

        elif opc == 4:
            pass

        elif opc == 5:
            pass

        elif opc == 6:
            pass

        elif opc == 7:
            print("Programa terminado.")

        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    test()
