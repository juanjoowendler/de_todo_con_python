__author__ = "Wendler Juan Jose"

#   La fuerza de atraccion entre dos masas m1 y m2 separadas por una distancia d,
#   esta dada por la siguiente formula de la mecanica clasica:
#                                   f = g (m1 * m2 / d^2)
#                                   -con g = 6.673 * 10^-8

#   Escribir un script que cargue las masas m1 y m2 de dos cuerpos
#   y la distancia d entre ellos y obtenga y muestre el valor de
#   la intensidad  de la fuerza de atraccion entre esos cuerpos

# PSEUDOCODIGO:
# 1. Con g = 6.673 * 10^-8
# 2. Cargar la m1 (masa 1)
# 3. Cargar la m2 (masa 2)
# 4. Cargar d (distancia entre ellos)
# 5. Con f = (g * m1 * m2) / d^2
# 6. Mostrar resultados

g = 6.673 * pow(10,-8)
m1 = float(input("Primer masa: "))
m2 = float(input("\nSegunda masa: "))
d = float(input("\nIngresar la distancia aproximada entre m1 y m2: "))

f = ((g * (m1 * m2))/d**2)

print("\t\nla fuerza de atraccion es de: ", f)



