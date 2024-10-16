__author__ = "Wendler Juan Jose"

# Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas
# por sus vendedores, para ello le solicita un sistemita que le permita calcular dicho montos.

# Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4).
# Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta
# (el proceso termina cuando se ingrese una categoría igual a cero) y acumular las comisiones
# de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:

# a) Categoría 1: cobra una comisión de 10%
# b) Categoría 2: cobra una comisión de 25%
# c) Categoría 3: cobra una comisión de 30%
# d) Categoría 4: cobra una comisión de 40%

# Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría
# de vendedores que tiene la empresa junto con el total general

print("\n\t\t\tComisión de Vendedores: ")
print("-" * 60)

ven_tt = 0
# acumulador de la cantidad de comisiones
cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
# acumulador general
acu_com = 0
# inicio del ciclo
cat = int(input("Ingresar la categoria del vendedor, (1-4): "))

while cat != 0 and cat <= 4:
    ven_tt = float(input("Ingresar el total de la venta: "))
    if cat == 1:
        cat1 = ven_tt * 0.10
    else:
        cat1 += 0
    if cat == 2:
        cat2 = ven_tt * 0.25
    else:
        cat2 += 0
    if cat == 3:
        cat3 = ven_tt * 0.30
    else:
        cat3 += 0
    if cat == 4:
        cat4 = ven_tt * 0.40
    else:
        cat4 += 0
    cat = int(input("\nIngresar otra categoria del vendedor, (1-4): "))
    acu_com = cat1 + cat2 + cat3 + cat4
else:
    print("\nfin del programa...")

print("\n\t-El total de comisiones a pagar por cada categoria es de: ")
print("\n\t\tComision 1: ", cat1, "\tComision 2: ", cat2, "\n\t\tComision 3: ", cat3, "\tComision 4: ", cat4)
print("\n\t-El total general de todas las comisiones es de: ", str(acu_com) + "$.")



