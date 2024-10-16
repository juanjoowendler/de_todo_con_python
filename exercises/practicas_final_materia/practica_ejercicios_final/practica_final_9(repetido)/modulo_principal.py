from modulo_validaciones import *
from modulo_registro import *
import random
import pickle
import os.path


def cargar_arreglo(v):
    puestos = ("Autopista Carlos Paz.", "Cordoba acceso norte.", "Cordoba acceso sur.",
               "Autopista 20.", "Cordoba acceso este.", "Cordoba acceso oeste.")
    letras = ("A","B","C","D","E","F", "G", "H", "I", "J",
              "K", "L", "M", "N", "O", "P", "Q", "R", "S",
              "T", "U", "V", "W", "X", "Y", "Z")

    n = validar_positivo(0, "Cantidad de cobros: ")
    for i in range(n):
        numero = random.randint(100, 999)
        puesto = random.choice(puestos)
        monto = random.uniform(100, 500)
        patente = f"{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}" \
                  f"{round(monto, 0)}"
        hora = random.randint(0, 23)

        cobro = Cobro(numero, puesto, monto, patente, hora)
        v.append(cobro)

    print("\nCobros cargados exitosamente en el arreglo de registros.", end="\n\n")


def ordenar_arreglo(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].numero > v[j].numero:
                v[i], v[j] = v[j], v[i]


def mostrar_arreglo(v, ban=True, importe=0):
    if ban:
        print("\nContenido completo del arreglo: ", end="\n\n")
        for cobro in v:
            print(to_string(cobro))
    else:
        print(f"\nContenido cuyos montos sean menor a $ {importe}")
        for cobro in v:
            if cobro.monto < importe:
                print(to_string(cobro))


def acumulador(v):
    ac = [0] * 24
    for cobro in v:
        ac[cobro.hora] += cobro.monto

    print("\nMontos acumulados por hora: ", end="\n\n")
    for i in range(len(ac)):
        if ac[i] != 0 and (20 <= i <= 23) or (0 <= i <= 6):
            print("Hora: ", i, "Monto acumulado: $ ", ac[i])


def generar_archivo(fd, v, puesto):
    m = open(fd, "wb")
    for cobro in v:
        if cobro.numero >= puesto:
            pickle.dump(cobro, m)

    m.close()

    print(f"\nSe ha creado exitosamente el archivo '{fd}' desde id's superiores a {puesto}.", end="\n\n")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta visualizar no existe.", end="\n\n")
        return

    print("\nContenido completo del arreglo: ", end="\n\n")
    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        cobro = pickle.load(m)
        print(to_string(cobro))

    m.close()


def buscar_cobro(p, h, v):
    for cobro in v:
        if cobro.patente == p and cobro.hora == h:
            return cobro.puesto

    return -1


def analizar_cadena(nombre):
    punto_8 = 0
    mayuscula = False

    for car in nombre:
        if car == " " or car == ".":
            if mayuscula:
                punto_8 += 1

            mayuscula = False
        else:
            if car == car.upper():
                mayuscula = True

    print(f"\nHay {punto_8} palabras con al menos una mayuscula.", end="\n\n")


def principal():
    menu = "\t\t\n==Espectaculos Menu=\n" \
           "1). Cargar arreglo completo.\n" \
           "2). Mostrar arreglo completo.\n" \
           "3). Mostrar comprendido ordenado.\n" \
           "4). Monto acumulado por hora.\n" \
           "5). Generar archivo comprendido.\n" \
           "6). Mostrar archivo completo.\n" \
           "7). Informar cobro peaje.\n" \
           "8). Analizar cadena.\n" \
           "0). Salir del programa.\n"

    fd = "cobros_peaje.dat"
    encontro = ""
    error = "\nError ! primero debe cargar el arreglo en el Pto 1)."
    paso_primero = False
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)
            paso_primero = True

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                importe = validar_positivo(0, "Importe a comprender: $ ", ban=False)
                ordenar_arreglo(v)
                mostrar_arreglo(v, importe=importe)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                acumulador(v)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                puesto = validar_rango(100, 999, "Identificacion a comprender (100-999): ")
                generar_archivo(fd, v, puesto)

        elif opc == 6:
            mostrar_archivo(fd)

        elif opc == 7:
            if not paso_primero:
                print(error)
            else:
                p = validar_cadena("Ingrese la patente: ")
                h = validar_rango(0, 23, "Ingrese la hora (0-23): ")
                nombre = buscar_cobro(p, h, v)
                if nombre != -1:
                    print(f"\nEncontrado ! el nombre del puesto es: '{nombre}'")
                    encontro = True
                else:
                    print(f"\nLo sentimos... no existe ningun cobro con esas caracteristicas.")

        elif opc == 8:
            if encontro:
                analizar_cadena(nombre)
            else:
                print("Primero debe buscar un cobro y encontrarlo en el Pto 7).")

        elif opc == 0:
            print("\nPrograma terminado.")

        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
