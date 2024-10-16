import random

# FUNCION PARA LAS IMAGENES DE LOS DADOS


def imagen_dados(D__1, D__2, D__3):

# PRINTS DE LOS DADOS

    d1img = "\n\x1b[1;35m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
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

    d2img = "\n\x1b[1;35m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
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

    d3img = "\n\x1b[1;35m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
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

    d4img = "\n\x1b[1;35m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
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

    d5img = "\n\x1b[1;35m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
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

    d6img = "\n\x1b[1;35m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
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

# VALIDACION PARA LOS PRINTS

    if D__1 == 1:
        print(d1img)
    elif D__1 == 2:
        print(d2img)
    elif D__1 == 3:
        print(d3img)
    elif D__1 == 4:
        print(d4img)
    elif D__1 == 5:
        print(d5img)
    else:
        print(d6img)

    if D__2 == 1:
        print(d1img)
    elif D__2 == 2:
        print(d2img)
    elif D__2 == 3:
        print(d3img)
    elif D__2 == 4:
        print(d4img)
    elif D__2 == 5:
        print(d5img)
    else:
        print(d6img)

    if D__3 == 1:
        print(d1img)
    elif D__3 == 2:
        print(d2img)
    elif D__3 == 3:
        print(d3img)
    elif D__3 == 4:
        print(d4img)
    elif D__3 == 5:
        print(d5img)
    else:
        print(d6img)


# FUNCION PARA INGRESAR LOS DATOS DE LOS JUGADORES Y VALIDAR SI SON DISTINTOS


def pl1_pl2(primero, segundo):
    while primero == segundo:
        print("\n \t\t\x1b[3;37m" + "Ingrese los nombres de los jugadores.")

        primero = input("\n \t\t\x1b[3;32m" + "Jugador 1: ")
        segundo = input("\t\tJugador 2: ")

        if primero == segundo:
            print("\n \t\t\x1b[3;31m" + "[ᵡ] Los jugadores no pueden llamarse igual, ingrese otros nombres.")

    return primero, segundo


# FUNCION PARA VALIDAR EL INGRESO DEL PUNTAJE FINAL


def puntaje_del_juego(p_f):
    while p_f < 11:
        print("\n \t\t\x1b[3;31m" + "[ᵡ] El puntaje no puede ser menor ni igual a 10, ingrese el puntaje de nuevo...")
        p_f = int(input("\n \t\t\x1b[3;37m" + "Limite de puntaje maximo de juego: "))

    return p_f


# FUNCION PARA LA ELECCION DEL JUGADOR


def v_eleccion(eleccion_jugador):
    if eleccion_jugador == "par":
        eleccion_jugador = 0
    else:
        eleccion_jugador = 1
    return eleccion_jugador


# FUNCION PARA VALIDAR ELECCIONES DE JUGADORES Y SUMAR, RESTAR O DUPLICAR PUNTAJES


def v_juego(jugador, acum_punt_jug, eleccion_jugador, dado_1, dado_2, dado_3):
    duplicidad_de_puntaje = False
    sumapuntaje = False
    aciertos = 0
    d_m = 0
    sumatoria = dado_1 + dado_2 + dado_3
    print("\n \t\t\x1b[3;34m" + "Salieron los dados:", "[", dado_1, dado_2, dado_3, "]")
    print("\n \t\t\x1b[3;35m" + "La sumatoria de los 3 dados nos dio:", sumatoria)

# VALIDACION DE LA ELECCION DEL JUGADOR

    if eleccion_jugador == 0:
        if sumatoria % 2 == 0:
            aciertos = 1
            sumapuntaje = True

    else:
        if sumatoria % 2 == 1:
            aciertos = 1
            sumapuntaje = True

# VALIDACION PARA LA DUPLICACION DE PUNTOS SI HAY PARIDAD EN LOS DADOS

    if eleccion_jugador == 0 and dado_1 % 2 == 0 and dado_2 % 2 == 0 and dado_3 % 2 == 0:
        d_m = max(dado_1, dado_2, dado_3) * 2
        duplicidad_de_puntaje = True

    if eleccion_jugador == 1 and dado_1 % 2 == 1 and dado_2 % 2 == 1 and dado_3 % 2 == 1:
        d_m = max(dado_1, dado_2, dado_3) * 2
        duplicidad_de_puntaje = True

