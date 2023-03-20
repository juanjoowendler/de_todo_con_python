__author__ = "Wendler Juan Jose"

# Para un análisis estadístico, se pide ingresar 3 valores y determinar:

# Si alguno de los valores es múltiplo de 5
# Cuántos de los valores son impares
# Si el mayor de ellos supera a la suma de los otros 2

val1 = int(input("Ingresar el primer valor: "))
val2 = int(input("Ingresar el segundo valor: "))
val3 = int(input("Ingresar el tercer valor: "))
imp_cant = 0

if val1 % 5 == 0 or val2 % 5 == 0 or val3 % 5 == 0:
   print("Alguno de los numeros es multiplo de 5.")
else:
    print("Ninguno es multiplo de 5.")


if val1 % 2 != 0:
    imp_cant += 1
if val2 % 2 != 0:
    imp_cant += 1
if val3 % 2 != 0:
    imp_cant += 1

# determino el mayor para calcular el punto 3

if val1 > val2 and val1 > val3:
    may = val1
    suma = val2 + val3
elif val2 > val1 and val2 > val3:
    may = val2
    suma = val1 + val3
else:
    may = val3
    suma = val1 + val2

if may > suma:
    print("El mayor de los valores supero la suma de los otros dos.")

print("La cantidad de valores impares es de: ", str(imp_cant) + ".")

