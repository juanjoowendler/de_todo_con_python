__author__ = "Wendler Juan Jose"

print("Palabra con la silaba 'mo'")

letras_pal = 0
palabras_mas4 = 0
tieneXY = False
palabras_XY = 0
letras = 0
palabras = 0
anterior = None
cantMO = 0
palabras_MO = 0

texto = input("Ingresar texto a ser procesada: ")

while texto[-1] != ".":
    print("Debe finalizar con un punto, ingrese nuevamente...", end=" ")
    texto = input("Ingresar nuevamente un texto: ")
else:
    for letra in texto:
        if letra == " " or letra == ".":
            if letras_pal > 4:
                palabras_mas4 += 1
            if tieneXY == True:

