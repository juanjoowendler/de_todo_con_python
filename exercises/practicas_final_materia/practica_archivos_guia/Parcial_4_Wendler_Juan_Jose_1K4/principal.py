from validaciones import *
from registro import *
import os.path
import pickle



def menu():
    print("\n╔══════════════════════════════════════════════════╗"
          "\n                -MENU DE OPCIONES-\n"
          " ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
          "➣ 1 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Cargar el contenido del archivo.\n"
          "➣ 2 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Buscar y sumar revisión.\n"
          "➣ 3 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Buscar el libro con mayor cantidad de revisiones.\n"
          "➣ 4 ╴ ╴ ╴ ╴ ╴ ╴ ╴   generar una matriz (Popularidad 2000).\n"
          "➣ 5 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Publicaciones por década.\n"
          "➣ 6 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Guardar populares en archivo binario.\n"
          "➣ 7 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Mostrar archivo.\n"
          "➣ 8 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Salir.\n"
          "\n╚══════════════════════════════════════════════════╝")

    opc = int(input("{:>40}".format(">>> [Ingrese su opcion:] <<< ")))

    return opc


"""Cargar: Cargar el contenido del archivo en un vector de registros de libros, que siempre debe mantenerse ordenado
 por isbn (Omitir la primera línea del archivo, que contiene el nombre de los campos)
 
Sumar revisión: El usuario puede optar por buscar el libro por ISBN o por título. Según el criterio elegido se debe
 ingresar por teclado el ítem a buscar. Si existe en el vector el libro con el criterio buscado,  mostrar sus datos 
 y sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.
 
Mayor revisiones: Buscar en el vector el libro con mayor cantidad de revisiones. Informar si su rating es mayor, 
menor o igual al rating promedio de su mismo idioma.

Popularidad 2000: A partir del vector, generar una matriz donde cada fila sea un idioma y cada columna un año de 
publicación. La celda debe contener el libro que tenga mayor rating para ese idioma y año (si hubiera varios, elegir 
sólo uno) sólo para los libros publicados entre el año 2000 y el 2020 (ambos incluídos).

Publicaciones por década: A partir del vector, generar un vector de conteo donde cada celda representa una década 
entre 1900 y 2000. La celda debe indicar cuántos libros se publicaron en esa década. Mostrar todas las cantidades 
mayores a cero. Informar además cuál fue la década con más publicaciones. Si varias tuvieran la misma cantidad, informar todas.

Guardar populares: Si la matriz de la opción 4 ya fue generada, almacenar su contenido registros por registro 
(omitiendo las celdas vacías) en un archivo binario llamado populares.dat e informar la cantidad de registros grabados.
 Si la matriz aún no fue generada, informarlo.
Mostrar archivo: Listar el contenido del archivo generado en el punto anterior."""


def add_in_order(v, libro):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2

        if libro.isbn == v[c].isbn:
            pos = c
            break

        if libro.isbn < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [libro]


def cargar_vector(v):
    primera_linea = True
    m = open("libros.csv", mode="rt", encoding="utf8")
    for linea in m:
        if primera_linea:
            primera_linea = False
            continue

        cadena = linea.split(',')  # Nos devuelve un vector con cada elemento que está separado por un coma.
        titulo = cadena[0]
        cantidad_revisiones = int(cadena[1])
        anio_de_publicacion = int(cadena[2])
        cod_idioma = int(cadena[3])
        rating = float(cadena[4])
        isbn = str(cadena[5])
        isbn = isbn[:-1]
        libro = Libro(titulo, cantidad_revisiones, anio_de_publicacion, cod_idioma, rating, isbn)
        add_in_order(v, libro)

    m.close()

    return v


def buscar_por_codigo(v, codigo):
    n = len(v)
    izq, der = 0, n - 1
    indice = -1

    while izq <= der:

        c = (izq + der) // 2

        if codigo == v[c].isbn:
            indice = c
            break

        if codigo < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    return indice


def busqueda_titulo(libros, titulo):
    pos = -1
    for i in range(len(libros)):
        if libros[i].titulo == titulo:
            pos = i
            break

    return pos


def validar_titulo(mensaje):
    tit = None
    while tit is None:
        tit = input(mensaje)
        if tit is None:
            print("\nError ! ingrese un titulo.")

    return tit


def redireccionar(v):
    if len(v) == 0:
        print("\nNo hay datos cargados....(ejecute la opcion 1 para cargarlos)", end="\n")

        return
    else:
        eleccion = ""
        while eleccion not in ["T", "I", "TITULO", "ISBN"]:
            eleccion = input("\nIngrese tipo de busqueda - ([T]: Titulo | [I]: Isbn ): ").upper()

            if eleccion not in ["T", "I", "TITULO", "ISBN"]:
                print("\nPor favor, vuelva a ingresar de forma correcta...")
                print()

        if eleccion == "T" or eleccion == "TITULO":

            tit = validar_titulo("\nIngrese el titulo del libro a buscar:")
            pos = busqueda_titulo(v, tit)

            if pos != -1:
                print(f"\nSe ha encontrado: {v[pos].titulo} que coincide con el titulo ingresado por teclado")
                print(to_string(v[pos]))
                print()

                v[pos].cantidad_revision += 1
                print("Se ha actualizado su revision a: +1...")
                print(to_string(v[pos]))
                print()
            else:
                print(f"\nNo se ha encontrado el titulo {tit}...")
                print()



        else:
            codigo_a_buscar = validar_isbn("Ingrese el codigo ISBN a buscar: ")
            pos = buscar_por_codigo(v, codigo_a_buscar)

            if pos != -1:
                print(f"Se ha encontrado: {v[pos].titulo} con el codigo -> {codigo_a_buscar}: ")
                print(to_string(v[pos]))
                print()

                v[pos].cantidad_revision += 1
                print("Se ha actualizado su revision a: +1...")
                print(to_string(v[pos]))
                print()

            else:
                print(f"No se ha encontrado el codigo {codigo_a_buscar}...")
                print()


