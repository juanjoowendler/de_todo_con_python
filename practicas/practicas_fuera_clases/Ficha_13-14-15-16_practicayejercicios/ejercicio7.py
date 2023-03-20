# Desarrollar un programa que permita procesar el puntaje obtenido por una pareja de
# bailarines en un concurso de TV.

# Para ello, generar un vector de 7 elementos, representando
# a los miembros del jurado. Por cada celda, generar un valor
# aleatorio entre -1 y 10 (inclusive) indicando la puntuación
# recibida.

# A continuación, informar:

# •Los tres mejores puntajes recibidos.

# •Si algún jurado los calificó con 6. En caso afirmativo,
# indicar cuántas notas mayores a esa recibieron.

# •La diferencia entre el mayor y el menor puntaje.

# •El puntaje total obtenido. Si es menor a 20, indicar
# que quedan descalificados.


import random as psg


def generacion(n):
    votos = list()
    for i in range(1, n + 1):
        voto = psg.randint(1, 10)
        votos.append(voto)
    return votos


def selection_sort(votos):
    # ordenamiento por seleccion directa
    n = len(votos)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if votos[i] > votos[j]:
                votos[i], votos[j] = votos[j], votos[i]


def mayores_6(votos):
    cant, band = 0, False
    for i in votos:
        if i == 6:
            band = True
        if band and i > 6:
            cant += 1
    return cant


def total(votos):
    suma = 0
    for elemento in votos:
        suma += elemento
    return suma


def principal():
    votos = generacion(n=7)
    print("Votos obtenidos: ", votos, end=" pts.\n")
    selection_sort(votos)
    print("Tres mejores: ", votos[4:], end=" pts.\n")
    cant = mayores_6(votos)
    print("Cantidad de votos mayores a 6 -> ", cant)
    dif = votos[-1] - votos[0]
    print("La diferencia entre el mayor y el menor es: ", dif)
    totala = total(votos)
    print("El puntaje total es de: ", totala)
    if totala < 20:
        print(" ! Quedan descalificados.")


if __name__ == "__main__":
    principal()