# PRINTS PARA INFORMAR SI SE SUMA, RESTA O DUPLICAN LOS PUNTOS A LOS JUGADORES

    if duplicidad_de_puntaje:
        print("\n  \t\t", jugador, "duplico sus puntos, todos sus dados fueron de la "
                                   "paridad elegida, gano", d_m, "puntos.")

    elif duplicidad_de_puntaje == False and sumapuntaje == True:
        print("\n  \t\t\x1b[3;33m" + jugador, "gano", max(dado_1, dado_2, dado_3), "puntos.")

    else:
        print("\n  \t\t\x1b[3;33m" + jugador, "perdió", min(dado_1, dado_2, dado_3), "puntos.")

# SUMA RESTA O MULTIPLICACION DE EL PUNTAJE OBTENIDO

    if sumapuntaje:
        if duplicidad_de_puntaje:
            acum_punt_jug += d_m
        else:
            acum_punt_jug += max(dado_1, dado_2, dado_3)
    else:
        acum_punt_jug -= min(dado_1, dado_2, dado_3)

    return acum_punt_jug, aciertos, sumapuntaje


# FUNCION PARA


def juego_entero(puntaje_final):
    jugador_1, jugador_2 = "A", "A"
    jugador_1, jugador_2 = pl1_pl2(jugador_1, jugador_2)

# ACUMULADORES Y CONTADORES

    acum_punt_jug_1 = acum_punt_jug_2 = cantidad_jugadas = ronda_ganadaj2 = ronda_ganadaj1 = aciertos_jugador1 = 0
    aciertos_jugador2 = turnos_seguidos2 = turnos_seguidos1 = 0

# FLAGS

    bandera_salvame = empate = gano_3_turnos_seguidos = False

# CICLO PARA EJECUTAR EL JUEGO HASTA QUE ALGUN JUGADOR ALCANZE EL PUNTAJE PREVIAMENTE INGRESADO

    while not bandera_salvame:

# CONTADOR DE JUGADAS

        cantidad_jugadas += 1

        print("\n \t\t\x1b[3;37m" + "-" * 38)
        input("\n \t\t\x1b[2;37m" + "Presiona ENTER para comenzar...")

        print("\x1b[2;32m" + "\n \t\t▁ ▂ ▄", jugador_1, "juega primero ▄ ▂ ▁")
        print("\x1b[2;37m" + "\n \t\tElegí...")

        eleccion_jugador_1 = input("\t\t\x1b[2;32m" + "¿par ó impar? (si se deja en blanco, queda impar)\n \t\t")
        elec_1 = v_eleccion(eleccion_jugador_1)

        input("\n \t\t\x1b[2;37m" + "Presiona ENTER para continuar...")

# TIRO DE DADOS DEL JUGADOR 1 Y EJECUCION DE LAS FUNCIONES PARA REGISTRAR LOS DATOS PEDIDOS (PUNTAJE, ACIERTOS...)

        dado_1, dado_2, dado_3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
        imagen_dados(dado_1, dado_2, dado_3)

        puntaje_rondaj1, aciertos, sumapuntaje = v_juego(jugador_1, acum_punt_jug_1, elec_1, dado_1, dado_2, dado_3)
        aciertos_jugador1 += aciertos
        acum_punt_jug_1 = puntaje_rondaj1

# PRINT DE EL PUNTAJE PARCIAL JUGADOR 1


        print("\t\t\x1b[3;36m" + " El puntaje parcial de", jugador_1, "es", acum_punt_jug_1)

