__author__ = "Wendler Juan Jose: "

# Operaciones de orden con 3 nros:

# Realizar un programa que tome tres números, los ordene de mayor a
# menor, y diga si el tercero es el resto de la división de los dos primeros.

print("\t\tOrden de numeros del mayor al menor: ")
print("*"*50)
n1 = int(input("\nCargar el primer numero: "))
n2 = int(input("Cargar el segundo numero: "))
n3 = int(input("Cargar el segundo numero: "))

if n1 > n2:
    may = n1
    men = n2
else:
    may = n2
    men = n1

if n3 > may:
    may = n3
    med = may
else:
    if n3 > men:
        med = n3
    else:
        med = men
        men = n3

print("Menor: ", men)
print("Mediano: ", med)
print("Mayor: ", may)
