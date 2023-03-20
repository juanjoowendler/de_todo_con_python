__author__ = "Wendler Juan Jose"

# Primer ejercicio

print("Comparamos dos numeros: ")

a = int(input("-A: "))
b = int(input("-B: "))

if a > b:
    may = a
else:
    may = b


# Segundo ejercicio

print("\nEl mayor de los valores es: ", may)

n1 = int(input("\nN1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

if n1  > n2 and n1  > n3:
    mensaje = "\nEl primero es el mayor"
else:
    mensaje = "\nEl primero no es el mayor"

print(mensaje)


