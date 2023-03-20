"""
Creacion de una matriz de forma manual y variantes:

"""

mo = [
    [2, 3, 1],
    [4, 6, 5],
    [5, 7, 0]
    ]

print("Matriz generada de forma mas clara: ", mo, end="\n\n")

mo = [[2, 3, 1], [4, 6, 5], [5, 7, 0]]

print("Matriz generada de forma compacta: ", mo, end="\n\n")


n, m = 3, 4
mo = []
for f in range(n):
    mo.append([])
    for c in range(m):
        mo[f].append(None)

print("Matriz generada tipo 1): ", mo, end="\n\n")

n, m = 3, 4
mo = [None] * n
for f in range(n):
    mo[f] = [None] * m

print("Matriz generada tipo 2):", mo, end="\n\n")

n, m = 3, 4
mo = [[None] * m for f in range(n)]

print("Matriz generada tipo 3)", mo, end="\n\n")

n, m = 3, 4
a = [[None] * m for f in range(n)]

for f in range(len(a)):
    for c in range(len(a[f])):
        a[f][c] = int(input("Valor: [" + str(f) + "][" + str(c) + "]"))

print("Matriz cargada por filas:", a, end="\n\n")

n, m = 3, 4
a = [[None] * m for f in range(n)]

filas, columnas = len(a), len(a[0])
for c in range(columnas):
    for f in range(filas):
        a[f][c] = int(input("Valor: [" + str(f) + "][" + str(c) + "]"))

print("Matriz cargada por columnas: ", a, end="\n\n")
