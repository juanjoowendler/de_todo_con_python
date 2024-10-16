# Solamente 'a'
# Desarrollar un programa que permita ingresar por teclado, con
# palabras separadas por un espacio y terminado en punto.
# En base al texto ingresado, determinar:

# a) Cuál es la longitud de la palabra más larga.
# b) Cuántas palabras tienen la a como única vocal
# c) Qué porcentaje representan las que sólo tienen la
# vocal a sobre el total de palabras.
# ********************************************************************************
# Ejemplo: "el agua clara salta por las piedras."
# La longitud de la palabra más larga es 7 letras
# Las palabras cuya única vocal es la a son: 3
# El porcentaje de estas palabras sobre el total es 43 %


def porcentaje(muestra, total):
    porc = 0
    if total > 0:
        porc = round((muestra*100)/total, 0)

    return porc


def main():
    texto = input("Ingrese el texto a ser procesado: ")

    cant_let_pal = cant_pal_a_unica = may = cant_pal = 0
    ban_a = ban_eiou = False

    for car in texto:
        if car == " " or car == ".":
            cant_pal += 1

            if cant_let_pal > may:
                may = cant_let_pal

            if ban_a and not ban_eiou:
                cant_pal_a_unica += 1

            ban_a = ban_eiou = False
            cant_let_pal = 0
        else:
            cant_let_pal += 1

            if car == "a":
                ban_a = True

            if car in "eiou":
                ban_eiou = True

            may = cant_let_pal

    print(f"La longitud de la palabra mas larga es de: {may} letras")
    print(f"Cantidad de palabras con la 'a' como unica vocal: {cant_pal_a_unica}")
    print(f"El porcentaje de las que solo tienen 'a' sobre el total "
          f"de palabras es: {porcentaje(cant_pal_a_unica, cant_pal)} %")


if __name__ == "__main__":
    main()
