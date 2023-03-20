def img_dados(dx):

    if dx == 1:
        print(d1img)
    elif dx == 2:
        print(d2img)
    elif dx == 3:
        print(d3img)
    elif dx == 4:
        print(d4img)
    elif dx == 5:
        print(d5img)
    else:
        print(d6img)

    if dx == 1:
        print(d1img)
    elif dx == 2:
        print(d2img)
    elif dx == 3:
        print(d3img)
    elif dx == 4:
        print(d4img)
    elif dx == 5:
        print(d5img)
    else:
        print(d6img)

    if dx == 1:
        print(d1img)
    elif dx == 2:
        print(d2img)
    elif dx == 3:
        print(d3img)
    elif dx == 4:
        print(d4img)
    elif dx == 5:
        print(d5img)
    else:
        print(d6img)

# IMPORTACION DE LA BIBLIOTECA
import random

# DADOS IMG

d1img = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░██░░░░░░░░░░░░░░░██░░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░▄▄░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░▐██▌░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░▀▀░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░░██░░░░░░░░░░░░░░░██░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

d2img = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░██░░░░░░░░▄▄░░░░░██░░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░░░██▌░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░░░░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░▐██░░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░░██░░░░░▀▀░░░░░░░░██░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

d3img = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░▄▄░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░██░░░░░░░░░▐██░░░██░░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░▄▄░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░██▌░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░▄▄░░░░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░░██░░▐██░░░░░░░░░░██░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

d4img = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░██░░░██▌░░░▐██░░░██░░░░░░░░░░░░░\
\n░░░░░░░░███░░░▀▀░░░░░▀▀░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░░░░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░▄▄░░░░░▄▄░░░███░░░░░░░░░░░░\
\n░░░░░░░░░██░░░██▌░░░▐██░░░██░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

d5img = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░▄▄░░░░░▄▄░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░██░░▐██░░░░░██▌░░██░░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░▄▄░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░██▌░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░▄▄░░░░░▄▄░░░███░░░░░░░░░░░░\
\n░░░░░░░░░██░░▐██░░░░░██▌░░██░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

d6img = "\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░██░░██▌░▐██░░██▌░██░░░░░░░░░░░░░\
\n░░░░░░░░███░░▀▀░░░▀▀░░▀▀░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░░░░░░░░░░░░░░███░░░░░░░░░░░░\
\n░░░░░░░░███░░▄▄░░░▄▄░░▄▄░░███░░░░░░░░░░░░\
\n░░░░░░░░░██░░██▌░▐██░░██▌░██░░░░░░░░░░░░░\
\n░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░\
\n░░░░░░░░░░░███████████████░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░\
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"

# ACUMULADORES DE PUNTAJE

acum_punt_jug_1 = 0
acum_punt_jug_2 = 0

# REGLAS DEL JUEGO

print("\n\t(っ◔◡◔)っ ☻ JUEGO DE 2 o 3 ☻")

reglas_del_juego = "\n\t▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒░\n\tREGLAS DE LA PRIMERA RONDA:\n\t░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒\n\n\t" \
                   "'Se lanzan los dados...'\n" \
                   "\n\t\ta) Si los tres dados fueran iguales el jugador suma 6 puntos.\n\n\t\tb)" \
                   "Si el jugador tuviera dos dados iguales y uno distinto, entonces" \
                   " el jugador vuelve a tirar,\n\t\t pero únicamente el dado distinto. Si al" \
                   " volver a lanzar ese dado logra que los tres dados sean\n\t\t iguales," \
                   " sumará 6 puntos en esa ronda. Si el dado relanzado sigue siendo" \
                   " distinto a los\n\t\t dos que eran iguales, el jugador sumará 3 puntos" \
                   " en esa ronda. \n\n\t\tc) Si los tres dados fueran todos distintos, entonces" \
                   " obtiene 0 puntos y no puede volver\n\t\t a tirar en esa ronda.\n\t\t" \
                   "\n\n\t ▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒░\n\t REGLAS DE LA SEGUNDA " \
                   "RONDA:\n\t ▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒░" \
                   "\n\n\t'Se lanzan los dados...' \n\n\t\ta) Se considera que apuesta todo" \
                   " el puntaje de la ronda anterior\n\t\t a par/impar \n\n\t\tb) Si la suma de los tres" \
                   " dados en esta segunda jugada es de la paridad elegida, entonces\n\t\t suma" \
                   " el dado de mayor valor a su puntaje de la ronda anterior; en caso" \
                   " contrario, resta\n\t\t el dado de menor valor a su puntaje anterior." \
                   "\n\n\t\tc) Si la suma en la segunda jugada es de la paridad elegida, se" \
                   " duplica el puntaje total.\n\t\t Se repite la jugada para el segundo" \
                   " jugador con las mismas reglas que el primero.\n\n\t▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒░\n\t\t FINAL DEL " \
                   "JUEGO:\n\t▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒░\n \n\t\tGana el jugador que más puntaje haya obtenido."

