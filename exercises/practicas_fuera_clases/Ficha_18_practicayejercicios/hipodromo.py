from soporte import *


def validar_positivo(mensaje):
    n = 0
    while n <= 0:
        n = int(input(mensaje))
        if n <= 0:
            print("Valor incorrecto.")
    return n


def cargar_vector(apuestas):
    for i in range(len(apuestas)):
        num = validar_positivo("Ingrese el numero del ticket: ") # num > 0
        cab = int(input("Ingrese el numero del caballo (0-9): ")) # 0<= cab <= 9
        mon = float(input("Ingrese el monto de la apuesta: ")) # mon > 0
        apuestas[i] = Apuesta(num, cab, mon)


def mostrar_vector(apuestas):
    for i in range(len(apuestas)):
        write(apuestas[i])


def contar(apuestas):
    cont = [0] * 10
    for i in range(len(apuestas)):
        cont[apuestas[i].caballo] += 1
    for i in range(10):
        print("Caballo: ", i, "- Cantidad:", cont[i])


def principal():
    n = validar_positivo("Ingrese la cantidad de apuestas: ") # num > 0
    apuestas = n * [None]
    cargar_vector(apuestas)
    mostrar_vector(apuestas)
    contar(apuestas)


if __name__ == "__main__":
    principal()
