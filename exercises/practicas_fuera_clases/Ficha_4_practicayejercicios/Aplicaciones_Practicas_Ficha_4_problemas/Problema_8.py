__author__ = "Wendler Juan Jose: "

# Cargar por teclado dos numeros enteros. Mostrarlos ordenados de menor a mayor

# PSEUDOCODIGO:
# 1. Cargar n1 > n2 dos numeros enteros
# 2. Si n1 > n2:
# 2.1 may = n1
# 2.2 men = n2
# 3 sino:
# 3.1 may = n2
# 3.2 men = n1
# 4. Mostrar men y may, en ese orden

n1 = int(input("Ingresar primer n°: "))
n2 = int(input("Ingresar segundo n°: "))

if n1 > n2:
    may = n1
    men = n2
else:
    may = n2
    men = n1

print("Numeros ordenados: ", men, "", may)