# VISUALIZACION DE LAS REGLAS

visualizacion_reglas = input("\t\t\n¿Desea conocer las reglas del juego? ")
afirmacion = "si"
negacion = "no"

if visualizacion_reglas == afirmacion:
    print(reglas_del_juego)
elif visualizacion_reglas == negacion:
    print("En otro momento sera.")

# INGRESO DEL NOMBRE DE LOS JUGADORES

jugador_1 = input("\nIngresar el nombre del primer jugador: ")
jugador_2 = input("Ingresar el nombre del segundo jugador: ")

# COMPARACION DE NOMBRES IGUALES

posibles_nombres = ("gamer123", "fire431", "skyland300", "gatuno3000", "goku14", "777", "Ironer", "nicetop"\
                    "flama", "motoroil43", "gasmonkey", "spiderman", "remoto1436", "furioso", "sony", "nogaman")
salida_posibles_nombres = random.choice(posibles_nombres)
if jugador_1 == jugador_2:
    print("\n-Ambos nombres son iguales, cambia uno o quizas puedas intentar con: ", jugador_1 + "",
          salida_posibles_nombres)
    jugador_1 = input("\nIngresar nuevamente el nombre del primer jugador: ")
    jugador_2 = input("Ingresar nuevamente el nombre del segundo jugador: ")
print("Iniciando juego...")

# INICIO DEL JUEGO

comenzar = input("Escribe cualquier tecla para comenzar: ")
print("\n\tIniciando primera ronda...")

print("\n", "-" * 50)
print("\n▒▓█▓▒░", jugador_1, "lanzara los dados ▒▓█▓▒░")
comenzar = input("Escribe cualquier tecla para lanzar los dados: ")

#              COMIENZO DE RONDA 1

# LANZAMIENTO DEL PRIMER JUGADOR

dado_1, dado_2, dado_3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print("\n-Los dados obtenidos son: ", dado_1, dado_2, dado_3)

# IMAGENES DE DADOS

if dado_1 == 1:
    print(d1img)
elif dado_1 == 2:
    print(d2img)
elif dado_1 == 3:
    print(d3img)
elif dado_1 == 4:
    print(d4img)
elif dado_1 == 5:
    print(d5img)
else:
    print(d6img)

if dado_2 == 1:
    print(d1img)
elif dado_2 == 2:
    print(d2img)
elif dado_2 == 3:
    print(d3img)
elif dado_2 == 4:
    print(d4img)
elif dado_2 == 5:
    print(d5img)
else:
    print(d6img)

if dado_3 == 1:
    print(d1img)
elif dado_3 == 2:
    print(d2img)
elif dado_3 == 3:
    print(d3img)
elif dado_3 == 4:
    print(d4img)
elif dado_3 == 5:
    print(d5img)
else:
    print(d6img)

# VALIDACION DE DADOS

if dado_1 == dado_2 == dado_3:
    acum_punt_jug_1 += 6
