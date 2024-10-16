# Desarrollar un programa que permita ingresar por teclado, con palabras separadas 
# por un espacio y terminado en punto. En base al texto ingresado, determinar:

# a) Cuál es la longitud de la palabra más larga. 

# b) Cuántas palabras tienen la a como única vocal OK 

# c) Qué porcentaje representan las que sólo tienen la vocal a sobre el total de palabras. OK


def es_vocal(car):
    if car in "aeiou":
        return True
    return False


def porcentaje(cantidad, total):
    porcentaje = 0
    if total != 0:
        porcentaje = round((cantidad * 100) / total, 2)
        porcentaje = str(porcentaje)
    return porcentaje


def test():
    input("\nPresiona cualquier tecla para comenzar...")
    # inicializar variables
    ban_a = False
    ban_eiou = False
    cont_a = 0
    cl = 0
    cp = 0

    texto = input("Ingresar texto a ser procesado: ")
    texto.lower()
    for car in texto: 
        if car != " " and car != ".":
            # letras
            cl += 1
            if es_vocal(car):
                if car == "a":
                    ban_a = True
                else:
                    ban_eiou = True   
        else:
            # fin de palabra
            cp += 1
            if ban_a and not ban_eiou: 
                cont_a += 1

            ban_eiou = False 
            ban_a = False
            
      
    print("\t-Cantidad de palabras que tienen la 'a' como unica vocal: ", str(cont_a) + ".")
    print("\t-Porcentaje de las que tienen vocal 'a' por sobre el total de palabras: ", porcentaje(cont_a, cp) + " %")

                                                          
if __name__ == "__main__":
    test() 

