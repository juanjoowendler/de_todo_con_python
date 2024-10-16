import modulo_validaciones
import modulo_registro
import random
import pickle
import os.path


def add_in_order(proyecto, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if proyecto.identificacion == v[c].identificacion:
            pos = c
            break

        if proyecto.identificacion < v[c].identificacion:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [proyecto]


def cargar_arreglo(v):
    nombres = ("Ciudad futurista", "Medicina del futuro", "IA Del mañana", "Nano-tecnologia",
               "Curar todas las heridas", "Control social", "Nuevo avance", "Nuevas ciencias")
    descripciones = ("Nuevas viviendas sin deforestar.", "Medicina que cura todo mal.",
                     "IA en los nuevos empleos.", "Usos de la nano-tecnologia en la sociedad.",
                     "Uso del marketing para el control.", "Ciudad autosuficiente en Marte.",
                     "El metodo c1entiafico c0uomo.", "Automovil x4solsticio.", "Saturno para aerosol98.")

    n = modulo_validaciones.validar_positivo(0, "Ingrese la cantidad de proyectos: ")
    for i in range(n):
        identificacion = random.randint(100, 999)
        nombre = random.choice(nombres)
        descripcion = random.choice(descripciones)
        monto = random.uniform(10000, 999999)
        area_aplicacion = random.randint(1, 39)
        tip_proyecto = random.randint(0, 9)

        proyecto = modulo_registro.Proyecto(identificacion, nombre, descripcion, monto, area_aplicacion, tip_proyecto)
        add_in_order(proyecto, v)

    print(f"\nSe crearon {n} proyectos exitosamente en el arreglo.")


def mostrar_arreglo(v):
    print("\nContenido completo del arreglo: ")
    for proyecto in v:
        print(modulo_registro.to_string(proyecto))


def crear_archivo(fd, v):
    archivo = open(fd, "wb")
    for proyecto in v:
        if proyecto.tip_proyecto not in [0, 1]:
            pickle.dump(proyecto, archivo)

    archivo.close()

    print(f"Archivo '{fd}' comprendido, creado exitosamente.")


def promedio(suma, total):
    prom = 0
    if total > 0:
        prom = round((suma / total), 2)

    return prom


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nError ! el archivo que intenta visualizar no existe.", end="\n\n")
        return

    print(f"\nContenido completo del archivo '{fd}': ")
    suma, cant = 0, 0
    archivo = open(fd, "rb")
    tam = os.path.getsize(fd)
    while archivo.tell() < tam:
        proyecto = pickle.load(archivo)
        suma += proyecto.monto
        cant += 1
        print(modulo_registro.to_string(proyecto))

    archivo.close()

    prom = promedio(suma, cant)
    print(f"\nEl monto promedio de los registros mostrados es de: $ {prom}")


def buscar_por_nombre(v):
    nom = modulo_validaciones.validar_cadena(0, "Ingrese el nombre a buscar: ")

    for proyecto in v:
        if proyecto.nombre == nom:
            return proyecto

    return -1


def crear_matriz(v):
    matriz = [[0] * 39 for f in range(10)]
    for proyecto in v:
        fila = proyecto.tip_proyecto
        columna = proyecto.area_aplicacion - 1

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nContenido de la matriz: ")

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("{}{:<10}{}{:<10}{}{}".format("Tip.Proyecto: ", f,
                                                    "A.Aplicacion: ", c + 1,
                                                    "Cantidad total: ", matriz[f][c]))


def es_digit(cad):
    if "0" <= cad <= "9":
        return True
    return False


def analizar_cadena(texto):
    vocales, anterior = "aeiou", ""
    cant_pal_buscadas = 0
    digito, seguidas = False, False

    for car in texto:
        if car == " " or car == ".":
            if digito and seguidas:
                cant_pal_buscadas += 1

            digito, seguidas = False, False
        else:
            if es_digit(car):
                digito = True

            if car in vocales and anterior in vocales:
                seguidas = True

            anterior = car

    print(f"\n{cant_pal_buscadas} es la cantidad de palabras que cumplen la condicion.")


def main():
    menu = "\t\t\n==Centro de investigacion==\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Generar archivo.\n" \
           "4). Mostrar archivo.\n" \
           "5). Buscar por nombre.\n" \
           "6). Crear y mostrar matriz.\n" \
           "7). Analizar cadena.\n" \
           "0). Salir del programa.\n"

    fd = "proyectos.dat"
    error = format("Error ! {}.")
    paso_primero, tiene_cad = False, False
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)
            paso_primero = True
        elif opc == 2:
            if not paso_primero:
                print(error.format("primero cree el arreglo"))
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error.format("imposible crear archivo sin el arreglo"))
            else:
                crear_archivo(fd, v)

        elif opc == 4:
            mostrar_archivo(fd)

        elif opc == 5:
            if not paso_primero:
                print(error.format("imposible buscar sin el arreglo"))
            else:
                res = buscar_por_nombre(v)
                if res != -1:
                    print("\nEncontrado ! sus datos: ")
                    print(modulo_registro.to_string(res))
                    cadena = res.descripcion
                    tiene_cad = True
                else:
                    print("\nLo sentimos... no existe el nombre buscado.")

        elif opc == 6:
            if not paso_primero:
                print(error.format("imposible crear matriz sin arreglo"))
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 7:
            if not tiene_cad:
                print(error.format("primero debe buscar y encontrar un nombre"))
            else:
                analizar_cadena(cadena)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
