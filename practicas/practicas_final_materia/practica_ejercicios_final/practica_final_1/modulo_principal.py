import random
import modulo_registro
import modulo_funciones
import pickle
import os.path


def cargar_arreglo(v):
    n = modulo_funciones.validar_positivo(0, "Ingrese la cantidad de cobros realizados: ")
    nombre_puestos = ("Autopista Carlos Paz.", "Córdoba acceso norte.", "Córdoba acceso sur.", "Córdoba acceso oeste.",
                      "Autopista Córdoba.")
    patentes_letras = ("FDX", "ASQ", "ASE", "KOA", "OPA", "SDS", "BHV", "ASZ")
    for i in range(n):
        numero = random.randint(10, 15) #id
        nombre = random.choice(nombre_puestos)
        monto = random.randint(100, 200)
        patente = f"{random.choice(patentes_letras)}{monto}"
        hora = random.randint(0, 23)

        cobro = modulo_registro.Cobro(numero, nombre, monto, patente, hora)
        v.append(cobro)


def mostrar_arreglo(v):
    if len(v) == 0:
        print("\nPrimero debe crear el arreglo...", end="\n\n")
        return

    print("\nSe muestra el contenido del arreglo completo: ", end="\n\n")
    for cobro in v:
        print(modulo_registro.to_string(cobro))


def ordenar_arreglo(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].numero > v[j].numero:
                v[i], v[j] = v[j], v[i]


def mostrar_listado(v):
    m = modulo_funciones.validar_rango(100, 200, f"Ingrese el monto. $ (van de {100}-{200}): ")
    ordenar_arreglo(v)
    print(f"\nLos datos ordenados por 'id' con un monto menor a $ {m} se muestran: ", end="\n\n")
    for cobro in v:
        if cobro.monto < m:
            print(modulo_registro.to_string(cobro))


def acumulado_por_hora(v):
    # 24 acumuladores
    acu = [0] * 24
    for cobro in v:
        acu[cobro.hora] += cobro.monto

    return acu


def mostrar_acu(acu):
    for i in range(len(acu)):
        if acu[i] > 0 and (0 <= i <= 6):
            print(f"Hora: {i} - Monto acumulado: $ {acu[i]}")


def generar_archivo(fd, v):
    if len(v) == 0:
        print("\nError ! el arreglo se encuentra vacio.", end="\n\n")
        return

    m = open(fd, "wb")
    id_x = modulo_funciones.validar_rango(10, 15, f"Ingrese un id entre ({10}-{15}): ")
    for cobro in v:
        if cobro.numero >= id_x:
            pickle.dump(cobro, m)

    m.close()
    print(f"\nSe creo un archivo con los registros cuyas id's son mayores o iguales a {id_x}.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta ver no existe.", end="\n\n")
        return

    print(f"\nSe muestra a continuacion el contenido del archivo '{fd}', sus datos: ", end="\n\n")

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        cobro = pickle.load(m)
        print(modulo_registro.to_string(cobro))

    m.close()


def buscar_cobro(v, p, h):
    for i in range(len(v)):
        if v[i].patente == p and v[i].hora == h:
            return i

    return -1


def analizar_cadena(nombre):
    cant_pal_may = 0
    mayusculas = "QWERTYUIOPÑLKJHGFDSAZXCVBNM"
    tiene_may = False

    for car in nombre:
        if car == " " or car == ".":
            if tiene_may:
                cant_pal_may += 1

                tiene_may = False
        else:
            if car in mayusculas:
                tiene_may = True

    print(f"\nResultados: \n'{cant_pal_may}' es la cantidad de palabras que contienen al menos una mayuscula.", end="\n\n")


def principal():
    menu = "\n\t\t==Peaje Menu==\n" \
           "1). Cargar arreglo de 'n' cobros, no ordenado.\n" \
           "2). Mostrar arreglo completo.\n" \
           "3). Mostrar ordenado por Num.Identificacion.\n" \
           "4). Monto acumulado en cada hora del dia.\n" \
           "5). Generar archivo desde un puesto por 'id'.\n" \
           "6). Mostrar el archivo binario.\n" \
           "7). Informar el cobro de peaje para una patente 'p' y hora 'h'.\n" \
           "8). Determinar cuantas palabras de la cadena contienen al menos 1 mayuscula.\n" \
           "0). Salir del programa\n"

    paso_7 = False
    fd = "cobros.dat"
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)

        elif opc == 2:
            mostrar_arreglo(v)

        elif opc == 3:
            mostrar_listado(v)

        elif opc == 4:
            acu = acumulado_por_hora(v)
            mostrar_acu(acu)
        elif opc == 5:
            generar_archivo(fd, v)

        elif opc == 6:
            mostrar_archivo(fd)

        elif opc == 7:
            p = modulo_funciones.validar_cadena(0, "Ingrese la patente: ")
            h = modulo_funciones.validar_rango(0, 23, "Ingrese la hora: ")
            res = buscar_cobro(v, p, h)
            if res != -1:
                nombre = v[res].nombre
                print(f"\n{nombre} - es el nombre del puesto que realizo el cobro.", end="\n\n")
                paso_7 = True
            else:
                print(f"\nNo existe ningun cobro realizado a una hora: {h} y a una patente: {p}.", end="\n\n")

        elif opc == 8:
            if paso_7:
                analizar_cadena(nombre)
            else:
                print("\nPrimero debe ejecutar la opcion 7).", end="\n\n")

        elif opc == 0:
            print("Programa terminado.")
        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