else:
    if dado_1 == dado_2:
        print("\n\tSe volvera a tirar el tercer dado")
        dado_3 = random.randint(1, 6)
        print("\tEl tercer dado dio:", dado_3)
        if dado_3 == 1:
            print(d1img)
        elif dado_3 == 2:
            print(d2img)
        elif dado_3 == 3:
            print(d3img)
        elif dado_3 == 4:
            print(d4img)
        elif dado_3 == 5:
            print(d5img)
        elif dado_3 == 6:
            print(d6img)
        if dado_1 == dado_2 == dado_3:
            acum_punt_jug_1 += 6
        else:
            acum_punt_jug_1 += 3

    elif dado_2 == dado_3:
        print("\n\tSe volvera a tirar el primer dado")
        dado_1 = random.randint(1, 6)
        print("\tEl primer dado dió:", dado_1)
        if dado_1 == 1:
            print(d1img)
        elif dado_1 == 2:
            print(d2img)
        elif dado_1 == 3:
            print(d3img)
        elif dado_1 == 4:
            print(d4img)
        elif dado_1 == 5:
            print(d5img)
        elif dado_1 == 6:
            print(d6img)
        if dado_1 == dado_2 == dado_3:
            acum_punt_jug_1 += 6
        else:
            acum_punt_jug_1 += 3
    else:
        if dado_1 == dado_3:
            print("\n\tSe volvera a tirar el segundo dado")
            dado_2 = random.randint(1, 6)
            print("\tEl segundo dado dio:", dado_2)
            if dado_2 == 1:
                print(d1img)
            elif dado_2 == 2:
                print(d2img)
            elif dado_2 == 3:
                print(d3img)
            elif dado_2 == 4:
                print(d4img)
            elif dado_2 == 5:
                print(d5img)
            elif dado_2 == 6:
                print(d6img)
            if dado_1 == dado_2 == dado_3:
                acum_punt_jug_1 += 6
            else:
                acum_punt_jug_1 += 3

if dado_1 != dado_2 != dado_3 != dado_1:
    print("\n\t", jugador_1, "No suma puntos...")

# MOSTRAR PUNTAJE
print("\n\tEl puntaje de", jugador_1, "es:", acum_punt_jug_1)

# --------------------------------------------------------------------------------------------------------------

print("\n", "-" * 50)
print("\n▒▓█▓▒░", jugador_2, "lanzara los dados ▒▓█▓▒░")
comenzar = input("Escribe cualquier tecla para lanzar los dados: ")

# LANZAMIENTO DEL SEGUNDO JUGADOR

dado_1, dado_2, dado_3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print("-Los dados obtenidos son: ", dado_1, dado_2, dado_3)

# IMAGENES DE DADOS

if dado_1 == 1:
    print(d1img)
elif dado_1 == 2:
    print(d2img)
elif dado_1 == 3:
    print(d3img)
elif dado_1 == 4:
    print(d4img)
elif dado_1 == 5:
    print(d5img)
else:
    print(d6img)

if dado_2 == 1:
    print(d1img)
elif dado_2 == 2:
    print(d2img)
elif dado_2 == 3:
    print(d3img)
elif dado_2 == 4:
    print(d4img)
elif dado_2 == 5:
    print(d5img)
else:
    print(d6img)

if dado_3 == 1:
    print(d1img)
elif dado_3 == 2:
    print(d2img)
elif dado_3 == 3:
    print(d3img)
elif dado_3 == 4:
    print(d4img)
elif dado_3 == 5:
    print(d5img)
else:
    print(d6img)

# VALIDACION DE DADOS

if dado_1 == dado_2 == dado_3:
    acum_punt_jug_2 += 6
