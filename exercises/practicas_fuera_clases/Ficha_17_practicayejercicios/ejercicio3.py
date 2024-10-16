# Tren de la costa
# Desarrollar un programa que representeel recorrido de ida y vuelta del tren de la costa
# El recorrido del tren abarca las siguientes estaciones: Maipu, Borges, Libertador,
# Anchorena, Barracas, San Isidro R, Punta Chica, Mariana Nueva, San Fernando R, Canal, Delta.

# Se pide cargar un vector que contenga el nombre de las estaciones y otros dos que representen
# el viaje de ida y de vuelta del tren, respectivamente.

# En los dos últimos, se cargará la cantidad de pasajeros que ascendieron al tren
# en la estación correspondiente. Con la información cargada, plantear el siguiente menú de opciones:

# 1) Mostrar los datos cargados
# 2) Cuántos pasajeros en total subieron en el viaje de ida, y cuántos en el viaje de vuelta
# 3) En qué estación subió la mayor cantidad de pasajeros, durante el viaje de ida
# 4) En cuántas estaciones del viaje de vuelta no subieron pasajeros, y qué porcentaje representan
# sobre el total de estaciones
# 4) Mostrar las estaciones en las que la cantidad de pasajeros del viaje de ida fue mayor a
# la del viaje de la vuelta

import random


def acumular_viajes(viajes):
    total = 0
    for i in range(len(viajes)):
        total += viajes[i]
    return total


def buscar_mayor(ida):
    pos_mayor = 0
    for i in range(1, len(ida)):
        if ida[i] > ida[pos_mayor]:
            pos_mayor = i
    return pos_mayor


def comparar(estaciones, ida, vuelta, hay=False):
    print("Estaciones con mas pasajeros de ida que de vuelta.")
    for i in range(len(estaciones)):
        if ida[i] > vuelta[i]:
            print("Estacion: ", estaciones[i])
            hay = True
    if not hay:
        print("No hay estaciones con mas pasajeros en el viaje de ida que de vuelta.")


def no_pasajeros_vuelta(estaciones, vuelta, hay=False):
    print("Estaciones sin pasajeros en la vuelta")
    for i in range(len(vuelta)):
        if vuelta[i] == 0:
            print(estaciones[i])
            hay = True
    if not hay:
        print("No hubieron estaciones vacias en la vuelta.")


def cargar_vector(ida, vuelta):
    for i in range(len(ida)):
        ida[i] = random.randint(0, 169)
        vuelta[i] = random.randint(0, 169)


def mostrar_estaciones(estaciones, ida, vuelta):
    for i in range(len(estaciones)):
        print("Estaciones: ", estaciones[i], "- cantidad de pasajeros ida: ", ida[i], "- cantidad de pasajeros vuelta: ",
              vuelta[i])


def principal():
    estaciones = ["Maipu", "Borges", "Libertador", "Anchorena", "Barrancas", "San isidro R", "Punta chica", "Marina Nueva",
                  "San Fernando R", "Canal", "Delta"]
    ida = [0] * 11
    vuelta = [0] * 11
    op = 1

    carga = False
    mensaje_error = "Primero cargue el vector.."

    while op != 7:
        print("Tren de la Costa - Menu de Opciones")
        print("1.- Cargar vectores.")
        print("2.- Mostrar vectores.")
        print("3.- Acumular viajes")
        print("4.- Mayor cantidad de pasajeros en la ida.")
        print("5.- Mayores ida, que vuelta.")
        print("6.- No subieron en vuelta.")
        print("7.- Salir.")

        op = int(input("Ingrese su opcion: "))

        if op == 1:
            cargar_vector(ida, vuelta)
            carga = True

        elif op == 2:
            if not carga:
                print(mensaje_error)
            else:
                mostrar_estaciones(estaciones, ida, vuelta)

        elif op == 3:
            if not carga:
                print(mensaje_error)
            else:
                print("Cantidad de pasajeros de ida: ", acumular_viajes(ida))
                print("Cantidad de pasajeros de vuelta: ", acumular_viajes(vuelta))

        elif op == 4:
            if not carga:
                print(mensaje_error)
            else:
                may = buscar_mayor(ida)
                print("Estacion con mayor cantidad de pasajeros en la ida: ", estaciones[may])

        elif op == 5:
            if not carga:
                print(mensaje_error)
            else:
                comparar(estaciones, ida, vuelta)

        elif op == 6:
            if not carga:
                print(mensaje_error)
            else:
                no_pasajeros_vuelta(estaciones, vuelta)

        elif op == 7:
            print("Adios..")

        else:
            print("Opcion incorrecta !")

    cargar_vector(ida, vuelta)
    mostrar_estaciones(estaciones, ida, vuelta)


if __name__ == "__main__":
    principal()