# TIRO DE DADOS DEL JUGADOR 2 Y EJECUCION DE LAS FUNCIONES PARA REGISTRAR LOS DATOS PEDIDOS (PUNTAJE, ACIERTOS...)

        print("\n \t\t\x1b[3;37m" + "-" * 38)

        input("\n \t\t\x1b[2;37m" + "Presiona ENTER para comenzar...")

        print("\x1b[2;32m" + "\n \t\t▁ ▂ ▄", jugador_2, "juega ▄ ▂ ▁")
        print("\x1b[2;37m" + "\n \t\tElegí...")
        eleccion_jugador_2 = input("\t\t\x1b[2;32m" + "¿par ó impar? (si se deja en blanco, queda impar)\n \t\t")
        elec_2 = v_eleccion(eleccion_jugador_2)

        dado_1, dado_2, dado_3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
        imagen_dados(dado_1, dado_2, dado_3)

        puntaje_rondaj2, aciertos, sumapuntaje = v_juego(jugador_2, acum_punt_jug_2, elec_2, dado_1, dado_2, dado_3)

        aciertos_jugador2 += aciertos
        acum_punt_jug_2 = puntaje_rondaj2

# PRINT DE EL PUNTAJE PARCIAL JUGADOR 2

        print("\t\t\x1b[3;36m" + " El puntaje parcial de", jugador_2, "es", acum_punt_jug_2)

# VALIDACION PARA CONTAR SI HAY UN EMPATE Y SI ALGUIEN GANO 3 RONDAS SEGUIDAS

        if puntaje_rondaj1 > puntaje_rondaj2 and sumapuntaje:
            turnos_seguidos2 = 0
            turnos_seguidos1 += 1

        elif puntaje_rondaj2 > puntaje_rondaj1 and sumapuntaje:
            turnos_seguidos1 = 0
            turnos_seguidos2 += 1

        else:
            turnos_seguidos1 = 0

            turnos_seguidos2 = 0

        if turnos_seguidos1 == 3 or turnos_seguidos2 == 3:
            gano_3_turnos_seguidos = True

        if puntaje_rondaj1 < puntaje_rondaj2:
            ronda_ganadaj2 += 1

        elif puntaje_rondaj1 > puntaje_rondaj2:
            ronda_ganadaj1 += 1
        else:
            empate = True

        if puntaje_final <= acum_punt_jug_1 or puntaje_final <= acum_punt_jug_2:
            bandera_salvame = True

    porcentaje_aciertos_1 = aciertos_jugador1 / cantidad_jugadas
    porcentaje_aciertos_2 = aciertos_jugador2 / cantidad_jugadas

    return jugador_1, jugador_2, acum_punt_jug_1, acum_punt_jug_2, cantidad_jugadas, empate, ronda_ganadaj1, \
           ronda_ganadaj2, aciertos_jugador1, aciertos_jugador2, gano_3_turnos_seguidos, porcentaje_aciertos_1,\
           porcentaje_aciertos_2


# FUNCION PARA MOSTRAR LOS PUNTAJES Y DATOS QUE SE PIDIERON


def salida_por_pantalla(jugador_1, jugador_2, puntaje_final_1, puntaje_final_2, ronda_ganadaj1, ronda_ganadaj2,
                        cantidad_jugadas, empate, aciertos_jugador1, aciertos_jugador2, gano_3_turnos_seguidos,
                        porcentaje_aciertos_1, porcentaje_aciertos_2):

    print("\n\x1b[3;33m" + "֎ - Puntaje de", jugador_1 + ":", puntaje_final_1, "\t\n֎ - Puntaje de",
          jugador_2 + ":", puntaje_final_2)

# VALIDACION DE ACIERTOS

    if aciertos_jugador1 > aciertos_jugador2:
        aciertos_jugador1 = "tuvo mayor porcentaje de aciertos que " + jugador_2 + "."
        aciertos_jugador2 = "tuvo menor porcentaje de aciertos que " + jugador_1 + "."

    elif aciertos_jugador1 < aciertos_jugador2:
        aciertos_jugador1 = "Tuvo menor porcentaje de aciertos que " + jugador_2 + "."
        aciertos_jugador2 = "Tuvo mayor porcentaje de aciertos que " + jugador_1 + "."
    else:
        aciertos_jugador1 = "Tuvo el mismo porcentaje de aciertos que " + jugador_2 + "."
        aciertos_jugador2 = "Tuvo el mismo porcentaje de aciertos que " + jugador_1 + "."

