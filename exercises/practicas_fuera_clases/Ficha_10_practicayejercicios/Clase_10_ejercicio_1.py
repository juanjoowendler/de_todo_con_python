__author__ = "Wendler Juan Jose"

def es_vocal(car):
    res = False
    if car in "aeiou":
        res = True
    return res

def porcentaje(subtotal, total):
    if total > 0:
        porc = subtotal * 100 / total
        round(porc)
    else:
        porc = 0
    return porc


ban_a = ban_eiou = False
cont_a = c_pal = c_let = may =  0
texto = input("Ingresar texto a procesar: ")
for car in texto:
    if car != " " and car != ".":
        c_let += 1
        if es_vocal(car):
            if car == "a":
                ban_a = True # T
            else:
                ban_eiou = True # F
        else:
            # fin de palabras
            c_pal += 1
            if ban_a and not(ban_eiou):
                cont_a += 1
            if c_pal == 1 or c_let > may:
                may = c_let
            else:
                if c_let > may:
                    may = c_let

        ban_a = ban_eiou = False
        clet = 0

p = porcentaje(cont_a, c_pal)

print("Longitud de la palabra mas larga", may)
print("Palabras con solo 'a' como vocal: ", cont_a)
print("Porcentaje que representan: ", str(porcentaje) + "%")


