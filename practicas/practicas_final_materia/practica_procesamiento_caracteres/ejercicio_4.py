# Sílaba "pe"
# Se pide desarrollar un programa en Python que permita cargar
# por teclado un texto completo en una variable de tipo cadena
# de caracteres.  El programa debe:

# a) Determinar cuántas palabras tienen 3, 5 o 7 letras.
# b) Determinar la cantidad de palabras con más de tres
# letras, que tienen una vocal en la tercera letra.
# c) Determinar el porcentaje de palabras que tienen sólo una o
# dos vocales sobre el total de palabras del texto.
# d) Determinar la cantidad de palabras que contienen más de
# una vez la sílaba "pe".


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra * 100)/total, 2)

    return porc


def main():
    vocales = "aeiouAEIOU"
    cant_let_pal = cant_pal_pe = cant_pal_con357 = cant_pe = cant_palabras = cant_mas3yvocal = cant_vocales = cant_1o2_voc = 0
    cumple_pb = False

    texto = input("Ingrese el texto a ser procesado: ")
    for car in texto:
        if car == " " or car == ".":
            cant_palabras += 1

            if cant_let_pal in [3, 5, 7]:
                cant_pal_con357 += 1

            if cumple_pb:
                cant_mas3yvocal += 1

            if cant_vocales in [1, 2]:
                cant_1o2_voc += 1

            if cant_pe > 1:
                cant_pal_pe += 1

            cant_let_pal = cant_vocales = cant_pe = 0
            cumple_pb = False

        else:
            cant_let_pal += 1
            if cant_let_pal == 3 and car in vocales:
                cumple_pb = True

            if car in vocales:
                cant_vocales += 1

            if car == "e" and anterior == "p":
                cant_pe += 1

            anterior = car

    print(f"La cantidad de palabras con '3,5,7' letras es de: {cant_pal_con357}.")
    print(f"La cantidad de palabras con mas de '3' y que tienen "
          f"una vocal en la 3(ra) es de: {cant_mas3yvocal}.")
    print(f"Porcentaje de palabras con solo '1 ó 2' vocales respecto a "
          f"al total de palabras del texto es de: {porcentaje(cant_1o2_voc, cant_palabras)}%.")
    print(f"La cantidad de palabras que contienen mas de una vez la silaba 'pe' "
          f"es de: {cant_pal_pe}.")


if __name__ == "__main__":
    main()
