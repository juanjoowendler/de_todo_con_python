
# Uso del write() (con '\n')

m = open("datos.txt", "wt")
m.write("Primera linea de texto\n")
m.write("Segunda linea de texto")

m.close()

# Uso del read()

m = open("datos.txt", "rt")
print("Contenido completo: ")
cad = m.read()
print(cad)

m.close()

# Uso del readline() (con 'end=""')

m = open("datos.txt", "rt")
r1 = m.readline()
r2 = m.readline()
print("\nContenido linea por linea: ")
print(r1, end="")
print(r2)

m.close()

# Lectura por ciclo iterador (al ser muchas lineas)
# 'line in m' actua como un readline internamente

m = open("datos.txt", "rt")
print("\nContenido con iterador: ")
for line in m:
    print(line, end="")

m.close()

# Lectura controlada

print()
m = open("datos.txt", "rt")
print("\nContenido con control de lectura: ")
while True:
    # intenta leer una linea...
    line = m.readline()

    # ¿Cadena vacia? cortar el ciclo...
    if line == "":
        break

    # Si lo tenia, sacar el caracter salto de linea...
    if line[-1] == "\n":
        line = line[:-1]

    print(line)

m.close()

# Uso del readlines(); un arreglo con un casillero por
# cada linea|cadena leida donde el \n se preserva

m = open("datos.txt", "rt")
lista = m.readlines()
print("\nLista de lineas contenidas: ")
print(lista)

m.close()


