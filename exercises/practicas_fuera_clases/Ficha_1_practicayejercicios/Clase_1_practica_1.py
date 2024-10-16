__author__ = "Wendler Juan Jose"

print("División con resto: ")

# Plantear un script (directamente en el shell de Python) que
# permita informar, para dos valores a y b el
# resultado de la división a/b y el resto de esa divisón.


a = float(input("Ingresar el primer numero: "))
b = float(input("Ingresar el segundo numero: "))

div, rest = a/b, a % b

print("-cociente: ", round(div,3), "-resto: ", round(rest,3))
