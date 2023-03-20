import random as psg

# ordenamiento por seleccion (select sort)
def ordenar_arreglo(v):
    tam = len(v)
    for i in range(tam-1):
        for j in range(i + 1, tam):
            if v[j] > v[i]:
                v[j], v[i] = v[i], v[j]


def test():
    flag_nota_6 = False
    cant_notas_mayor_6 = acu_calificaciones = 0

    vec = [0] * 7  # creo areglo con 7 elementos
    for i in range(len(vec)):
        vec[i] = psg.randint(-1, 10)  # grabando calificaciones desde -1;10

    print("Calificaciones: ", vec)
    ordenar_arreglo(vec)
    print("Arreglo ordenardo: ", vec)
    for i in range(len(vec)):
        acu_calificaciones += vec[i]
        if vec[i] == 6:
            flag_nota_6 = True
        elif vec[i] > 6:
            cant_notas_mayor_6 += 1

    diferencia = vec[0] - vec[-1] # diferencia entre mayor y menor

    if flag_nota_6:
        print("Existieron", cant_notas_mayor_6, "notas mayores a seis.")
    print("Diferencia entre mayor y menor puntaje: ", diferencia)
    print("Maximo en la lista: ", max(vec), end=" | ")
    print("Minimo en la lista: ", min(vec))
    print("Puntaje total obtenido: ", acu_calificaciones, ".", end="", sep="")
    if acu_calificaciones < 20:
        print("- Descalificados")

test()


