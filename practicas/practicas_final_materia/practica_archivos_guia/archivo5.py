__author__ = "Wendler Juan Jose"

"""
Un amigo tiene una lista de series que le gustaría ver, guardadas en un archivo “series.csv” y nos 
pide ayuda para poder manejar dicha lista. El archivo posee la siguiente información de cada serie:

Título o nombre 
Género: 0-Infantil, 1-Comedia, 2-Romántico, 3-Drama, 4-Ciencia Ficción, 5-Otros.
Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
Cantidad de temporadas.
Duracion total (en minutos)
En primer lugar, cargar el contenido del archivo en un vector de registros y ordenarlo por título.

Luego, implementar un menú de opciones que permita:

Listar el contenido del vector, mostrando una línea por serie (usar género y el idioma en lugar de sus códigos).

Ingresar por teclado un idioma x. Generar un archivo cuyo nombre tenga la forma “SeriesX.dat” (reemplazando x 
por el número del idioma seleccionado) conteniendo todas las series de ese idioma que tengan más de una temporada. 
Mostrar el nuevo archivo generado.

Buscar en el vector una serie con el título x (x se ingresa por teclado). Si la serie existe, mostrar sus datos.
Si no, informar con un mensaje.

Determinar la duración total de las series en idioma español por cada género disponible.

A partir del vector determinar la cantidad de series por género y por idioma. Para eso se debe utilizar una 
matriz de conteo. Mostrar las cantidades sólo cuando sean mayores a 0.
"""

import pickle
import random
import os.path


class Serie:
    def __init__(self, tit, gen, idiom, cant, dur):
        self.titulo = tit
        self.genero = gen
        self.idioma = idiom
        self.cantidad = cant
        self.duracion = dur


def generar_archivo_csv():
    fd = 'series.csv'

    titulos = ('Friends', 'Lost', 'House of Cards', 'Mad Men', 'Vis a Vis',
               'La casa de papel', 'Breaking Bad', 'Dexter', 'This is us', 'The Crown',
               'House', 'Los Simpsons', 'Cobra Kai', 'Narcos', 'Stranger Things')

    m = open(fd, 'wt')

    for tit in titulos:
        genero = random.randint(0, 5)
        idioma = random.randint(0, 4)
        temporadas = random.randint(1, 10)
        duracion = random.randint(60, 600)
        linea = '{},{},{},{},{}\n'.format(tit, genero, idioma, temporadas, duracion)
        m.write(linea)

    m.close()
    print('Archivo', fd, 'generado.')


def to_string(v):

    if v.genero == 0:
        v.genero = "Infantil"
    elif v.genero == 1:
        v.genero = "Comedia"
    elif v.genero == 2:
        v.genero = "Romantico"
    elif v.genero == 3:
        v.genero = "Drama"
    elif v.genero == 4:
        v.genero = "C.Ficcion"
    else:
        v.genero = "Otros"

    if v.idioma == 0:
        v.idioma = "Español"
    elif v.idioma == 1:
        v.idioma = "Ingles"
    elif v.idioma == 2:
        v.idioma = "Frances"
    elif v.idioma == 3:
        v.idioma = "Portugues"
    else:
        v.idioma = "Otros"

    v.duracion = str(v.duracion) + " min"

    cad = ""
    cad += "{:<20}".format("Titulo:   " + v.titulo + "|")
    cad += "{:<25}".format("Genero:   " + v.genero)
    cad += "{:<25}".format("Idioma:   " + v.idioma)
    cad += "{:<20}".format("Cantidad: " + str(v.cantidad))
    cad += "{:<25}".format("Duracion: " + v.duracion)

    return cad


def add_in_order(v, serie):
    n = len(v)
    pos = n

    for i in range(n):
        if serie.titulo < v[i].titulo:
            pos = i
            break

    v[pos:pos] = [serie]


def main():
    v = []
    fd = "SeriesX.dat"

    opc = -1
    while opc != 5:
        print('-' * 80)
        print('CATÁLOGO DE SERIES')
        print('1. Mostrar vector')
        print('2. Generar archivo por idioma')
        print('3. Buscar por título')
        print('4. Duración de series en español por género')
        print('5. Contar por género e idioma')
        print('0. Salir')
        print('-' * 80)

        opc = int(input("\n\t-Ingrese su opcion: "))

        if opc == 1:
            mostrar_vector()

        elif opc == 2:
            pass

        elif opc == 3:
            pass

        elif opc == 4:
            pass

        elif opc == "x":
            print("Programa terminado.")

        else:
            print("Error ! valor incorrecto.")



if __name__ == "__main__":
    main()
