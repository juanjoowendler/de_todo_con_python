__author__ = "Wendler Juan Jose"

# La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
# Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:

# a) Determinar y mostrar el nombre del ganador de la carrera.

# b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar
# si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.

# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

print("\n\t\t\tCiclistas: ")
print("-" * 35)

acu_tiempo = 0
cant = int(input("Ingresar la cantidad de competidores: "))

print("Ciclista 1:")
nom = input("Nombre del competidor: ")
tiempo = int(input("Tiempo del competidor: "))

for i in range(cant-1):
    if i == 0:
        men = tiempo
        ganador = nom

    elif tiempo < men:
        men = tiempo
        ganador = nom

    acu_tiempo += tiempo

    print("Ciclista", str(i+2)+":")
    nom = input("Nombre del otro competidor: ")
    tiempo = int(input("Tiempo del otro competidor: "))

record = int(input("Tiempo record registrado para dicha carrera: "))
if men < record:
    print("\n-Se supero el record de la carrera por", ganador)
else:
    print("\n\t-No se ha superado el record.")

prom = acu_tiempo / cant
print("-El ganador de la carrera es", str(ganador) + " con un tiempo de: ", str(men))
print("\n\t-El tiempo promedio entre los", str(cant) + " ciclistas fue de: ", round(prom, 2))
print("\nfin del programa...")

#-------------------------------------------------------------------------------------------------------------

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


print('CARRERA DE CICLISTAS')
print('-' * 40)
cont = acum = 0
ganador = None

n = int(input('Ingrese la cantidad de ciclistas que participan de la carrera: '))

for i in range(n):
    print('Ciclista',i)
    nombre = input('Ingrese nombre: ')
    tiempo = int(input('Ingrese tiempo: '))
    if ganador is None or tiempo < ganador[1]:
        ganador = nombre, tiempo
    cont += 1
    acum += tiempo

print('-' * 40)
if n > 0:
    record = int(input('Ingrese record actual: '))
    print('El ganador es', ganador[0])
    if ganador[1] < record:
        print('El ganador supero el record!')
        if cont > 0:
            promedio = round(acum / cont,2)
        else:
            promedio = 0
        print('Tiempo promedio general', promedio)
else:
    print('No se ingresaron datos')
