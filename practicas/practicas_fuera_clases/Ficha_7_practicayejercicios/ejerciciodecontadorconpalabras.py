__author__ = "Wendler Juan Jose"


print("Contador total de palabras")

# contador total de letras por palabra...
cl = 0
# contador total de palabras...
ctp = 0
# contador de palabras que empiezan con "p"...
cpp = 0
# contador de palabras que tienen la expresion "ta"...
cta = 0
# señal para avisar el paso de una letra "t"...
letra_t = False
# señal para avisar que se formo la secuencia "ta"...
sec_ta = False

# carga del texto completo
cadena = input("Cargue el texto (termine con un punto): ")

# ciclo iterador para procesar el texto...
for car in cadena:

    # contar las letras de la palabra actual...
    cl += 1

    # es final de palabra?
    if car == " " or car == ".":
        # si... entonces analizar lo que paso con la palabra que termino...
        # a. contar palabras del texto...
        if cl > 1:
            ctp += 1

        # c. contar palabras con "ta"...
        if sec_ta == True: # se podria poner solo sec_ta
            cta += 1

        # volver a cero el contador de letras...
        cl = 0

        # apagar las señales del detector de "ta"...
        sec_ta = False
        letra_t = False

    else:
        # no... entonces tengo una letra y estoy dentro de la palabra actual
        # b. contar las palabras que empiezan con "p" ...
        if car in "pP" and cl == 1:
            cpp += 1

        # c. detectar la secuencia "ta"
        if car == "t" or "T":
            letra_t = True
        else:
            if (car == "a" or "A") and (letra_t == True): # se podria escribir solo letra_t
                sec_ta = True
            letra_t = False


# resultados finales...
print("1. Cantidad total de palabras: ", ctp)
print("2. Cantidad de palabras que empiezan con 'p': ", cpp)
print("3. Cantidad de palabras con la expresion 'ta': ", cta)


