__author__ = "Wendler Juan Jose"

print("\n\t\tJUEGO DE DADOS:")


reglas_del_juego = "\nReglas de la primera ronda:" \
                   "Lanza los 3 dados el tercer jugador." \
                   "a) Si los tres dados fueran iguales el jugador suma 6 puntos." \
                   "b) Si el jugador tuviera dos dados iguales y uno distinto, " \
                   "entonces el jugador vuelve a tirar, " \
                   "pero únicamente el dado distinto. " \
                   "Si al volver a lanzar ese dado logra que los tres dados sean iguales," \
                   " sumará 6 puntos en esa ronda. " \
                   "Si el dado relanzado sigue siendo distinto a los dos que eran iguales, " \
                   "el jugador sumará 3 puntos en esa ronda." \
                   "c) Si los tres dados fueran todos distintos, entonces obtiene 0 puntos y" \
                   " no puede volver a tirar ningún dado en esa ronda." \
                   "Lanza los 3 dados el segundo jugador." \
                   "Reglas de la Segunda Ronda:" \
                   "El primer jugador lanza los 3 dados." \
                   "a)Se considera que apuesta todo el puntaje de la ronda anterior a par/impar" \
                   "b) Si la suma de los tres dados en esta segunda jugada es de la paridad elegida, " \
                   "entonces suma el dado de mayor valor a su puntaje de la ronda anterior; en caso contrario, " \
                   "resta el dado de menor valor a su puntaje anterior." \
                   "c) Si la suma en la segunda jugada es de la paridad elegida, se duplica el puntaje total." \
                   "Se repite la jugada para el segundo jugador con las mismas reglas que el primero." \
                   "Final del Juego:" \
                   "Gana el jugador que más puntaje haya obtenido."

jugador_1 = input("Ingresar el nombre del primer jugador: ")
jugador_2 = input("Ingresar el nombre del segundo jugador: ")

acumulador_punt_jug_1 = 0
acumulador_punt_jug_2 = 0

import random

posibles_nombres = ("gamer123",  "fire431", "skyland300", "gatuno3000", "goku14", "777", "Ironer", "nicetop" \
                    "flama", "motoroil43", "gasmonkey", "spiderman", "remoto1436", "furioso", "sony", "nogaman")
salida_posibles_nombres = random.choice(posibles_nombres)
if jugador_1 == jugador_2:
    print("Ambos nombres son iguales, cambia uno o quizas puedas intentar con: ", jugador_1 + "", salida_posibles_nombres )
    jugador_1 = input("Ingresar el nombre del primer jugador: ")
    jugador_2 = input("Ingresar el nombre del primer jugador: ")


visualizacion_reglas = input("¿Desea conocer las reglas del juego? ")
afirmacion = "si"
negacion = "no"
inicio = input("¿Listo para comenzar? ")

if visualizacion_reglas == afirmacion:
    print(reglas_del_juego)
elif inicio == afirmacion:
    print("Iniciando juego...")
else:
    print("Mas tarde sera, no olvides que puedes chequear las reglas del juego.")

# DATOS DE LOS DADOS
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)


# RONDA 1

# PRIMERA JUGADA DEL JUGADOR 1
print("Comienza la primera ronda: ", "\n","El primer jugador va a lanzar primero.")


# Si todos son iguales
if dado1 == dado2 == dado3:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("Todos los dados son iguales, sumas 6 puntos. ")
    acumulador_punt_jug_1 = acumulador_punt_jug_1 + 6



# Si el TERCER dado es distinto
else:
    if dado1 == dado2 and dado1 != dado3 and dado2 != dado3:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("El tercer es distinto, lo volvemos a lanzar.")
        dado3 = random.randint(1,6)
        print("El dado 3 dio:", dado3)
        if dado1 == dado2 == dado3:
            print("Los dados obtenidos son: ",dado1,dado2,dado3)
            print("Todos los dados son iguales, sumas 6 puntos: ")
            acumulador_punt_jug_1 = acumulador_punt_jug_1 + 6
        else:
            print("Los dados obtenidos son: ",dado1,dado2,dado3)
            print("El tercer dado dio distinto nuevamente, sumas 3 puntos.")
            acumulador_punt_jug_1 = acumulador_punt_jug_1 + 3



# Si el PRIMER dado es distinto
if dado2 == dado3 and dado2 != dado1 and dado3 != dado1:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("El primer dado es distinto, lo volvemos a lanzar.")
    dado1 = random.randint(1,6)
    print("El primer dado dio:", dado1)
    if dado1 == dado2 == dado3:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("Todos los dados son iguales, sumas 6 puntos: ")
        acumulador_punt_jug_1 = acumulador_punt_jug_1 + 6
    else:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("El primer dado dio distinto nuevamente, sumas 3 puntos.")
        acumulador_punt_jug_1 = acumulador_punt_jug_1 + 3



# Si el SEGUNDO dado es distinto
if dado1 == dado3 and dado1 != dado2 and dado3 != dado2:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("El segundo dado es distinto, lo volvemos a lanzar.")
    dado2 = random.randint(1,6)
    print("El segundo dado dio:", dado2)
    if dado1 == dado2 == dado3:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("Todos los dados son iguales, sumas 6 puntos: ")
        acumulador_punt_jug_1 = acumulador_punt_jug_1 + 6
    else:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("El primer dado dio distinto nuevamente, sumas 3 puntos.")
        acumulador_punt_jug_1 = acumulador_punt_jug_1 + 3