# VALIDACION Y PRINTS DE PUNTAJES

    if puntaje_final_1 > puntaje_final_2:
        print("\n\x1b[3;32m" + "►►► El ganador es:", jugador_1, "con", puntaje_final_1, "puntos, " +
              aciertos_jugador1, "◄◄◄")

    elif puntaje_final_1 < puntaje_final_2:
        print("\n \t\t\x1b[3;32m" + "►►► El ganador es:", jugador_2, "con", puntaje_final_2, "puntos, " +
              aciertos_jugador2, "◄◄◄")

    elif ronda_ganadaj1 < ronda_ganadaj2:
        print("\n \t\t\x1b[3;32m" + "►►► El ganador es:", jugador_2, "con", puntaje_final_2, "puntos, " +
              aciertos_jugador2, "◄◄◄")

    elif ronda_ganadaj1 > ronda_ganadaj2:
        print("\n \t\t\x1b[3;32m" + "►►► El ganador es:", jugador_1, "con", puntaje_final_1, "puntos, " +
              aciertos_jugador1, "◄◄◄")

    else:
        print("\n \t\t\x1b[3;32m" + "►►► Han empatado con:", puntaje_final_1, "puntos ◄◄◄")

# PRINT CANTIDAD DE JUGADAS

    print("\n \t\t\x1b[1;35m" + "Se hicieron", cantidad_jugadas, "jugadas en todo el juego.")

# VALIDACION Y PRINT DE EMPATE O DE NO EMPATE

    if empate:
        print("\n \t\t\x1b[2;33m" + "Hubo al menos una jugada con puntaje empatado entre ambos jugadores!!")
    else:
        print("\n \t\t\x1b[2;33m" + "No hubo ninguna jugada con puntaje empatado entre ambos jugadores")

# PRINTS DE PORCENTAJE PROMEDIO DE JUGADAS

    print("\n \t\t\x1b[3;35m" + "Porcentaje promedio de puntos por judada de", jugador_1 + ":",
          round((puntaje_final_1 / cantidad_jugadas), 2))

    print("\n \t\t\x1b[3;35m" + "Porcentaje promedio de puntos por jugada de", jugador_2 + ":",
          round((puntaje_final_2 / cantidad_jugadas), 2))

# PRINTS DE PORCENTAJE DE ACIERTOS

    print("\n \t\t\x1b[2;37m" + "Porcentaje de aciertos de", jugador_1 + ":", round((porcentaje_aciertos_1 * 100), 2),
          "%")

    print("\n \t\t\x1b[2;37m" + "Porcentaje de aciertos de", jugador_2 + ":", round((porcentaje_aciertos_2 * 100), 2),
          "%")

# VALIDACION DE SI ALGUIEN GANO 3 VECES SEGUIDAS Y PRINT

    if not gano_3_turnos_seguidos:
        print("\n \t\t\x1b[3;31m" + "Nadie ha ganado 3 turnos seguidos en ninguna ronda.")
    else:
        print("\n \t\t\x1b[3;31m" + "Uno de los jugadores gano 3 turnos seguidos en alguna de las rondas.")


# FUNCION PARA INICIAR EL JUEGO DE DADOS 2.0


def principal():
    print("\n\n\t\t🅹🆄🅴🅶🅾 🅳🅴 🅳🅰🅳🅾🆂", end = "\n\t\t➋.⓿")

    puntaje_final = int(input("\n \t\t\x1b[3;37m" + "\nLimite de puntaje maximo del juego: "))
    print("\n \t\t\x1b[3;37m" + "-" * 38)

# INVOCACION DE FUNCIONES PARA EJECUTAR EL JUEGO COMPLETO

    puntaje_de_corte = puntaje_del_juego(puntaje_final)

    jugador_1, jugador_2, puntaje_final_1, puntaje_final_2, cantidad_jugadas, empate, \
    ronda_ganadaj1, ronda_ganadaj2, aciertos_jugador1, aciertos_jugador2, \
    gano_3_turnos_seguidos, porcentaje_aciertos_1, porcentaje_aciertos_2 = juego_entero(puntaje_de_corte)

    salida_por_pantalla(jugador_1, jugador_2, puntaje_final_1, puntaje_final_2,
                        ronda_ganadaj1, ronda_ganadaj2, cantidad_jugadas, empate,
                        aciertos_jugador1, aciertos_jugador2, gano_3_turnos_seguidos,
                        porcentaje_aciertos_1, porcentaje_aciertos_2