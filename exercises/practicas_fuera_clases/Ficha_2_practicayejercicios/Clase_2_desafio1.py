__author__ = "Wendler Juan Jose"

print("CUADRADOS Y CUBOS: ")

# Leer dos numeros y calcular:
#   1. la suma de sus cuadrados
#   2. el promedio de sus cubos

#   Asignacion...
n1 = float(input("\t\nPrimer numero: "))
n2 = float(input("Segundo numero: " ))

#   Proceso/presentacion...
ca, cb = n1**2, n2**2
sum = ca + cb
print("\n\t- La suma de sus cuadrados es: ", sum )
cu1, cu2 = n1**3, n2**3
print("\nDe los valores anteriores tenemos...")
prom = (cu1 + cu2) // 2
print("\n\t-El promedio de sus cubos es de: ", prom)










