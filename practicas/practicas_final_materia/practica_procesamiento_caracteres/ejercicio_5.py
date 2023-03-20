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


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra*100)/total, 2)

    return porc


def main():
    texto = input("Ingrese el texto a ser procesado: ")
    vocales = "aeiouAEIOU"

    cant_pal_ct_voc = cant_let_pal = cant_com_t_ant = cant_pal = 0
    com_voc = False
    term_ant = term_voc = ""

    for car in texto:
        if car == " " or car == ".":
            cant_pal += 1

            if com_voc and term_voc:
                cant_pal_ct_voc += 1

            cant_let_pal = 0
            com_voc = term_voc = False
        else:
            cant_let_pal += 1

            if cant_let_pal == 1 and car == term_ant:
                cant_com_t_ant += 1

            if car in vocales and cant_let_pal == 1:
                com_voc = True
            term_voc = False
            if car in vocales:
                term_voc = True

            term_ant = car

    print(f"Cantidad que comienzan y terminan en vocal: {cant_pal_ct_voc}.")
    print(f"{cant_com_t_ant} palabra\s comienzan con el caracter de la ultima palabra.")
    print(f"El porcentaje que representa a) sobre el total de palabras es: {porcentaje(cant_pal_ct_voc, cant_pal)}%.")


if __name__ == "__main__":
    main()
