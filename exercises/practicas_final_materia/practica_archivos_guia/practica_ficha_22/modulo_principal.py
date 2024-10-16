import modulo_validaciones
import random
from modulo_registro import *
import pickle
import os.path


def add_in_order_binary(v, pelicula):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if v[c].codigo == pelicula.codigo:
            pos = c
            break

        if pelicula.codigo < v[c].codigo:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq
        v[pos:pos] = [pelicula]


def cargar_vector(v, n):

    titulos = ("Proyecto  X", "GG2-Z", "Parciales mortales", "Potencial", "Randomizado", "SetaMax",
               "Caraoque", "KarateKid", "X-men", "Spider-Man", "Superman", "Batman Ark.nigth")

    for i in range(n):
        codigo = random.randint(100, 999)
        titulo = random.choice(titulos)
        genero = random.randint(0, 5)
        calificacion = random.randint(1, 5)

        pelicula = Pelicula(codigo, titulo, genero, calificacion)

        add_in_order_binary(v, pelicula)


def mostrar_vector(v):
    if len(v) == 0:
        print("\nEl vector esta vacio, cargue los datos...")
        print()
        return

    print("\nEl listado de peliculas es: ", end="\n\n")
    for pelicula in v:
        print(to_string(pelicula))


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo no existe...")
        print()
        return

    m = open(fd, "rb")
    t = os.path.getsize(fd)

    while m.tell() < t:
        pelicula = pickle.load(m)
        print(to_string(pelicula))

    m.close()


def cargar_archivo(v, genero, fd):
    if len(v) == 0:
        print("\nEl vector esta vacio, cargue los datos...")
        print()
        return

    m = open(fd, "wb")

    for pelicula in v:
        if pelicula.genero == genero:
            pickle.dump(pelicula, m)

    print("El archivo ", fd, "se creo correctamente. Su contenido: ", end="\n\n")

    m.close()

    mostrar_archivo(fd)


def buscar_pelicula_codigo(v, cod):
    inicio = 0
    final = len(v) - 1
    while inicio <= final:
        puntero = (inicio+final) // 2
        if cod == v[puntero].codigo:
            return puntero
        elif cod > v[puntero].codigo:
            inicio = puntero + 1
        else:
            final = puntero - 1

    return -1


def buscar_pelicula_titulo(v, titulo, fd1):
    a = open(fd1, "ab")

    for pelicula in v:
        if pelicula.titulo == titulo:
            pickle.dump(pelicula, a)

            return f"\nSe agrego la pelicula {titulo} en el archivo {fd1}."

    a.close()

    return f"\nNo se encontro la pelicula {titulo} en el vector."


def test():
    v = []

    opc = -1
    while opc != 7:
        print("\n\t\t\tStreaming AlgoFlix++")
        print("-*-"*15)
        print("1.-Cargar los datos de 'n' peliculas en el vector.")
        print("2.-Mostrar los datos del vector.")
        print("3.-Grabar archivo por genero.")
        print("4.-Buscar por codigo.")
        print("5.-Peliculas por genero y calificacion.")
        print("6.-Buscar por titulo.")
        print("7.-Salir del programa.", end="\n\n")

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            n = modulo_validaciones.validar_positivo(0, "Cantidad de peliculas a cargar - (mayor a cero): ")
            cargar_vector(v, n)
        elif opc == 2:
            mostrar_vector(v)
        elif opc == 3:
            genero = modulo_validaciones.validar_rango(0, 5, "Ingrese genero [0-5]: ")
            fd = "Peliculas_{}".format(str(genero) + ".dat")

            cargar_archivo(v, genero, fd)

        elif opc == 4:
            cod = modulo_validaciones.validar_rango(100, 999, "Ingrese codigo a buscar: ")
            pos = buscar_pelicula_codigo(v, cod)
            
            if pos != -1:
                nueva_calificacion = modulo_validaciones.validar_rango(1, 5, "\nNueva calificacion [1-5]: ")
                v[pos].calificacion = nueva_calificacion
                print(f"\nSe modifico la calificacion de la pelicula - {v[pos].titulo} por {nueva_calificacion}"
                      f" (estrellas).")
            else:
                print(f"\nNo se encontro la pelicula con codigo - {cod}...")

        elif opc == 5:
            pass

        elif opc == 6:
            fd1 = "Votaciones.dat"
            titulo = input("Ingrese titulo a buscar: ")
            res_busqueda = buscar_pelicula_titulo(v, titulo, fd1)
            print(res_busqueda, end="\n\n")
            print(f"\nLos datos del arhivo {fd1} se muestran actualizados a continuacion - (todos): ")
            mostrar_archivo(fd1)

        elif opc == 7:
            print("\nPrograma terminado.")
        else:
            print("\nOpcion incorrecta !")


if __name__ == "__main__":
    test()
