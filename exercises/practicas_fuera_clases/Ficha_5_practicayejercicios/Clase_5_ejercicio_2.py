__author__ = "Wendler Juan Jose"

# Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente
#                   se eligen de acuerdo a las siguientes reglas:

# Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento
# (45 %) de los votos afirmativos válidamente emitidos; en su defecto, aquella que hubiere
# obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmativos válidamente
# emitidos y, además, existiere una diferencia mayor de diez puntos porcentuales respecto
# del total de los votos afirmativos válidamente emitidos, sobre la fórmula que le sigue
# en número de votos.
#
# Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo
# al escrutinio ejecutado por las Juntas Electorales, y cuyo resultado único para toda
# la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el artículo
# 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días.
#
# Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas
# en la primera, resultando electa la que obtenga mayor número de votos afirmativos válidamente emitidos.
#
# Desarrollar un programa que permita ingresar, para los 3 partidos más votados:
# fórmula (presidente + vice) y cantidad de votos obtenidos.
#
#                           Luego determinar:
#
# Qué fórmula obtuvo el mayor porcentaje.
# Si la fórmula resulta elegida o se requiere segunda vuelta.
# En este caso, indicar también quienes participan de la segunda vuelta.

print("Elecciones Presidenciales: ")

print("*" * 50)
print("\nPrimera vuelta: ")

p1_form = input("\nIngresar formula del partido 1: ")
p1_cant = int(input("Ingresar la cantidad de votos obtenidos: "))
p2_form = input("Ingresar formula del partido 1: ")
p2_cant = int(input("Ingresar la cantidad de votos obtenidos: "))
p3_form = input("Ingresar formula del partido 1: ")
p3_cant = int(input("Ingresar la cantidad de votos obtenidos: "))

cant_v = p1_cant + p2_cant + p3_cant
p1_porc = (p1_cant * 100) / cant_v
p2_porc = (p2_cant * 100) / cant_v
p3_porc = (p3_cant * 100) / cant_v

f1 = False
f2 = False
f3 = False

diferencia = p1_cant - p2_cant - p3_cant
dif_porc = (diferencia * 100) / cant_v

if p1_porc > 40 and dif_porc > 10:
    electa = p1_form
else:
    if p2_porc > 40 and dif_porc > 10:
        electa = p2_form
    else:
        if p3_porc > 40 and dif_porc > 10:
            electa = p3_form


if p1_porc < 40 and dif_porc < 10 or p2_porc < 40 and dif_porc < 10 or p3_porc < 40 and dif_porc < 10:
    print("Ningun partido alcanzo los minimos requisitos, por el A.150 se hara la segunda vuelta.")


    if p1_cant > p2_cant and p1_cant > p3_cant:
        may = p1_cant
        f1 = True
        if p2_cant > p3_cant:
            men = p3_cant
            med = p2_cant
            f2 = True
        else:
            men = p2_cant
            med = p3_cant
            f3 = True
    else:
        if p2_cant > p1_cant and p2_cant > p3_cant:
            may = p2_cant
            f2 = True
            if p1_cant > p3_cant:
                men = p3_cant
                med = p1_cant
                f1 = True
            else:
                men = p1_cant
                med = p3_cant
                f3 = True
        else:
             may = p3_cant
             f3 = True
             if p1_cant > p2_cant:
                 men = p2_cant
                 med = p1_cant
                 f1 = True
             else:
                 men = p1_cant
                 med = p2_cant
                 f2 = True

        if f1 and f2:
            print("Participaran el primer y segundo partido.")
        else:
            if f1 and f3:
                print("Parciciparan el primer y el tercer partido.")
            else:
                if f2 and f3:
                    print("Participaran el segundo y tercer partido.")


    print("La formula que obtuvo el mayor porcentaje fue: ", electa, "con un",
        max(round(p1_porc, 2), round(p2_porc, 2), round(p3_porc, 2)), "%.")
    print("La formula elegida fue: ", str(electa) + ".")
