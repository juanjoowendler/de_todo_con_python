# Sílaba "dre"
# Desarrollar un programa en Python que permita cargar por
# teclado un texto completo. Siempre se supone que el usuario
# cargará un punto para indicar el final del texto, y que cada
# palabra de ese texto está separada de las demás por un espacio en blanco.
# El programa debe:

# a) Determinar cuántas palabras tenían exactamente 3 letras.
# b) Determinar el porcentaje que las palabras del punto 1 representan
# en el total del palabras del texto.
# c) Determinar cuántas palabras terminaban con la letra "s".
# d) Determinar cuántas palabras contuvieron al menos una vez la expresión "dre".


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra*100)/total, 2)
    return porc


def main():
    texto = input("Ingrese el texto a ser procesado: ")

    cant_let_pal = cant_pal_dre = cant_pal_term_s = cant_solo_3 = cant_pal = 0
    solo_3 = term_s = ban_dre = ban_dr = False
    anterior = ""

    for car in texto:
        if car == " " or car == ".":
            cant_pal += 1

            if solo_3:
                cant_solo_3 += 1

            if term_s:
                cant_pal_term_s += 1

            if ban_dre:
                cant_pal_dre += 1

            cant_let_pal = 0
            solo_3 = term_s = ban_dre = ban_dr = False
        else:
            cant_let_pal += 1

            solo_3 = False
            if cant_let_pal == 3:
                solo_3 = True

            term_s = False
            if car == "s":
                term_s = True

            if car == "r" and anterior == "d":
                ban_dr = True
            else:
                if ban_dr and car == "e":
                    ban_dre = True

                ban_dr = False

            anterior = car

    print(f"Cantidad de palabras con solo '3' letras: {cant_solo_3}")
    print(f"Porcentaje de solo '3' letras respecto al total de palabras: {porcentaje(cant_solo_3, cant_pal)} %")
    print(f"Cantidad de palabras que terminan con 's': {cant_pal_term_s}")
    print(f"Cantidad de palabras que contienen 'dre': {cant_pal_dre}")


if __name__ == "__main__":
    main()
