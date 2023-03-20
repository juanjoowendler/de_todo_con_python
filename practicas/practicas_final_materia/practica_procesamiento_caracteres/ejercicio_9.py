# Con m y b
# Desarrollar un programa que permita ingresar por teclado,
# con palabras separadas por un espacio y terminado en punto.
# En base al texto ingresado, determinar:

# a) Cuántas palabras tienen una m y una b a partir de la tercer letra.
# b) Cuántas palabras comienzan con la letra p seguida de cualquier vocal.
# c) Cuántas palabras comienzan y terminan con el mismo carácter.

# **************************************************************
# Ejemplo: 'Mi amiga Ambar siempre piensa y cambia pronto.'
# **************************************************************
# Palabras tienen una m y una b a partir de la tercer letra: 1
# Palabras que comienzan con la letra p seguida de cualquier vocal: 1
# Palabras que comienzan y terminan con el mismo carácter: 2


def es_vocal(caracter):
    if caracter in "aeiou":
        return True
    return False


def main():
    texto = input("Ingrese el texto a ser procesado: ")
    anterior = primero = ultimo = ""
    cant_let_pal = cant_tiene_mb = cant_p_vocal = cant_com_term_ig = 0
    tiene_mb = p_vocal = False

    for car in texto:
        if car == " " or car == ".":
            ultimo = anterior

            if tiene_mb:
                cant_tiene_mb += 1

            if p_vocal:
                cant_p_vocal += 1

            if primero == ultimo:
                cant_com_term_ig += 1

            tiene_mb = p_vocal = False
            cant_let_pal = 0
        else:
            cant_let_pal += 1

            if cant_let_pal == 1:
                primero = car

            if cant_let_pal == 2 and es_vocal(car) and anterior == "p":
                p_vocal = True

            if cant_let_pal == 4:
                if car == "b" and anterior == "m":
                    tiene_mb = True

        anterior = car

    print()
    print(f"Cantidad de palabras que tienen 'mb' a partir de la 3(er) letra: {cant_tiene_mb}")
    print(f"Cantidad de palabras seguidas de vocal que comienzan con 'p': {cant_p_vocal}")
    print(f"Cantidad de palabras con la ultima letra igual a la primera: {cant_com_term_ig}")


if __name__ == "__main__":
    main()
