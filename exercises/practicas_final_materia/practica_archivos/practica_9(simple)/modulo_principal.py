import modulo_funciones
import modulo_registro
import random
import pickle
import os.path


def add_in_order(profesional, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if profesional.dni == v[c].dni:
            pos = c
            break

        if profesional.dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [profesional]


def busqueda_binaria(v, doc):
    n = len(v)
    indice = -1
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if doc == v[c].dni:
            indice = c
            break

        if doc < v[c].dni:
            der = c - 1
        else:
            izq = c + 1

    return indice


def buscar_por_dni(v):
    doc = modulo_funciones.validar_rango(11111111, 99999999, "Ingrese el n°DNI a buscar: ")
    res = busqueda_binaria(v, doc)

    if res != -1:
        print(f"\nSe ha encontrado el DNI: '{doc}', sus datos: ", end="\n\n")
        imp = float(input("Ingrese el importe actual a cumplir: "))
        if v[res].importe < imp:
            print(f"El importe de {v[res].nombre} se encuentra desactualizado, tomar medidas.", end="\n\n")
            print(modulo_registro.to_string(v[res]))
    else:
        print(f"\nLo sentimos... no hemos encontrado el DNI: '{doc}'.", end="\n\n")


def cargar_arreglo(v):
    n = modulo_funciones.validar_positivo(0, "Ingrese la cantidad de profesionales: ")
    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes", "Maceira", "Armando", "Londo",
                 "Pearson", "Wenjshac", "Smoll")

    for i in range(n):
        dni = random.randint(11111111, 99999999)
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        importe = round(random.uniform(10000, 60000), 2)
        t_afiliacion = random.randint(0, 4)
        t_trabajo = random.randint(0, 14)

        profesional = modulo_registro.Profesional(dni, nombre, importe, t_afiliacion, t_trabajo)
        add_in_order(profesional, v)

    print("\nSe ha generado correctamente el arreglo de profesionales ordenado por DNI.", end="\n\n")


def mostrar_arreglo(v):
    print("\nSe muestra a continuacion todo el contenido de los registros en el arreglo: ", end="\n\n")
    for profesional in v:
        print(modulo_registro.to_string(profesional))


def cargar_archivo(v, fd):
    m = open(fd, "wb")
    x = float(modulo_funciones.validar_positivo(0, "Ingrese un monto para crear el archivo comprendido: "))
    for profesional in v:
        if profesional.t_trabajo in [3, 4, 5] and profesional.importe > x:
            pickle.dump(profesional, m)

    m.close()
    print(f"\nSe ha creado el archivo '{fd}' comprendido.", end="\n\n")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta ver no existe.", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestra a continuacion los registros del archivo '{fd}': ", end="\n\n")
    while m.tell() < tam:
        profesional = pickle.load(m)
        print(modulo_registro.to_string(profesional))

    m.close()


def buscar_por_nombre(v):
    nom = modulo_funciones.validar_cadena("Ingrese el nombre a busca: ")
    modulo_funciones.buscador_visual(nom)

    indice = -1
    for i in range(len(v)):
        if v[i].nombre == nom:
            indice = i
            break

    if indice != -1:
        print(f"\nSe encontro a '{nom}', sus datos: ", end="\n\n")
        print(modulo_registro.to_string(v[indice]))
    else:
        print(f"\nLo sentimos... no hemos encontrado a '{nom}'.", end="\n\n")


def crear_matriz(v):
    matriz = [[0] * 5 for f in range(15)]

    for profesional in v:
        fila = profesional.t_trabajo
        columna = profesional.t_afiliacion

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nResultados del analisis: ", end="\n\n")

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("{:>8}{:<17}{}{:<17}{}{}".format("T.Afiliacion: ", modulo_registro.convertir_datos(c, ban=False),
                                                       "- T.Trabajo: ", modulo_registro.convertir_datos(f, ban=True),
                                                       "- Cantidad total: ", matriz[f][c]))


def principal():
    menu = "\n\t\t==Profesiones Menu==\n" \
           "1). Cargar arreglo de 'n' profesionales, ordenado por DNI.\n" \
           "2). Mostrar el arreglo completo.\n" \
           "3). Buscar profesional por DNI.\n" \
           "4). Crear un archivo comprendido con el arreglo.\n" \
           "5). Mostrar al archivo completo.\n" \
           "6). Buscar profesional por nombre.\n" \
           "7). Cantidad de profesionales por tipo de afiliacion-tipo de trabajo.\n" \
           "0). Salir del programa.\n"

    fd = ""
    v = []
    paso_primero = False
    error = "\nError ! primero debe generar el arreglo."

    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            cargar_arreglo(v)

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_por_dni(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                fd = input("Ingrese el nombre del archivo: ")
                fd = f"{fd}.dat"
                cargar_archivo(v, fd)

        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo(fd)

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                buscar_por_nombre(v)

        elif opc == 7:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 0:
            print("\nPrograma terminado.")
        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