# Si Todos los dados son distintos
if dado1 != dado2 != dado3:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("Todos los dados son distintos, sumas 0 puntos")



# PRIMERA JUGADA DEL JUGADOR 2

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)

print("Ahora es el turno del segundo jugador.")


# Si todos son iguales
if dado1 == dado2 == dado3:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("Todos los dados son iguales, sumas 6 puntos. ")
    acumulador_punt_jug_2 = acumulador_punt_jug_2 + 6



# Si el TERCER dado es distinto
else:
    if dado1 == dado2 and dado1 != dado3 and dado2 != dado3:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("El tercer es distinto, lo volvemos a lanzar.")
        dado3 = random.randint(1,6)
        print("El dado 3 dio:", dado3)
        if dado1 == dado2 == dado3:
            print("Los dados obtenidos son: ",dado1,dado2,dado3)
            print("Todos los dados son iguales, sumas 6 puntos: ")
            acumulador_punt_jug_2 = acumulador_punt_jug_2 + 6
        else:
            print("Los dados obtenidos son: ",dado1,dado2,dado3)
            print("El tercer dado dio distinto nuevamente, sumas 3 puntos.")
            acumulador_punt_jug_2 = acumulador_punt_jug_2 + 3



# Si el PRIMER dado es distinto
if dado2 == dado3 and dado2 != dado1 and dado3 != dado1:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("El primer dado es distinto, lo volvemos a lanzar.")
    dado1 = random.randint(1,6)
    print("El primer dado dio:", dado1)
    if dado1 == dado2 == dado3:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("Todos los dados son iguales, sumas 6 puntos: ")
        acumulador_punt_jug_2 = acumulador_punt_jug_2 + 6
    else:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("El primer dado dio distinto nuevamente, sumas 3 puntos.")
        acumulador_punt_jug_2 = acumulador_punt_jug_2 + 3



# Si el SEGUNDO dado es distinto
if dado1 == dado3 and dado1 != dado2 and dado3 != dado2:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("El segundo dado es distinto, lo volvemos a lanzar.")
    dado2 = random.randint(1,6)
    print("El segundo dado dio:", dado2)
    if dado1 == dado2 == dado3:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("Todos los dados son iguales, sumas 6 puntos: ")
        acumulador_punt_jug_2 = acumulador_punt_jug_2 + 6
    else:
        print("Los dados obtenidos son: ",dado1,dado2,dado3)
        print("El primer dado dio distinto nuevamente, sumas 3 puntos.")
        acumulador_punt_jug_2 = acumulador_punt_jug_2 + 3


# Si Todos los dados son distintos
if dado1 != dado2 != dado3:
    print("Los dados obtenidos son: ",dado1,dado2,dado3)
    print("Todos los dados son distintos, sumas 0 puntos")

# RONDA 2

# El primer jugador elige
print("Comienza la segunda ronda.")
eleccion_jug1 =input("¿Apuestas todo a par o impar?")
print("El primer jugador esta lanzando los dados...")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)

print("Los dados obtenidos fueron: ", dado1,dado2,dado3)

sumatoria = dado1 + dado2 + dado3
print("La sumatoria de los 3 dados nos dio: ", sumatoria)

if sumatoria %2 == 0 and eleccion_jug1 == "par":
    print("La sumatoria es: ", sumatoria, "es par. Sumas: ", max(dado1,dado2,dado3))
    acumulador_punt_jug_1 = acumulador_punt_jug_1 + max(dado1,dado2,dado3)
else:
    if sumatoria %2 != 0 and eleccion_jug1 == "impar":
        print("La sumatoria es impar", sumatoria, "es impar. Sumas: ", max(dado1,dado2,dado3))
    else:
        acumulador_punt_jug_1 = acumulador_punt_jug_1 - min(dado1,dado2,dado3)
        print("Se le resto el minimo de los dados obtenidos a tu puntaje: ", "-", min(dado1,dado2,dado3))

print("Los puntos obtenidos son: ",acumulador_punt_jug_1)


# El segundo jugador elige
print("Elige el segundo jugador.")
eleccion_jug2 =input("¿Apuestas todo a par o impar?")
print("El segundo jugador esta lanzando los dados...")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)

sumatoria = dado1 + dado2 + dado3

if sumatoria %2 == 0 and eleccion_jug2 == "par":
    print("La sumatoria: ", sumatoria, "es par. Sumas: ", max(dado1,dado2,dado3))
    acumulador_punt_jug_2 = acumulador_punt_jug_2 + max(dado1,dado2,dado3)
else:
    if sumatoria %2 != 0 and eleccion_jug1 == "impar":
        print("La sumatoria es impar", sumatoria, "es impar. Sumas: ", max(dado1,dado2,dado3))
        acumulador_punt_jug_2 = acumulador_punt_jug_2 + max(dado1,dado2,dado3)
    else:
        acumulador_punt_jug_2 = acumulador_punt_jug_2 - min(dado1,dado2,dado3)
        print("Se le resto el minimo de los dados obtenidos a tu puntaje: ", "-", min(dado1,dado2,dado3))

print("Los puntos obtenidos son: ",acumulador_punt_jug_2)

# Fin del juego
if acumulador_punt_jug_1 > acumulador_punt_jug_2:
    print("El jugador: ", jugador_1, "ha ganado.")
else:
    if acumulador_punt_jug_2 > acumulador_punt_jug_1:
        print("El jugador: ", jugador_2, "ha ganado.")
    else:
        print("Han empatado.")






