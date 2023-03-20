__author__ = "Wendler Juan Jose"

print("Rinde de un Campo Agricola: ")

# Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela. Se pide ingresar el
# largo y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.

largo = int(input("Ingresar el largo de la parcela: "))
ancho = int(input("Ingresar el ancho de la parcela: "))

# 2 quintales = 10m^2

area_parcela = largo * ancho

quintales = area_parcela * 2 // 10 # entero porque es un terreno

print("La cantidad de quintales sera: ", str(quintales) + ".")


