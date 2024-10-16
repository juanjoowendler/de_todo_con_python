# Inicio y fin con vocal
# Se solicita crear un programa que permita ingresar un texto,
# las palabras se encontrarán separadas únicamente por espacios
# en blanco y el mismo debe finalizar con un punto.
# En base a ese texto determinar:
#
# a) La cantidad de palabras que comienzan y terminan en vocal
# b) La cantidad de palabras que comienzan con la misma letra
# que terminó la palabra anterior
# c) El porcentaje que representa el punto a) sobre el total de
# palabras del texto


def es_vocal(car):
    """
    :param car: caracter de texto a procesar
    :return: valor boolean
    """
    if car in "aeiou":
        return True
    return False


def porcentaje(cantidad, total):
    """
    :param cantidad: cantidad palabras comprendidas en a)
    :param total: total de palabras de toda la cadena
    :return: porcentaje comprendido
    """
    porc = 0
    if total != 0:
        porc = ((cantidad*100)/total)

    if porc > 0:
        round(porc, 2)

    return porc


def main():
    texto = ""
    while len(texto) == 0:
        texto = input("Ingrese la cadena a procesar: ")

    anterior_car, primer_letra = "", ""
    cant_com_ter_voc, cant_let_pal, cant_com_ter_ant, cant_total_palabras = 0, 0, 0, 0
    primer_vocal = False
    for car in texto:
        if car == " " or car == ".":
            cant_total_palabras += 1

            if primer_vocal and es_vocal(anterior_car):
                cant_com_ter_voc += 1

            primer_vocal = False
            cant_let_pal = 0
        else:
            cant_let_pal += 1

            if anterior_car == car and cant_let_pal == 1:
                cant_com_ter_ant += 1

            if cant_let_pal == 1 and es_vocal(car):
                primer_vocal = True

            anterior_car = car

    print(f"Comienzan y terminan en vocal: {cant_com_ter_voc}.") # bien
    print(f"Comienzan con la letra que termino la anterior palabra: {cant_com_ter_ant}.") # bien
    print(f"El porcentaje que representa sobre el total de palabras es de: {porcentaje(cant_com_ter_voc, cant_total_palabras)} %.") # bien


if __name__ == "__main__":
    main()
