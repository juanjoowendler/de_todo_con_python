from random import random, randint


def menu():
    cadena = "\n\t\tMenu de Opciones\n" \
             "==================================\n" \
             "1) Los tres mejores puntajes recibidos\n" \
             "2) Indicar cuantos jueces calificaron con mas de 6\n" \
             "3) Indicar el puntaje promedio que obtuvo la gimnasta\n" \
             "4) Indicar cuantas veces se repitio la menor nota\n" \
             "5) Genere un nuevo vector, tal que no admita notas repetidas\n" \
             "6) Salir\n" \
             "\nIngrese su opcion: "
    return cadena


def generar_arreglo(vector):
    for i in range(len(vector)):
        vector[i] = randint(1, 10)


def ordenar_arreglo(vector):
    tam = len(vector)
    for i in range(tam - 1):
        for j in range(1, tam):
            if vector[i] < [j]:
                vector[i], vector[j] = vector[j], vector[i]


def principal():
    print("\n\t\tREPASO DE VECTORES: ")
    print("*" * 40)
    opcion = 0

    puntuaciones = [None] * 9
    print(puntuaciones)
    generar_arreglo(puntuaciones)
    print(puntuaciones)
    ordenar_arreglo(puntuaciones)
    print(puntuaciones)


   # FORMAS DE CREAR ARREGLOS
   # puntuaciones = []
   # puntuaciones = list()
   # puntuaciones = [0] * 9
   # puntuaciones = [None] * 9


    while opcion != 5:

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass


if __name__ == "__main__":
    principal()