else:
    if dado_1 == dado_2:
        print("\n\tSe volvera a tirar el tercer dado")
        dado_3 = random.randint(1, 6)
        print("\tEl tercer dado dio:", dado_3)
        if dado_3 == 1:
            print(d1img)
        elif dado_3 == 2:
            print(d2img)
        elif dado_3 == 3:
            print(d3img)
        elif dado_3 == 4:
            print(d4img)
        elif dado_3 == 5:
            print(d5img)
        else:
            print(d6img)
        if dado_1 == dado_2 == dado_3:
            acum_punt_jug_2 += 6
        else:
            acum_punt_jug_2 += 3
    else:
        if dado_2 == dado_3:
            print("\n\tSe volvera a tirar el primer dado")
            dado_1 = random.randint(1, 6)
            print("\tEl primer dado dió:", dado_1)
            if dado_1 == 1:
                print(d1img)
            elif dado_1 == 2:
                print(d2img)
            elif dado_1 == 3:
                print(d3img)
            elif dado_1 == 4:
                print(d4img)
            elif dado_1 == 5:
                print(d5img)
            else:
                print(d6img)
            if dado_1 == dado_2 == dado_3:
                acum_punt_jug_2 += 6
            else:
                acum_punt_jug_2 += 3
        else:
            if dado_1 == dado_3:
                print("\n\tSe volvera a tirar el segundo dado")
                dado_2 = random.randint(1, 6)
                print("\tEl segundo dado dio:", dado_2)
                if dado_2 == 1:
                    print(d1img)
                elif dado_2 == 2:
                    print(d2img)
                elif dado_2 == 3:
                    print(d3img)
                elif dado_2 == 4:
                    print(d4img)
                elif dado_2 == 5:
                    print(d5img)
                else:
                    print(d6img)
                if dado_1 == dado_2 == dado_3:
                    acum_punt_jug_2 += 6
                else:
                    acum_punt_jug_2 += 3

if dado_1 != dado_2 != dado_3 != dado_1:
    print("\n\t", jugador_2, "No suma puntos...")

# MOSTRAR PUNTAJE

print("\n\tEl puntaje de", jugador_2, "es:", acum_punt_jug_2)

#              COMIENZO DE RONDA 2

print("\n", "-" * 50)
print("\n\tIniciando segunda ronda...")
comenzar = input("Escribe cualquier tecla para comenzar la segunda ronda: ")
print("\n▒▓█▓▒░", jugador_1, "elegira... ▒▓█▓▒░")
eleccion_jugador_1 = input("\n¿Apuestas todo a par o impar (si escribe mal se tomara como eleccion impar)? ")
comenzar = input("Escribe cualquier tecla para lanzar los dados: ")

# LANZAMIENTO DEL PRIMER JUGADOR

dado_1, dado_2, dado_3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)


print("-Los dados obtenidos son: ", dado_1, dado_2, dado_3)

# IMAGENES DE DADOS

if dado_1 == 1:
    print(d1img)
elif dado_1 == 2:
    print(d2img)
elif dado_1 == 3:
    print(d3img)
elif dado_1 == 4:
    print(d4img)
elif dado_1 == 5:
    print(d5img)
else:
    print(d6img)

if dado_2 == 1:
    print(d1img)
elif dado_2 == 2:
    print(d2img)
elif dado_2 == 3:
    print(d3img)
elif dado_2 == 4:
    print(d4img)
elif dado_2 == 5:
    print(d5img)
else:
    print(d6img)

if dado_3 == 1:
    print(d1img)
elif dado_3 == 2:
    print(d2img)
elif dado_3 == 3:
    print(d3img)
elif dado_3 == 4:
    print(d4img)
elif dado_3 == 5:
    print(d5img)
else:
    print(d6img)

sumatoria = dado_1 + dado_2 + dado_3
print("La sumatoria de los 3 dados nos dio: ", sumatoria)

if eleccion_jugador_1 == "par":
    eleccion_jugador_1 = 0
else:
    eleccion_jugador_1 = 1

if sumatoria % 2 == 0 and eleccion_jugador_1 == sumatoria % 2:
    acum_punt_jug_1 += max(dado_1, dado_2, dado_3)
    print("\t", jugador_1, "suma:", max(dado_1, dado_2, dado_3), "puntos")
else:
    if sumatoria % 2 == 1 and eleccion_jugador_1 == sumatoria % 2:
        print("La sumatoria es impar", sumatoria, "suma: ", max(dado_1, dado_2, dado_3))
        acum_punt_jug_1 += max(dado_1, dado_2, dado_3)
    else:
        acum_punt_jug_1 -= min(dado_1, dado_2, dado_3)
        print("\t", jugador_1, "resta:", min(dado_1, dado_2, dado_3), "puntos")

