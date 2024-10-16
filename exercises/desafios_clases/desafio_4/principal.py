import pickle
import os.path
import math

# clase y funcion de display


class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


# carga en el arreglo

fd = "puntos.df4"

v = []
m = open(fd, "rb")

t = os.path.getsize(fd)

while m.tell() < t:
    dato = pickle.load(m)
    v.append(dato)

m.close()

# visualizacion

for registro in v:
    print(to_string(registro))


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))


n = len(v)
dmax = 0
dmin = distance_between(v[0], v[1])
for i in range(0, n-1):
    for j in range(i+1, n):
        d = distance_between(v[i], v[j])
        if d < dmin:
            dmin = d

        if d > dmax:
            dmax = d

print(f"Distancia minima: {round(dmin, 0)}")
print(f"Distancia maxima: {round(dmax, 0)}")
