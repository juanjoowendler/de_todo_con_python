# 1. Sílaba "mo"
#  Desarrollar un programa en Python que permita cargar por teclado un texto completo

#  El programa debe:
# a) Determinar cuántas palabras tenían más de 4 letras.
# b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".
# c) Determinar el promedio de letras por palabra en todo el texto.
# d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

# Ejemplo: 'el mono momoxy toca el xilofon.'

# Palabras con más de 4 letras: 2
# Palabras tenían al menos una vez la letra "x" o la letra "y": 2
# El promedio de letras por palabra en todo el texto es: 4.17
# Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1

def promedio(suma, cantidad):
    if cantidad == 0:
        promedio = 0

    else:
        promedio = round(suma/cantidad, 2)

    return promedio


def main():
    cant_letras_pal = cant_palabras_mo = cant_mo = cant_pal_mas_4 = cant_pal_xoy = cant_letras = cant_palabras = 0
    hay_xoy = False
    texto = input("Ingrese el texto a ser procesado: ")
    for car in texto:

        if car == " " or car == ".":
            cant_palabras += 1

            if cant_letras_pal > 4:
                cant_pal_mas_4 += 1
            if hay_xoy:
                cant_pal_xoy += 1
            if cant_mo == 2:
                cant_palabras_mo += 1

            cant_letras_pal = 0
            hay_xoy = False
            cant_mo = 0
        else:

            cant_letras += 1
            cant_letras_pal += 1
            if car in "xy":
                hay_xoy = True
            if car == "o" and anterior == "m":
                cant_mo += 1

            anterior = car

    print(f"La cantidad de palabras con mas de 4 letras es de: {cant_pal_mas_4}.")
    print(f"La cantidad de palabras con al menos la letra 'x' ó 'y' es: {cant_pal_xoy}.")
    print(f"El promedio de letras por palabra de todo el texto es: {promedio(cant_letras, cant_palabras)}")
    print(f"La cantidad de palabras que tienen solo una vez 'mo' es: {cant_palabras_mo}.")


if __name__ == "__main__":
    main()
