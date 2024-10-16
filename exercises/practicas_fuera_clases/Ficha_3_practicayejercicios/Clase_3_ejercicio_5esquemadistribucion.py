__author__ = "Wendler Juan Jose"

#   una oficina de correos dispone de 5 casillas para guardad cartas
#   c/u de las casillas puede contener muchas cartas;
#   esta enumerada con numeros correlativos del 0 al 4. Cada carta
#   que se recibe tiene un codigo postal numerico, y en base a eses codigo
#   el despachante debe determinar en que box guardara la carta, pero de tal forma
#   que el mismo sistema sirva luego para saber en que caja buscar la carta, dado su
#   codigo postal de tres cartas y mostrando en que casilla sera alacenada c/u

# PSEUDOCODIGO
# 1. Sea n = 5
# 2. Cargar c1,c2,c3 (codigos postales de las 3 cartas)
# 3. Sea c1 = % n
# 4. Sea c2 = % n
# 5. Sea c3 = % n
# 6. Mostrar n1, n2, n3 (numeros de los casilleros)
print("\tAsignacion de casillas por codigo postal: ")
n = 5
c1 = int(input("\n- Codigo postal de la primera carta: "))
c2 = int(input("- Codigo postal de la segunda carta: "))
c3 = int(input("- Codigo postal de la tercera carta: "))

n1 = c1 % n
n2 = c2 % n
n3 = c3 % n

print("\nCodigo postal: ", c1, "\tasignado a la casilla n°", n1)
print("Codigo postal: ", c2, "\tasignado a la casilla n°", n2)
print("Codigo postal: ", c3, "\tasignado a la casilla n°", n3)
