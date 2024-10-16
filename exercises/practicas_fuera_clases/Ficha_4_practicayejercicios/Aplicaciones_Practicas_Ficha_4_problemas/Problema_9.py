__author__ = "Wendler Juan Jose"

# Cargar por teclado 3 numeros enteros. Determinar si el primero que se cargo
# es el mayor de los 3

# PSEUDOCODIGO:
# 1. Cargar n1, n2 y n3
# 2. Si n1 > n2 and n1 > n3:
# 2.1 mensaje = "El primero es el mayor."
# 3. else:
# 3.1 mensaje = "El primero no es el mayor."
# 4. Mostrar el mensaje

n1 = int(input("Primer n°: "))
n2 = int(input("Segundo n°:"))
n3 = int(input("Tercer n°: "))

if n1 > n2 and n1 > n3:
    mensaje = "El primero es el mayor."
else:
    mensaje = "El primero no es el mayor."

print("Conclusion: ", mensaje)
