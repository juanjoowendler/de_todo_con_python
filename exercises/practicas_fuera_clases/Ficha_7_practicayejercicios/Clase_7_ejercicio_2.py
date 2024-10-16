__author__ = "Wendler Juan Jose"

# Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos,
# en forma ascendente y descendente.

print("\t\tSecuencia de impares: ")
print("-" * 40)

a = int(input("\nPrimer numero: "))
b = int(input("Segundo numero: "))

while a == b == 0:
    print("-No se pueden ingresar dos ceros, intente nuevamente...")
    a = int(input("\nPrimer numero: "))
    b = int(input("Segundo numero: "))

print("\n----Ascendente----")
for i in range(a, b+1):
    if i % 2 != 0:
        print("i.- impar: ", i, end=" |")

print("\n----Descendente----")
for i in range(b, a-1, -1):
    if i % 2 != 0:
        print("i.- impar: ", i, end=" |")




