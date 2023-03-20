# Inicio con sílaba "pa"

# Desarrollar un programa en Python que permita cargar por teclado
# un texto. El programa debe determinar:

# a) La cantidad de palabras que comienzan con la expresión "pa"
# y termina con la letra "n"
# c) La cantidad de palabras que presentan mas de dos vocales
# a partir de la tercera letra de la palabra
# d) El porcentaje que representa la cantidad de palabras del
# punto anterior respecto de la cantidad de total de palabras
# del texto
# e) Cantidad de palabras de mas de 5 letras


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra*100)/total, 2)
    return porc


def main():
    cant_pal_pa_n = cant_let_pal = cant_mas_5 = cant_mas2_voc = cant_vocales = cant_palabras = 0
    com_pa = fin_n = mas_de_5 = False

    texto = input("Ingrese el texto a ser procesado: ")
    for car in texto:
        if car == " " or car == ".":
            cant_palabras += 1

            if com_pa and fin_n:
                cant_pal_pa_n += 1
            if cant_vocales > 2:
                cant_mas2_voc += 1

            if mas_de_5:
                cant_mas_5 += 1

            cant_let_pal = cant_vocales = 0
            com_pa = False
            mas_de_5 = False
        else:

            cant_let_pal += 1

            if car == "a" and anterior == "p":
                com_pa = True

            if car == "n":
                fin_n = True
            else:
                fin_n = False

            if car in "aeiou":
                cant_vocales += 1

            if cant_let_pal > 5:
                mas_de_5 = True

            anterior = car

    print(f"Cantidad palabras comienzan con 'pa' y terminan con 'n': {cant_pal_pa_n}.")
    print(f"Cantidad de palabras con mas de '2' vocales: {cant_mas2_voc}.")
    print(f"El porcentaje de la cantidad de palabras con mas de '2' vocales"
          f" respecto al total de palabras del texto es {porcentaje(cant_mas2_voc, cant_palabras)}%.")
    print(f"La cantidad de palabras con mas de '5' letras es: {cant_mas_5}.")

if __name__ == "__main__":
    main()
