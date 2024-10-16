from modulo_validaciones import *
from modulo_registro import *
import os.path
import pickle


# Menú principal.


def menu():
    global point
    point = yellow + "➣" + reset
    print("\n  〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓"
          , yellow + "\n\t              📖 BIBIOTECA VIRTUAL 📖\n" + reset,
          " 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓\n\n"
          , point + " 1  ◦•◦•◦•◦•◦•◦•◦   Cargar el contenido del archivo.\n"
          , point + " 2  ◦•◦•◦•◦•◦•◦•◦   Buscar y sumar revisión.\n"
          , point + " 3  ◦•◦•◦•◦•◦•◦•◦   Buscar el libro con mayor cantidad de revisiones.\n"
          , point + " 4  ◦•◦•◦•◦•◦•◦•◦   Generar una matriz (Popularidad 2000).\n"
          , point + " 5  ◦•◦•◦•◦•◦•◦•◦   Publicaciones por década.\n"
          , point + " 6  ◦•◦•◦•◦•◦•◦•◦   Guardar populares en archivo binario.\n"
          , point + " 7  ◦•◦•◦•◦•◦•◦•◦   Mostrar archivo.\n"
          , point + " 8  ◦•◦•◦•◦•◦•◦•◦ ", red + " Salir." + reset + "\n"
          "\n  〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓")

    opc = int(input("{:>53}".format(yellow + ">>> [Ingrese su opcion] <<< " + reset)))

    return opc


# Agrega los registros de forma ordenada en el vector.


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


# Recolecta datos de los libros y genera un vector de registros.


def cargar_vector(v):
    primera_linea = True
    m = open("libros.csv", mode="rt", encoding="utf8")
    for linea in m:
        if primera_linea:
            primera_linea = False
            continue

        # Nos devuelve un vector con cada elemento que está separado por un coma.

        cadena = linea.split(',')
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


# Busca por código ISBN de forma binaria.


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


# Busca pot título de forma secuencial.


def busqueda_titulo(libros, titulo):
    pos = -1
    for i in range(len(libros)):
        if libros[i].titulo == titulo:
            pos = i
            break

    return pos


# Redirecciona el tipo de búsqueda y muestra sus datos (si es que lo encuentra).


def redireccionar(v):
    if len(v) == 0:
        print(yellow + "\n[❗] No hay datos cargados...(ejecute la opcion 1 para cargarlos)" + reset, end="\n")

        return
    else:
        eleccion = ""
        while eleccion not in ["T", "I", "TITULO", "ISBN"]:

            t, i = yellow + "T" + reset, yellow + "I" + reset

            eleccion = input(f"\nIngrese tipo de busqueda - ([{t}]: Titulo | [{i}]: ISBN): ").upper()

            if eleccion not in ["T", "I", "TITULO", "ISBN"]:
                print(yellow + "\nPor favor, vuelva a ingresar de forma correcta..." + reset)
                print()

        if eleccion == "T" or eleccion == "TITULO":

            tit = validar_titulo("\nIngrese el titulo del libro a buscar: ")
            pos = busqueda_titulo(v, tit)

            if pos != -1:
                print("\n{:^100}".format("Buscando..."))
                print(cyan + f"\n✪ Se ha encontrado: {v[pos].titulo}" + reset)

                v[pos].cantidad_revision += 1
                print("\n✪ Se ha actualizado su revision a: +1, la mostrarmos a continuacion...")
                print(to_string(v[pos]), end="\n")

            else:
                print(cyan + f"\n❌ No se ha encontrado el titulo {tit}..." + reset)

        else:
            codigo_a_buscar = validar_isbn("\nIngrese el codigo ISBN a buscar: ")
            pos = buscar_por_codigo(v, codigo_a_buscar)

            if pos != -1:
                print(f"\n✪ Se ha encontrado: {cyan + v[pos].titulo + reset} con el codigo " + yellow + "➣ " + reset +
                      f"{cyan + str(codigo_a_buscar) + reset}: ")

                v[pos].cantidad_revision += 1
                print("\n✪ Se ha actualizado su revision a: " + yellow + "+1" + reset)
                print(to_string(v[pos]))
                print()

            else:
                print(cyan + f"\n❌ No se ha encontrado el codigo {codigo_a_buscar}..." + reset)
                print()


# Acumula los ratings, clasificandolos segun su idioma para luego sacar el promedio.


def acumularor_ratings(v):
    if len(v) == 0:
        print(yellow + "\n[❗] No hay datos cargados...(ejecute la opcion 1 para cargarlos)" + reset, end="\n")

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


# Valida el rating.


def rating_validar(v, pos, prom):
    cadena = "\nEl rating del libro con mayor cantidad de revisiones es "

    if pos != -1:
        print("\nEl libro con mayor cantidad de revisiones es: ")
        print(to_string(v[pos]))
        print(red + "-" * 170 + "\n" + reset)
        print("{:^110}".format(f"Rating promedio del idioma {v[pos].codigo_idioma}: {magenta + str(prom) + reset}"))

        if v[pos].rating < prom:
            print(cadena + cyan + "menor (<)" + reset + " al rating promedio de su mismo idioma. ")

        elif v[pos].rating > prom:
            print(cadena + cyan + "mayor (>)" + reset + " al rating promedio de su mismo idioma. ")
        else:
            print(cadena + cyan + "igual (=)" + reset + " al rating promedio de su mismo idioma. ")


