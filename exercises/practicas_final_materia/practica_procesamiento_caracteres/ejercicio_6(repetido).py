# # Silaba "ta"
# # El usuario ingresa una frase al comenzar el programa, la misma no
# # puede tener longitud cero. La frase finaliza con un punto, y las
# # palabras están separadas por espacios únicamente.
# # Se debe mostrar:
#
# # a) Ver el porcentaje de vocales respecto del total de letras de la frase.
# # b) La longitud promedio de las palabras
# # c) La longitud de la palabra mas larga del texto
# # d) Cantidad de palabras que comienzan con "ta"


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra * 100) / total, 2)

    return porc


def promedio(suma, total):
    prom = 0
    if total > 0:
        prom = round((suma/total), 2)

    return prom


def main():
    texto = input("Texto a analizar: ")

    cant_pal, cant_let_pal, cant_let, cant_vocales, mas_larga, longitud, cant_ta = 0, 0, 0, 0, 0, 0, 0
    vocales, anterior = "aeiou", ""
    for car in texto:
        if car == " " or car == ".":
            cant_pal += 1
            if longitud > mas_larga:
                mas_larga = longitud

            cant_let_pal = 0
        else:
            cant_let += 1
            cant_let_pal += 1

            longitud = cant_let_pal

            if car in vocales:
                cant_vocales += 1

            if cant_let_pal == 2 and car == "a" and anterior == "t":
                cant_ta += 1

            anterior = car

    print(f"a). {porcentaje(cant_vocales, cant_let)} %")
    print(f"b). {promedio(cant_let, cant_pal)}")
    print(f"c). {mas_larga}")
    print(f"d). {cant_ta}")


if __name__ == "__main__":
    main()
