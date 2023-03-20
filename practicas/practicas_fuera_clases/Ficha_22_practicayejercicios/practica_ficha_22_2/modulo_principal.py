from modulo_validaciones import *
import random
from modulo_registro import *
import os.path
import pickle


def add_in_order(alumno, v):
    n = len(v)
    pos = n

    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2

        if alumno.nombre == v[c].nombre:
            pos = c
            break

        if alumno.nombre < v[c].nombre:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [alumno]


def cargar_arreglo(v, n):
    nombres = ("Juanjo", "Pepe", "Juancruz", "Flavia", "Jorge", "Hernan",
               "Carolina", "Florencia", "Ana", "Marta", "Fernanda", "Luz")

    apellidos = ("Wendler", "Paredes", "Lambrusqui", "Maceira", "Steldon",
                 "Nuñez", "Maria", "Soria", "Galarza", "Perez", "Kassis")

    for i in range(n):
        legajo = random.randint(20000, 90000)
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        anio = random.randint(1, 7)
        deporte = random.randint(0, 9)

        alumno = Alumno(legajo, nombre, anio, deporte)
        add_in_order(alumno, v)

    print("\nSe ha generado exitosamente el vector con los registros de los alumnos.")


def mostrar_arreglo(v):
    print("\n ----Los datos de los alumnos se muestran a continuacion----")
    for alumno in v:
        print(to_string(alumno))


def buscar_legajo_deporte(v, deporte, legajo):
    indice = -1

    for i in range(len(v)):
        if (deporte == v[i].deporte) and (legajo == v[i].legajo):
            return i

    return indice


def crear_matriz_conteo(v):
    matriz = [[0] * 10 for i in range(7)]
    # columnas = 10
    # filas = 7

    for alumno in v:
        f = alumno.anio                  # va de[1-7] en f recibe un 1 o un 7 o un 6 y asi (nunca 0)
        c = alumno.deporte               # va de [0-9]

        matriz[f-1][c] += 1

    return matriz


def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] != 0:
                print(f"{f+1}° Año - {convertir_datos(c)} - Total: {matriz[f][c]}")
                # le sumo al año restado para mostrar el correcto


def generar_archivo(fd, v):
    m = open(fd, "wb")

    for alumno in v:
        pickle.dump(alumno, m)

    m.close()

    print(f"\nSe ha generado el archivo '{fd}' con todos los registros"
          f" exitosamente.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe ningun archivo, cargue uno en el punto 5).")
        print()
        return

    alguno = 0
    m = open(fd, "rb")
    t = os.path.getsize(fd)

    while m.tell() < t:
        alumno = pickle.load(m)
        if alumno.anio == 7:
            alguno = 1
            print(to_string(alumno))

    m.close()

    if alguno == 0:
        print("\nNo hay ningun registro con alumnos del 7°  Año.")
        print()


def test():
    paso_primero = False
    v = []
    fd = ""

    error = "Error ! primero debe cargar los datos en el punto 1)."

    menu = ("\n===MENU DE OPCIONES===\n"
            "1). Cargar vector.\n"
            "2). Mostrar vector.\n"
            "3). Buscar por legajo y deporte.\n"
            "4). Alumnos por deporte y año.\n"
            "5). Generar archivo.\n"
            "6). Mostrar archivo.\n"
            "0). Salir del programa.\n\n")

    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            n = validar_positivo(0, "Ingrese cantidad de estudiantes: ")
            cargar_arreglo(v, n)
        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)
        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                legajo = validar_rango(20000, 90000, "Ingrese legajo a buscar - [20000-90000]: ")
                deporte = validar_rango(0, 9, "Ingrese deporte [0-9]: ")
                indice = buscar_legajo_deporte(v, deporte, legajo)

                if indice != -1:
                    print(f"\nSe encontro al alumno {v[indice].nombre} en el vector, sus datos: ")
                    print(to_string(v[indice]))
                else:
                    print("No se ha encontrado al alumno con los siguientes datos:")
                    print(f"Deporte: {deporte} - Legajo: {legajo}, procederemos a agregarlo...")

                    nombre = input("Nombre y apellido: ")
                    anio = validar_rango(1, 7, "Ingrese su año: ")

                    alumno = Alumno(legajo, nombre, anio, deporte)
                    add_in_order(alumno, v)

                    print("\nSe ha generado un registro con el nuevo alumno faltante: ")
                    print(to_string(alumno))

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz_conteo(v)
                print()
                mostrar_matriz(matriz)
        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                primero = True
                while os.path.exists(fd) or primero:
                    primero = False
                    fd = input("Ingrese el nombre del archivo: ")
                    fd += ".dat"
                    if os.path.exists(fd):
                        print(f"El archivo {fd} ya existe, cambie el nombre.")

                print("\nNombre correcto...")

                generar_archivo(fd, v)

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo(fd)

        elif opc == 0:
            print("Programa terminado.")
        else:
            print("Error ! valor incorrecto.")


if __name__ == "__main__":
    test()