# VERIFICACION Y DUPLICACION DE PUNTOS SI HAY PARIDAD EN LOS DADOS

if dado_1 % 2 == eleccion_jugador_1 and dado_2 % 2 == eleccion_jugador_1 and dado_3 % 2 == eleccion_jugador_1:
    acum_punt_jug_1 *= 2
    print(jugador_1, "duplico sus puntos, todos sus dados fueron de la paridad elegida.")

# -----------------------------------------------------------------------------------------------------------

# TURNO DEL SEGUNDO JUGADOR

print("\n", "-" * 50)
print("\n▒▓█▓▒░", jugador_2, "elegira... ▒▓█▓▒░")
eleccion_jugador_2 = input("\n¿Apuestas todo a par o impar (si escribe mal se tomara como eleccion impar)? ")
comenzar = input("Escribe cualquier tecla para lanzar los dados: ")

# LANZAMIENTO DEL SEGUNDO JUGADOR

dado_1, dado_2, dado_3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print("Los dados obtenidos son: ", dado_1, dado_2, dado_3)

# IMAGENES DE DADOS

if dado_1 == 1:
    print(d1img)
elif dado_1 == 2:
    print(d2img)
elif dado_1 == 3:
    print(d3img)
elif dado_1 == 4:
    print(d4img)
elif dado_1 == 5:
    print(d5img)
else:
    print(d6img)

if dado_2 == 1:
    print(d1img)
elif dado_2 == 2:
    print(d2img)
elif dado_2 == 3:
    print(d3img)
elif dado_2 == 4:
    print(d4img)
elif dado_2 == 5:
    print(d5img)
else:
    print(d6img)

if dado_3 == 1:
    print(d1img)
elif dado_3 == 2:
    print(d2img)
elif dado_3 == 3:
    print(d3img)
elif dado_3 == 4:
    print(d4img)
elif dado_3 == 5:
    print(d5img)
else:
    print(d6img)

sumatoria = dado_1 + dado_2 + dado_3
print("La sumatoria de los 3 dados nos dio: ", sumatoria)

if eleccion_jugador_2 == "par":
    eleccion_jugador_2 = 0
else:
    eleccion_jugador_2 = 1

if sumatoria % 2 == 0 and eleccion_jugador_2 == sumatoria % 2:
    acum_punt_jug_2 += max(dado_1, dado_2, dado_3)
    print("\t", jugador_2, "suma:", max(dado_1, dado_2, dado_3), "puntos")
else:
    if sumatoria % 2 == 1 and eleccion_jugador_2 == sumatoria % 2:
        print("La sumatoria es impar", sumatoria, "sumas: ", max(dado_1, dado_2, dado_3))
        acum_punt_jug_2 += max(dado_1, dado_2, dado_3)
    else:
        acum_punt_jug_2 -= min(dado_1, dado_2, dado_3)
        print("\t", jugador_2, "resta:", min(dado_1, dado_2, dado_3), "puntos")

# VERIFICACION Y DUPLICACION DE PUNTOS SI HAY PARIDAD EN LOS DADOS

if dado_1 % 2 == eleccion_jugador_2 and dado_2 % 2 == eleccion_jugador_2 and dado_3 % 2 == eleccion_jugador_2:
    acum_punt_jug_2 *= 2
    print(jugador_2, "duplico sus puntos, todos sus dados fueron de la paridad elegida.")

# FINAL DEL JUEGO
print("\n- Puntaje de", jugador_1 + ":", acum_punt_jug_1, "\t\n- Puntaje de", jugador_2 + ":", acum_punt_jug_2)

if acum_punt_jug_1 > acum_punt_jug_2:
    print("\n\t▒▓█▓▒░ El ganador es:", jugador_1 + " ▒▓█▓▒░")
elif acum_punt_jug_1 < acum_punt_jug_2:
    print("\n\t▒▓█▓▒░ El ganador es:", jugador_2 + " ▒▓█▓▒░")
else:
    print("\n\t▒▓█▓▒░ Han empatado ▒▓█▓▒░")
