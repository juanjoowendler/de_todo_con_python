"""
Se solicita un programa que permita agendar contactos en un archivo. De cada contacto
se debe ingresar su nombre y apellido, mail y teléfono.

Se pide:

Cargar el archivo por teclado.
Mostrar el archivo.
Generar a partir del archivo un vector con todos los contactos.
"""

__author__ = "Wendler Juan Jose"

import random
import pickle
import os.path


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print("Error ! ingrese mayor a ", inf)
    return n


class Contacto:
    def __init__(self, nombre, apellido, mail, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono


def cargar_archivo(cantidad, fd):
    nombres = ("Maria", "Ana", "Juanjo", "Sebastian", "Thomas", "Pedro", "Carlos", "Cecilia", "Carolina", "Agostina",
               "Oriana", "Alvaro", "Joaquin", "Lucas", "Juan", "Karina", "Marta", "Gian", "Julian", "Diana", "Manuel")

    apellidos = ("Kassis", "Wendler", "Maceira", "Lambrusqui", "Gonzales", "Sanchez", "Puy", "Rivarola", "Di-Maria")

    terminaciones = ("@gmail.com.ar", "@yahoo.com.ar", "@email.com.ar", "@exodus.com.ar")

    m = open(fd, "wb")
    for i in range(cantidad):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        mail = nombre.lower() + str(random.randint(0, 90)) + apellido.lower() + random.choice(terminaciones)
        telefono = str(random.randint(3000, 3500)) + "-" + str(random.randint(100000, 900000))

        contacto = Contacto(nombre, apellido, mail, telefono)
        pickle.dump(contacto, m)

    print("\nSe almacenaron exitosamente los datos en el archivo", fd + ".")

    m.close()


def to_string(c):
    r = ""
    r += "{} {:<15}".format("Nom:  ", c.nombre)
    r += "{} {:<17}".format("App:  ", c.apellido)
    r += "{} {:<45}".format("Mail: ", c.mail)
    r += "{}       ".format("Tel:  " + str(c.telefono))

    return r


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No hay datos en el archivo.", end="\n\n")
        return

    m = open(fd, "rb")
    tb = os.path.getsize(fd)

    while m.tell() < tb:
        contacto = pickle.load(m)
        print(to_string(contacto))

    m.close()


def generar_vector(v, fd):
    if not os.path.exists(fd):
        print("No hay datos en el archivo.", end="\n\n")
        return

    m = open(fd, "rb")
    tb = os.path.getsize(fd)
    while m.tell() < tb:
        contacto = pickle.load(m)
        v.append(contacto)

    print("\nLos datos del archivo", fd, "se cargaron exitosamente en el vector.")

    m.close()


def test():
    fd = ""
    v = []

    opc = -1
    while opc != 4:
        print("\n\t\t----Menu de Opciones----")
        print("1.-Cargar los datos del archivo completo.")
        print("2.-Mostrar los datos del archivo completo.")
        print("3.-Generar un vector con los datos del archivo.")
        print("4.-Salir del programa.", end="\n\n")
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            fd = input("Ingrese el nombre del archivo - (sin extension): ")
            fd += ".dat"

            cantidad = validar_positivo(0, "Cantidad de contactos a almacenar: ")
            cargar_archivo(cantidad, fd)

        elif opc == 2:
            mostrar_archivo(fd)

        elif opc == 3:
            generar_vector(v, fd)

        elif opc == 4:
            print("Programa terminado.")
        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    test()
