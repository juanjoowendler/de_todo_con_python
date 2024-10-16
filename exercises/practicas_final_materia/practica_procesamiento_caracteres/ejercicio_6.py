# Silaba "ta"
# El usuario ingresa una frase al comenzar el programa, la misma no
# puede tener longitud cero. La frase finaliza con un punto, y las
# palabras están separadas por espacios únicamente.
# Se debe mostrar:

# a) Ver el porcentaje de vocales respecto del total de letras de la frase.
# b) La longitud promedio de las palabras
# c) La longitud de la palabra mas larga del texto
# d) Cantidad de palabras que comienzan con "ta"


def c_porcentaje(muestra, total):
    porcentaje = 0
    if total > 0:
        porcentaje = round((muestra * 100) / total, 2)

    return porcentaje


def main():
    texto = ""
    while len(texto) == 0:
        texto = input("Ingrese texto a ser procesado: ")
        if len(texto) == 0:
            print("No puede ser de longitud cero...")
            print()

    cant_palabras = cant_com_ta = may = cant_vocales = cant_letras = cant_let_pal = 0
    con_ta = False
    anterior = ""

    for car in texto:
        if car == " " or car == ".":
            cant_palabras += 1

            if con_ta:
                cant_com_ta += 1

            cant_let_pal = 0
            con_ta = False
        else:
            cant_letras += 1
            cant_let_pal += 1
            if cant_let_pal > may:
                may = cant_let_pal

            if car in "aeiouAEIOU":
                cant_vocales += 1

            if car == "a" and anterior == "t":
                con_ta = True

            anterior = car

    promedio = 0
    if cant_palabras != 0:
        promedio = round((cant_letras / cant_palabras), 2)

    print(f"Punto a): {c_porcentaje(cant_vocales, cant_letras)}%.")
    print(f"Punto b): {promedio}.")
    print(f"Punto c): {may}.")
    print(f"Punto d): {cant_com_ta}.")


if __name__ == "__main__":
    main()
