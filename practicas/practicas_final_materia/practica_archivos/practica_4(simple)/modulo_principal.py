from modulo_registro import *
from modulo_funciones import *
import random
import pickle
import os.path

def add_in_order(paciente, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if v[c].numero_hcl == paciente.numero_hcl:
            pos = c
            break

        if paciente.numero_hcl < v[c].numero_hcl:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [paciente]


def cargar_arreglo(v):
    n = validar_positivo(0, "Ingrese la cantidad de pacientes a cargar: ")

    for i in range(n):
        nombres = ("Juan", "Pepe", "Carlos", "Caro", "Maria", "Ana", "Julian", "Agos", "Lucia", "Ludmila"
                   ,"Humberto", "Manuel", "Thiago", "Tomas", "Jeron", "Luz", "Julieta")
        apellidos = ("Paredes", "Leister", "Lambrusqui", "Wendler", "Laica", "Orsyon", "Armando", "Gonzalez")

        numero_hcl = random.randint(1, 99999999)
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        ult_visita = random.randint(1, 99)
        problema = random.randint(0, 9)

        paciente = Paciente(numero_hcl, nombre, ult_visita, problema)
        add_in_order(paciente, v)


def mostrar_comprendido(v):
    d = validar_rango(1, 99, "Ingrese la cantidad de dias para mostrar los pacientes: ")

    print(f"\nSe muestran a continuacion los pacientes que no residen desde hace {d} dias o mas: ")
    for paciente in v:
        if paciente.ult_visita >= d:
            print(to_string(paciente))


def buscar_paciente(v):
    x = validar_positivo(0, "Ingrese el Num.HC a buscar: ")

    n = len(v)
    indice = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2

        if x == v[c].numero_hcl:
            indice = c
            break

        if x < v[c].numero_hcl:
            der = c-1

        else:
            izq = c+1

    if indice != -1:
        print(f"Se ha encontrado al paciente {v[indice].nombre} - Num.HC = {v[indice].numero_hcl}, sus datos:")
        print(to_string(v[indice]))
        print()

    else:
        print(f"No se ha encontrado ningun paciente con el Num.HC = {x}.")


def mostrar_arreglo(v):
    print("\nTodos los pacientes del arreglo se muestran a continuacion: ")
    for paciente in v:
        print(to_string(paciente))


def cargar_archivo(v, fd):
    m = open(fd, "wb")

    for paciente in v:
        pickle.dump(paciente, m)

    m.close()
    print(f"Se han cargado exitosamente todos los datos en el arhcivo {fd}.")
    print()


def mostrar_archivo(fd):
    m = open(fd, "rb")

    print(f"\nSe muestran a continuacion los datos del archivo {fd}: ")
    tam = os.path.getsize(fd)
    while m.tell() < tam:
        paciente = pickle.load(m)
        print(to_string(paciente))

    m.close()


def cargar_segundo_arreglo(v2, fd):
    if not os.path.exists(fd):
        print("\nError ! primero debe crear el archivo en el pto (5).")
        print()
        return

    m = open(fd, "rb")

    tam = os.path.getsize(fd)
    while m.tell() < tam:
        paciente = pickle.load(m)
        if paciente.problema in [8, 9]:
            v2.append(paciente)

    m.close()
    print(f"\nSe ha generado exitosamente el segundo arreglo con el archivo {fd}.")
    print()


def mostrar_segundo_arreglo(v2):
    print("\nSe muestran a continuacion los pacientes con codigo de enfermedad '8' y '9': ")
    for paciente in v2:
        print(to_string(paciente))


def test():
    v, v2 = [], []
    fd = ""

    error = "\nError ! primero debe cargar el arreglo."
    paso_primero = False
    opc = -1
    while opc != 0:
        print("\n\t\t----Consultorio Medico----\n")
        print("1). Cargar arreglo ordenado por Num.HC.")
        print("2). Mostrar pacientes que no han asistido en 'd' dias.")
        print("3). Buscar paciente por Num.HC 'x'.")
        print("4). Mostrar todos los datos del arreglo.")
        print("5). Cargar todos los datos del arreglo en un archivo.")
        print("6). Mostrar los datos del archivo generado en el pto (5).")
        print("7). Crear otro arreglo con pacientes con problema tipo '8' o '9'.")
        print("8). Mostrar arreglo creado en el pto (7)")
        print("0). Terminar programa.")
        print()
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            cargar_arreglo(v)

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_comprendido(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_paciente(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                fd = input("Ingrese el nombre del archivo (sin extension): ")
                fd = f"{fd}.dat"
                cargar_archivo(v, fd)

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo(fd)

        elif opc == 7:
            if not paso_primero:
                print(error)
            else:
                cargar_segundo_arreglo(v2, fd)

        elif opc == 8:
            if not paso_primero:
                print(error)
            else:
                mostrar_segundo_arreglo(v2)

        elif opc == 0:
            print("\nPrograma terminado.")
        else:
            print("\nError ! opcion incorrecta.")
            print()




if __name__ == "__main__":
    test()
