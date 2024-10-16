from modulo_registro import *
from modulo_validaciones import *
import random as rd
import pickle
import os.path


def add_in_order(pelicula, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if pelicula.titulo == v[c].titulo:
            pos = c
            break

        if pelicula.titulo < v[c].titulo:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [pelicula]


def cargar_arreglo(v):
    titulos = ("Spider-Man", "The Amazing Spider-Man", "Batman Arkam night", "Avengers",
               "Vikings valhalla", "Los minions", "Halo reach", "Cars", "Sin limites",
               "Rapidos y furiosos", "Tres chiflados", "Marte", "Interestellar", "The Moon",
               "Avengers-End Game", "Iron-Man", "Duro de matar 3", "Alquimia 2", "Alquimia 3")
    cantidad, suma_costos = 0, 0

    n = validar_positivo(0, "Ingrese la cantidad de peliculas: ")
    for i in range(n):
        identificacion = rd.randint(100, 999)
        titulo = rd.choice(titulos)
        tip_pelicula = rd.randint(1, 20)
        calificacion = rd.randint(0, 5)
        costo = rd.uniform(10000, 999999)

        pelicula = Pelicula(identificacion, titulo, tip_pelicula, calificacion, costo)
        cantidad += 1
        suma_costos += pelicula.costo
        add_in_order(pelicula, v)

    print("\nSe ha creado exitosamente el arreglo de registros ordenado por titulo.")
    prom = promedio(suma_costos, cantidad)
    return prom


def promedio(suma, total):
    prom = 0
    if total > 0:
        prom = round((suma/total), 2)

    return prom


def mostrar_arreglo(v):
    costo_x = validar_rango(10000, 999999, "Costo de la pelicula $(10k-99k): ", ban=False)
    tipo_x = validar_rango(1, 20, "Tipo de pelicula (1-20): ")

    print(f"\nPeliculas con costo superiores a $ {costo_x} y del tipo {tipo_x}: ", end="\n\n")
    for pelicula in v:
        if pelicula.costo > costo_x and pelicula.tip_pelicula == tipo_x:
            print(to_string(pelicula))


def crear_matriz(v):
    matriz = [[0] * 20 for f in range(6)]
    for pelicula in v:
        fila = pelicula.calificacion
        columna = pelicula.tip_pelicula-1
        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    tipo_x = validar_rango(1, 20, "Tipo de pelicula (1-20): ")
    print("\nContenido de la matriz: ")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0 and (c+1) > tipo_x:
                print(f"Tip.Pelicula: {c+1} - Calificacion: {f} - "
                      f"Cantidad total: {matriz[f][c]}")


def generar_archivo(fd, v, prom):
    m = open(fd, "wb")
    for pelicula in v:
        if pelicula.costo < prom:
            pickle.dump(pelicula, m)

    m.close()

    print(f"\nSe ha generado el archivo {fd} con costes menores al promedio - ${prom}.", end="\n\n")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta visualizar no existe...", end="\n\n")
        return

    x = validar_rango(1, 20, "Tipo de pelicula de la que quiere saber la cantidad (1-20): ")
    cantidad_x = 0
    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        pelicula = pickle.load(m)
        print(to_string(pelicula))
        if pelicula.tip_pelicula == x:
            cantidad_x += 1

    m.close()
    print(f"\nSe encontraron '{cantidad_x}' de peliculas del tipo '{x}'.", end="\n\n")


def is_digit(car):
    if "0" <= car <= "9":
        return True
    return False


def analizar_cadena(texto):
    cant_let_pal, cant_pal_buscadas = 0, 0
    tiene_digito, tiene_ae = False, False
    for car in texto:
        if car == " " or car == ".":
            if tiene_digito and tiene_ae:
                cant_pal_buscadas += 1

            cant_let_pal = 0
            tiene_digito, tiene_ae = False, False
        else:
            cant_let_pal += 1
            if cant_let_pal == 2 and is_digit(car):
                tiene_digito = True

            if car.lower() in "ae":
                tiene_ae = True

    print(f"\n{cant_pal_buscadas} es la cantidad de palabras buscadas.", end="\n\n")


def main():
    menu = "\t\t\n==Estudio cinematografico==\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Crear y mostrar matriz.\n" \
           "4). Crear archivo.\n" \
           "5). Mostrar archivo.\n" \
           "6). Analizar cadena.\n" \
           "0). Salir del programa.\n"

    prom = 0
    error = "Error ! primero debe crear el arreglo en el Pto 1)."
    paso_primero = False
    fd = "peliculas.dat"
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            prom = cargar_arreglo(v)
            paso_primero = True

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                generar_archivo(fd, v, prom)

        elif opc == 5:
            mostrar_archivo(fd)

        elif opc == 6:
            texto = ""
            while len(texto) == 0:
                texto = input("Ingrese el texto a procesar: ")

            analizar_cadena(texto)

        elif opc == 0:
            print("\nPrograma terminado.")

        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    main()
