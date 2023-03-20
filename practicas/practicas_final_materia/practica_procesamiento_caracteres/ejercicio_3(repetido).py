# # Inicio con sílaba "pa"
#
# # Desarrollar un programa en Python que permita cargar por teclado
# # un texto. El programa debe determinar:
#
# # a) La cantidad de palabras que comienzan con la expresión "pa"
# # y termina con la letra "n"
# # b) La cantidad de palabras que presentan mas de dos vocales
# # a partir de la tercera letra de la palabra
# # c) El porcentaje que representa la cantidad de palabras del
# # punto anterior respecto de la cantidad de total de palabras
# # del texto
# # d) Cantidad de palabras de mas de 5 letras


def main():
    texto = input("Ingrese el texto: ")

    com_pa, vocal_en_tercera, mas_5 = False, False, False
    anterior, vocales = "", "aeiou"
    cant_let_pal, cant_com_pa, cant_voc, cant_pal = 0, 0, 0, 0
    punto_a, punto_b, punto_c, punto_d = 0, 0, 0, 0
    for car in texto:
        if car == " " or car == ".":
            cant_pal += 1

            if com_pa and anterior == "n":
                punto_a += 1

            if cant_voc > 2:
                punto_b += 1

            if mas_5:
                punto_d += 1

            cant_let_pal = cant_voc = 0
            com_pa, vocal_en_tercera, mas_5 = False, False, False
        else:
            cant_let_pal += 1
            if cant_let_pal == 2 and car == "a" and anterior == "p":
                com_pa = True

            if vocal_en_tercera and car in vocales:
                cant_voc += 1

            if cant_let_pal == 3 and car in vocales:
                vocal_en_tercera = True
                cant_voc += 1

            if cant_let_pal > 5:
                mas_5 = True

        anterior = car

    if cant_pal > 0:
        punto_c = round(((punto_b*100)/cant_pal), 2)

    print(f"a). {punto_a}")
    print(f"b). {punto_b}")
    print(f"c). {punto_c} %")
    print(f"d). {punto_d}")


if __name__ == "__main__":
    main()
