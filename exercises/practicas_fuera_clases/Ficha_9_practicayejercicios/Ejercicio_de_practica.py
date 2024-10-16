__author__ = "Wendler Juan Jose"


# Desarrollar un programa en Python que permita cargar por teclado un texto completo.
# Siempre se supone que el usuario cargará un punto para indicar el final del texto,
# y que cada palabra de ese texto está separada de las demás por un espacio en blanco.

# El programa debe:

# a) Determinar cuántas palabras tenían más de 4 letras.
# b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".
# c) Determinar el promedio de letras por palabra en todo el texto.
# d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".


clet = cpal = 0
acu = cpal4 = cpalxy = cmo = cpalmo = 0
bxy = bm = False

texto = input("Ingrese un texto a ser procesado: ")

for car in texto:
    if car != " " and car != ".":
        # letras de palabras
        clet += 1
        if car == "x" or car == "y":
            bxy = True
        if car == "m":
            bm = True
        else:
            if car == "o" and bm:
                cmo += 1
            bm = False

    else:
        # fin de palabra
        if clet > 0:
            cpal += 1
            acu += clet
        if clet > 4:
            cpal4 += 1
        if bxy:
            cpalxy += 1
        if cmo == 1:
            cpalmo += 1

        clet = cmo = 0
        bxy = bm = False

if cpal != 0:
    prom = acu / cpal
else:
    prom = 0

print("Promedio de letras por palabras: ", str(prom) + ".")
print("Cantidad de palabras con mas de 4 letras: ", str(cpal4) + ".")
print("Cantidad de palabras con 'x o y': ", str(cpalxy) + ".")
print("Cantidad de palabras con la expresion 'mo': ", str(cpalmo) + ".")


