__author__= "Wendler Juan Jose"

# Titulos y carga de datos...
print("Calculo de la temperatura promedio: ")
t1 = int(input("Temperatura 1: "))
t2 = int(input("Temperatura 2: "))
t3 = int(input("Temperatura 3: "))

# Procesos...
suma = t1 + t2 + t3
prom1 = suma // 3
prom2 = suma / 3

# Visualizacion de resultados...
print("Promedio entero: ", prom1)
print("Promedio real: ", prom2)
