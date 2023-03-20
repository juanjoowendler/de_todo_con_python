from modulo_validaciones import *
import random
from modulo_registro import *
import pickle
import os.path

def add_in_order(prof, v):
    n = len(v)
    pos = n

    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].dni == prof.dni:
            pos = c
            break

        if prof.dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [prof]


def cargar_arreglo(n, v):
    nombres = ("Juanjo", "Pepe", "Juancruz", "Flavia", "Jorge", "Hernan",
               "Carolina", "Florencia", "Ana", "Marta", "Fernanda", "Luz")

    apellidos = ("Wendler", "Paredes", "Lambrusqui", "Maceira", "Steldon",
                 "Nuñez", "Maria", "Soria", "Galarza", "Perez", "Kassis")

    for i in range(n):
        dni = random.randint(40000000, 90000000)
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        importe = round(random.uniform(15000, 50000), 2)
        afiliacion = random.randint(0, 4)
        tipo_trabajo = random.randint(0, 14)

        prof = Profesional(dni, nombre, importe, afiliacion, tipo_trabajo)
        add_in_order(prof, v)

    print("\n Se han generado los registros de profesionales de forma ordenada.")


def mostrar_arreglo(v):
    print("-----Datos de los Profesionales-----\n")
    for profesional in v:
        print(to_string(profesional))


def buscar_dni(dni, v):
    n = len(v)
    pos = n

    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if dni == v[c].dni:
            pos = c
            return pos

        if dni < v[c].dni:
            der = c-1
        else:
            izq = c+1

    return -1


def crear_archivo(fd, v):
    importe_x = float(validar_positivo(0, "Ingrese importe a comparar: $ "))

    m = open(fd, "wb")

    for profesional in v:
        if (profesional.tipo_trabajo in [3, 4, 5]) and (profesional.importe > importe_x):
            pickle.dump(profesional, m)

    m.close()
    print(f"\n Se han cargado exitosamente los registros comprendidos en el archivo {fd}"
          f" y con un importe mayor a $ {importe_x}.")
    print()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe, debe crearlo primero.")
        print()
        return

    m = open(fd, "rb")

    t = os.path.getsize(fd)

    while m.tell() < t:
        profesional = pickle.load(m)
        print(to_string(profesional))

    m.close()


def buscar_por_nombre(v, nombre):
    for i in range(len(v)):
        if v[i].nombre == nombre:
            return i

    return -1


def mostrar_matriz(matriz):
    filas, columnas = len(matriz), len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] > 0:
                print(f"{convertir_datos(f, tipo=True)} - {convertir_datos(c, tipo=False)} - "
                      f"Total: {matriz[f][c]}")


def afiliaciones_por_trabajo(v):
    matriz = [[0] * 15 for i in range(5)]

    for profesional in v:
        f = profesional.afiliacion
        c = profesional.tipo_trabajo
        matriz[f][c] += 1

    mostrar_matriz(matriz)


def test():
    paso_primero = False
    error = "\nPrimero debe cargar el vector en el punto 1)."
    menu = ("\n===MENU DE OPCIONES===\n"
            "1). Cargar arreglo.\n"
            "2). Mostrar arreglo.\n"
            "3). Buscar por DNI.\n"
            "4). Crear un archivo.\n"
            "5). Mostrar archivo.\n"
            "6). Buscar por nombre.\n"
            "7). Cantidad de afiliaciones por trabajo.\n"
            "0). Salir del programa\n\n")

    v = []
    fd = ""

    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("\t->Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            n = validar_positivo(0, "Ingrese cantidad de profesionales: ")
            cargar_arreglo(n, v)
        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)
        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                dni = validar_dni(40000000, 90000000, "Ingrese DNI - [40000000-90000000]: ")
                indice = buscar_dni(dni, v)
                print(f"\n Buscando {dni} en el vector...")

                if indice != -1:
                    print("Datos del profesional encontrado: \n")

                    print(to_string(v[indice]))

                    nuevo_importe = float(validar_positivo(0, "Ingrese nuevo importe: $ "))

                    if nuevo_importe > v[indice].importe:
                        print(f"ATENCION ! El importe de {v[indice].nombre} esta desactualizado - "
                              f"su importe: {v[indice].importe} $.\n")

                else:
                    print(f"\nNo se encontro el DNI: {dni} en el vector.")

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                fd = input("Ingrese el nombre del archivo: ")
                fd += ".dat"
                crear_archivo(fd, v)
        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo(fd)
        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                nombre = input("Ingrese nombre a buscar: ")
                resultado = buscar_por_nombre(v, nombre)

                if resultado != -1:
                    print(f"Encontrado ! se muestran a continuacion los datos de {v[resultado].nombre}: \n")
                    print(to_string(v[resultado]))

                else:
                    print(f"No se ha encontrado a {nombre} en el vector.")

        elif opc == 7:
            if not paso_primero:
                print(error)
            else:
                afiliaciones_por_trabajo(v)
        elif opc == 0:
            print("Programa terminado.")
        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    test()
