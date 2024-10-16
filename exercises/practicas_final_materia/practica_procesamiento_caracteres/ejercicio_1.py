# Desarrollar un programa en Python que permita cargar por teclado un texto
# completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena
# de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a
# través de un while). Siempre se supone que el usuario cargará un punto para indicar el final
# del texto, y que cada palabra de ese texto está separada de las demás por un espacio en
# blanco.

# El programa debe:

# a. Determinar cuántas palabras se cargaron.
# b. Determinar cuántas palabras comenzaron con la letra "p".
# c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta".

def main():
    cant_palabras = cant_letras = cant_comenzaron_p = cant_pal_ta = 0
    hay_ta = False
    t = input("Ingrese el texto a procesar (finaliza con punto '.'): ")

    for car in t:
        cant_letras += 1

        if car == " " or car == ".":
            # palabra (termino)
            cant_palabras += 1
        if hay_ta:
            cant_pal_ta += 1
            hay_ta = False

        else:
            # dentro de la palabra (no termino)
            if car == "p" and (cant_letras == 1 or t[cant_letras-2] == " "):
                cant_comenzaron_p += 1
            if car == "a" and (cant_letras > 1 and [cant_letras-2] == "t"):
                hay_ta = True

    print(f"La cantidad de palabras es {cant_palabras}.")
    print(f"La cantidad de palabras que comienzan con 'p' es {cant_comenzaron_p}.")
    print(f"La cantidad de palabras con 'ta' es {cant_pal_ta}.")


if __name__ == "__main__":
    main()
