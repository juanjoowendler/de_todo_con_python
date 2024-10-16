# Agenda
# Se solicita un programa que permita agendar contactos
# en un archivo. De cada contacto se debe ingresar
# su nombre y apellido, mail y teléfono.

# Se pide:

# Cargar el archivo por teclado.
# Mostrar el archivo.
# Generar a partir del archivo un vector con todos los contactos.

import random
import pickle
import os.path


class Contacto:
    def __init__(self, nom, app, mail, tel):
        self.nombre = nom
        self.apellido = app
        self.mail = mail
        self.telefono = tel


def to_string(contacto):
    cad = ""
    cad += "{:>8}{:<15}".format("Nom: ", contacto.nombre)
    cad += "App: {:<17}".format(contacto.apellido)
    cad += "Mail: {:<30}".format(contacto.mail)
    cad += "Tel: {}".format(contacto.telefono)

    return cad


def validar_positivo(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print(f"Error ! ingrese mayor a [{inf}].")

    return n


def cargar_archivo(fd):
    m = open(fd, "wb")

    n = validar_positivo(0, "Cantidad de contactos a agendar (mayor a cero): ")
    nombres = ("Ana", "Maria", "Carlos", "Juan", "Pepe", "Oriana", "Carolina", "Alfonso")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Armando", "Pereyra", "Perez")

    for i in range(n):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        mail = f"{nombre}{apellido[0:5]}{random.randint(0,99)}@gmail.com"
        telefono = f"{random.randint(3000, 4000)}-{random.randint(300000, 999999)}"

        contacto = Contacto(nombre, apellido, mail, telefono)

        pickle.dump(contacto, m)

    m.close()
    print(f"\nSe ha generado exitosamente el archivo {fd} con los contactos.")
    print()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta ver no existe...")
        print()
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print("\nSe muestran a continuacion los datos del archivo: ")
    while m.tell() < tam:
        contacto = pickle.load(m)
        print(to_string(contacto))

    m.close()


def cargar_arreglo(v, fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo...")
        print()
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        contacto = pickle.load(m)
        v.append(contacto)

    m.close()
    print("\nSe ha creado exitosamente el arreglo a partir del archivo.")
    print()


def principal():
    print("\tAGENDA")
    print("*"*20)

    v = []
    fd = ""

    menu = "\n---Menu de opciones---\n" \
           "1) Cargar el archivo.\n" \
           "2) Mostrar el archivo.\n" \
           "3) Generar arreglo.\n" \
           "0) Salir del programa.\n"

    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("\nIngrese su opcion: "))

        if opc == 1:
            fd = input("Ingrese el nombre del archivo (sin extension): ")
            fd = f"{fd}.dat"
            cargar_archivo(fd)
        elif opc == 2:
            mostrar_archivo(fd)
        elif opc == 3:
            cargar_arreglo(v, fd)
        elif opc == 0:
            print("\nPorgrama terminado.")
            print()
        else:
            print("\nError ! Opcion incorrecta.")
            print()



if __name__ == "__main__":
    principal()
