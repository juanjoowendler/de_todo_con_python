__author__ = "Wendler Juan Jose"

"""
Un consultorio médico necesita un programa para gestionar los datos de sus
pacientes. Por cada paciente, se deben almacenar los siguientes elementos: número de
historia clínica (un número entero), nombre del paciente, fecha de la última visita (en días –
otro número entero) y código de la enfermedad o problema registrado (un valor entre 0 y 9
incluidos). Los datos deben cargarse y almacenarse inicialmente en un arreglo de registros, a
razón de un registro por paciente, el cual debe mantenerse en todo momento ordenado de
menor a mayor de acuerdo al valor del número de historia clínica de los pacientes. El
programa debe incluir un menú con las opciones siguientes

1. Cargar el arreglo con los registros pedidos (recuerde: el arreglo debe mantenerse
ordenado por historia clínica: cada registro debe insertarse en el lugar correcto
cuando se agrega al arreglo).

2. Cargar por teclado un número entero d, y mostrar por pantalla los datos de todos los
pacientes del arreglo que hayan asistido al consultorio por última vez en un período
de d días o más.

3. Determinar si en el arreglo existe un paciente con número de historia clínica igual a x.
Si existe, mostrar todos sus datos. Si no, dar un mensaje de error.

4. Mostrar todos los datos del arreglo.

5. Grabe todos los datos del arreglo en un archivo (para favorecer el desarrollo de los
puntos que siguen, asegúrese de hacerlo de forma que cada registro se grabe por
separado, uno por uno). El archivo debe ser creado si no existía, y todo dato que
hubiese contenido debe ser eliminado si ya existía.

6. Mostrar el archivo generado en el punto anterior.

7. Usando el archivo creado en el punto 5, crear en memoria otro arreglo que contenga
los registros de los pacientes cuyo código de enfermedad sea 8 o 9. Recuerde: debe
crear otro arreglo de registros, y no eliminar ni modificar el original que se creó en el
punto 1.

8. Mostrar el arreglo creado en el punto 7.

"""
import random
import pickle
import os.path


class Paciente:
    def __init__(self, num_h, nom, fecha, prob):
        self.numero_historia = num_h
        self.nombre = nom
        self.fecha = fecha
        self.problema = prob


def display(v):
    print("{:<20}{:<20}{:<20}{:<20}".format("|Num.Historial|", "|Nom.Paciente|", "|Ult.Fecha|", "|Prob.Paciente|"))
    print("{:<20}{:<20}{:<20}{:<20}".format(v.numero_historia, v.nombre, "Hace " + str(v.fecha), "Tipo " + str(v.problema)))
    print()


def cargar_arreglo(v):
    n = int(input("Ingresar la cantidad de pacientes a cargar: "))

    for i in range(n):
        numero_historia = i
        nombre = "pac." + str(i)
        fecha = random.randint(1, 99)
        problema = random.randint(0, 9)

        paciente = Paciente(numero_historia, nombre, fecha, problema)
        v.append(paciente)

    print("Se ha generado el arreglo con los registros de los pacientes.")
    print()


def validar_rango(inf, sup, mensaje):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input(mensaje))
        if n < inf or n > sup:
            print("Valor incorrecto, ingrese nuevamente.")
    print("\nBuscando...")
    return n


def mostrar_dentro_periodo(v):
    if len(v) == 0:
        print("No hay datos en el arreglo.")
        print()
        return

    d = validar_rango(1, 99, "Ingresar dia a comparar (almacenamos datos desde 1-99 dias)")
    for paciente in v:
        if paciente.fecha < d:
            display(paciente)


def buscar_paciente(v, n):
    indice = -1
    for paciente in v:
        if paciente.numero_historia == n:
            return paciente
    return indice


def mostrar_paciente_x(v):
    if len(v) == 0:
        print("No hay datos en el arreglo.")
        print()
        return

    n = validar_rango(1, len(v), "Ingresar numero de historia clinica a buscar, entre (1" + "-" + str(len(v)) + ")")

    resultado = buscar_paciente(v, n)
    if resultado != -1:
        print("Del paciente con Nro.Historial", n, "se encontro: ")
        display(resultado)
    else:
        print("No se encontro registro con Nro.Historial", n)


def mostrar_todo_arreglo(v):
    if len(v) == 0:
        print("No hay datos en el arreglo.")
        print()
        return

    for paciente in v:
        display(paciente)


def cargar_archivo(v, fd):
    if len(v) == 0:
        print("No hay datos en el arreglo.")
        print()
        return

    m = open(fd, "wb")

    for paciente in v:
        pickle.dump(paciente, m)

    m.close()

    print("Se creo el archivo", fd, "con los registros de los pacientes.")


def mostrar_datos_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo de registros", fd, "que intenta mostrar no existe.")
        print()
        return

    m = open(fd, "rb")

    t = os.path.getsize(fd)
    while m.tell() < t:
        paciente = pickle.load(m)
        display(paciente)

    m.close()


def cargar_otro_arreglo(fd):
    if not os.path.exists(fd):
        print("El archivo que intenta cargar no existe.")
        print()
        return

    v2 = []

    m = open(fd, "rb")
    t = os.path.getsize(fd)

    while m.tell() < t:
        paciente = pickle.load(m)
        if paciente.problema in [8, 9]:
            v2.append(paciente)

    m.close()

    print("Se ha creado un arreglo con los pacientes comprendidos por codigo de enfermedad dentro del archivo.")
    print()

    return v2


def mostrar_otro_arreglo(v2):
    if len(v2) == 0:
        print("No hay datos en el arreglo comprendido.")
        print()
        return

    print("Los datos de los pacientes con codigo de enfermedad 8-9 son: ")
    for paciente in v2:
        display(paciente)


def test():
    v = []
    v2 = []
    fd = "datos_consultorio.dat"

    opc = -1
    while opc != 9:
        print("\t\t----Menu de Opciones----\n")
        print("1. Cargar arreglo con los registros.")
        print("2. Cargar y mostrar pacientes dentro de un periodo 'd'.")
        print("3. Buscar paciente por numero de historial clinico 'x'.")
        print("4. Mostrar todos los datos del arreglo.")
        print("5. Grabar todos los datos del arreglo dentro de un archivo.")
        print("6. Mostrar el contenido del archivo generado en el punto 5.")
        print("7. Nuevo arreglo de pacientes con codigo de enfermedad comprendido.")
        print("8. Mostrar arreglo creado en el punto 7.")
        print("9. Salir ")

        opc = int(input("\t\t-> Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)

        elif opc == 2:
            mostrar_dentro_periodo(v)

        elif opc == 3:
            mostrar_paciente_x(v)

        elif opc == 4:
            mostrar_todo_arreglo(v)

        elif opc == 5:
            cargar_archivo(v, fd)

        elif opc == 6:
            mostrar_datos_archivo(fd)

        elif opc == 7:
            v2 = cargar_otro_arreglo(fd)

        elif opc == 8:
            mostrar_otro_arreglo(v2)

        elif opc == 9:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    test()