# Calcula el promedio.


def promedio(suma, cantidad):
    if cantidad != 0:
        total = suma / cantidad
    else:
        total = 0

    return total


# Genera una matriz con los libros más populares de cada idioma en cada año.


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


# Muestra la matriz, recorriendo por filas y descartando valores iguales a 0.


def mostrar_matriz(mat):
    if mat == -1:
        print(yellow + "\n[❗] No hay datos cargados...(ejecute la opcion 1 para cargarlos)" + reset, end="\n")
        return False
    else:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    print(to_string_2(mat[i][j]))

    return True


# Busca el libro de X década con mayor cantidad de publicaciones.


def may_publicacion(decadas):
    pos = []
    may = 0
    for i in range(len(decadas)):
        if decadas == may:
            pos.append(i)
        elif decadas[i] > may:
            may = decadas[i]
            pos = [i]

    return pos


# Contador de décadas,
# Contamos las décadas comenzando desde 0 y terminando en 9 (1900-1909, 1910-1919...).


def decada_pub(libros):
    vec = [0] * 10

    if len(libros) == 0:

        return -1

    else:
        for i in range(len(libros)):
            if 1900 <= libros[i].anio_publicacion <= 1999:
                decada = str(libros[i].anio_publicacion)
                decada = decada[:-1]
                decada = int(decada)
                vec[decada - 190] += 1

        pos_mayor = may_publicacion(vec)

    return vec, pos_mayor


# Muestra la cantidad de publicaciones por década.


def mostrar_decada(v):
    if v == -1:
        print(yellow + "\n[❗] No hay datos cargados... (ejecute la opcion '1' para cargarlos)." + reset)
    else:
        mayor_cantidad_publicaciones = 0
        print()
        for i in range(len(v)):
            if v[i] > v[mayor_cantidad_publicaciones]:
                mayor_cantidad_publicaciones = i
            if v[i] != 0:
                print("{:>8} {:<10}{:<34}".format(
                    f"{'Decada: ' + blue + '19' + str(i) + str(0) if i != 10 else reset + 'Decada:' + blue + ' 2000' + reset}",
                    reset + point + " Su cantidad de libros es: ", blue + str(v[i]) + reset))


# Muestra la década con más publicaciones.


def tranfor_in_dec(mayores):
    for i in range(len(mayores)):
        mayores[i] += 190
        mayores[i] *= 10
        print("\n\tLa década con mas publicaciones es:", yellow + str(mayores[i]) + reset)


# Genera archivo binario donde se almacenan los registros de la matriz del punto 4.


def generar_archivo(mat, gen):
    if gen:
        m = open("populares.dat", "wb")
        cantidad = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    pickle.dump(mat[i][j], m)
                    cantidad += 1

        m.close()

        print(green + "\nArchivo generado" + reset)
        print(green + "\nCantidad de registros grabados" + reset, cyan + str(cantidad) + reset)

        return True
    else:
        print(yellow + "\n[❗] Debe ejecutar la opcion 4 primero......." + reset, end="\n")
        print(red + "\nNo se ha generado el archivo binario......." + reset, end="\n")

        return False


# Muestra los registros almacenados en el archivo "populares.dat".


def mostrar_archivo():
    nom = "populares.dat"
    if not os.path.exists(nom):
        print(yellow + "\n[❗] El arhivo no existe.......(ejecute la opcion 6 para generarlo)" + reset, end="\n")

        return

    m = open(nom, "rb")
    tam = os.path.getsize(nom)

    while m.tell() < tam:
        reg = pickle.load(m)
        print(to_string(reg))

    m.close()


# Gestiona las funciones del menú.


def test():
    v = []
    opc = -1
    gen = mat = False

    while opc != 8:
        opc = menu()

        if opc == 1:
            cargar_vector(v)

            for libro in v:
                print(to_string(libro))

        elif opc == 2:
            redireccionar(v)

        elif opc == 3:

            pos, rating_idioma, cant_idioma = acumularor_ratings(v)
            prom = promedio(rating_idioma, cant_idioma)
            rating_validar(v, pos, prom)

        elif opc == 4:
            mat = popularidad_2000(v)
            gen = mostrar_matriz(mat)

        elif opc == 5:
            vec_decada, mas_dec = decada_pub(v)
            mostrar_decada(vec_decada)
            tranfor_in_dec(mas_dec)

        elif opc == 6:
            generar_archivo(mat, gen)

        elif opc == 7:
            mostrar_archivo()

        elif opc == 8:
            print(yellow + "\nPrograma terminado 🤠" + reset)
        else:
            print(red + "\n[❗] Opcion incorrecta." + reset)


if __name__ == "__main__":
    test()