def matriz(v):
    if len(v) == 0:
        print("\nNo hay datos cargados....(ejecute la opcion 1 para cargarlos)", end="\n")

        return -1, -1, -1,

    else:
        may = v[0].cantidad_revision
        pos_mayor = 0

        mat = [[0] * 27 for i in range(2)]

        for i in range(len(v)):
            pos = v[i].codigo_idioma - 1
            mat[0][pos] += v[i].rating
            mat[1][pos] += 1

            if v[i].cantidad_revision > may:
                may = v[i].cantidad_revision
                pos_mayor = i

    return pos_mayor, mat[0][v[pos_mayor].codigo_idioma - 1], mat[1][v[pos_mayor].codigo_idioma - 1]


def rating_validar(v, pos, prom):
    if pos != -1:
        if v[pos].rating < prom:
            print("\nEl rating es menor al rating promedio de su mismo idioma. ")

        elif v[pos].rating > prom:
            print("\nEl rating es mayor al rating promedio de su mismo idioma. ")

        else:
            print("\nEl rating es igual al rating promedio de su mismo idioma. ")


def promedio(suma, cantidad):
    if cantidad != 0:
        total = suma / cantidad
    else:
        total = 0

    return total


def popularidad_2000(vector):
    if len(vector) == 0:
        return -1

    else:
        mat = [[0] * 21 for j in range(27)]
        for i in range(len(vector)):
            if 2000 <= vector[i].anio_publicacion <= 2020:
                fila = vector[i].codigo_idioma - 1
                columna = vector[i].anio_publicacion - 2000
                if mat[fila][columna] == 0:
                    mat[fila][columna] = vector[i]
                elif vector[i].rating > mat[fila][columna].rating:
                    mat[fila][columna] = vector[i]
        return mat


def mostrar_matriz(mat):
    if mat == -1:
        print("\nNo hay datos cargados....(ejecute la opcion 1 para cargarlos)", end="\n")

    else:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    print('No hay libros almacenados con este idioma (', i + 1, ') y año (', j + 2000, ')...')
                else:
                    print('Idioma:', i + 1, ' - Año:', j + 2000, ' - Libro:', to_string(mat[i][j]))



def decada_pub(libros):
    vec = [0] * 11

    if len(libros) == 0:

        return -1

    else:
        for i in range(len(libros)):
            if 1900 <= libros[i].anio_publicacion <= 2000:
                decada = str(libros[i].anio_publicacion)
                decada = decada[:-1]
                decada = int(decada)
                vec[decada - 190] += 1
        print(vec)
    return vec


def mostrar_decada(v):
    if v == -1:
        print("\nNo hay datos cargados....(ejecute la opcion 1 para cargarlos)", end="\n")
    else:
        decada_mas_publicaciones_cant = 0
        decada_mas_publicaciones = []

        for i in range(len(v)):
            if decada_mas_publicaciones_cant < v[i]:
               decada_mas_publicaciones = [i]
               decada_mas_publicaciones_cant = v[i]

            elif decada_mas_publicaciones_cant == v[i]:
                decada_mas_publicaciones.append(i)

            if v[i] > 0:
                print("{:>8} {:<10}{:<34}".format
                      (f"{cyan + 'Decada: '+reset + magenta+'19'+ str(i)+str(0) if i != 10 else cyan + 'Decada:' +magenta+ ' 2000'+reset}",
                       cyan+"| Cantidad de libros publicados: "+reset, magenta+str(v[i]) + reset))




# Informar además cuál fue la década con más publicaciones. Si varias tuvieran la misma cantidad, informar todas.

# principal
def test():
    v = []
    opc = -1
    fd = None
    ops_1 = False

    while opc != 8:
        opc = menu()

        if opc == 1:
            ops_1 = True
            cargar_vector(v)
            for libro in v:
                print(to_string(libro))


        elif opc == 2:
            redireccionar(v)

        elif opc == 3:

            pos, rating_idioma, cant_idioma = matriz(v)
            prom = promedio(rating_idioma, cant_idioma)
            rating_validar(v, pos, prom)

        elif opc == 4:
            mat = popularidad_2000(v)
            mostrar_matriz(mat)

        elif opc == 5:
            vec_decada = decada_pub(v)
            mostrar_decada(vec_decada)


        elif opc == 6:
            #populares.dat
            pass

        elif opc == 7:
            pass

        elif opc == 8:
            print("\nPrograma terminado.")
        else:
            print("\nOpcion incorrecta.")

if __name__ == "__main__":
    test()

def leer_archivo(nombre):
    if nombre is not None:
        costo_total = clientes = promedio = 0

        if os.path.exists(nombre):

            m = open(nombre, 'rb')

            tam = os.path.getsize(nombre)

            while m.tell() < tam:
                p = pickle.load(m)
                print(to_string(p))
                costo_total += p.costo
                clientes += 1

            m.close()
            if clientes != 0:
                promedio = round(costo_total / clientes, 2)
                print("\n promedio de los costos de licencia: ", promedio, end="\n")
            else:
                print("\nno se definio un promedio ya que el archivo en el punto 4 no contiene ningun valor en los"
                      " parametros que le fueron asignados")

        else:
            print('El archivo', nombre, 'no existe!.')

    else:
        print("\nprimero debe ejecutar la opcion 4")
