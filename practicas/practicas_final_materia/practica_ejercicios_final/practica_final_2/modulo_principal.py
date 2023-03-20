import random
import pickle
import os.path
from modulo_funciones import *
from modulo_registro import *


# Agregarlo ordenado por - codigo de identificacion
def add_in_order(evento, v):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2

        if evento.codigo == v[c].codigo:
            pos = c
            break

        if evento.codigo <= v[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [evento]


def cargar_arreglo(v):
    n = validar_positivo(0, "Ingrese la cantidad de eventos: ")

    descripciones = ("El terremoto tuvo su epicentro en San Juan y se sintió en todo el norte argentino.",
                     "Un milagro ocurrio con la flia del señor Juan Carlos esta mañana en Jujuy.",
                     "Messi ganó la copa america en Argentina.", "Falleció Diego Maradona esta tarde.",
                     "Un lobo puede hablar con su dueño.", "Este vecino comprobó que es posible viajar en el tiempo.",
                     "El gato de Pepe puede hablar.")
    titulos = ("Catastrofe maritima", "Oremos por la flia", "Buenas noticias",
               "Malas noticias", "Ultimo minuto", "No lo creeran", "Increible !")
    caract = ("RL", "RL", "CA", "LA", "OA", "AE")
    abc = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "W", "Z")
    for i in range(n):
        codigo = f"{random.choice(abc)}{random.choice(caract)}-{random.randint(0, 100)}"
        titulo = random.choice(titulos)
        descripcion = random.choice(descripciones)
        costo = random.uniform(100, 9999)
        tip_evento = random.randint(0, 19)
        seg_diario = random.randint(0, 9)

        evento = Evento(codigo, titulo, descripcion, costo, tip_evento, seg_diario)
        add_in_order(evento, v)


def mostrar_arreglo(v):
    if len(v) == 0:
        print("\nPrimero debe cargar el arreglo...", end="\n\n")
        return

    print("\nSe muestra a continuacion el contenido del registro: ", end="\n\n")
    for evento in v:
        print(to_string(evento))


def generar_archivo(v, fd):
    if len(v) == 0:
        print("\nPrimero debe cargar el arreglo...", end="\n\n")
        return

    p = validar_rango(100, 9999, "Ingrese un monto: ", ban=False)
    m = open(fd, "wb")

    for evento in v:
        if evento.costo > p:
            pickle.dump(evento, m)

    m.close()
    print(f"\nSe ha creado el arcivo {fd} con montos superiores a $ {p} exitosamente.", end="\n\n")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nEl archivo que intenta ver no existe.", end="\n\n")
        return

    print("\nSe muestra a continuacion el contenido del archivo: ", end="\n\n")
    m = open(fd, "rb")
    size = os.path.getsize(fd)

    while m.tell() < size:
        evento = pickle.load(m)
        print(to_string(evento))

    m.close()


def mostrar_arreglo_v2(v2, prom):
    cad = "Costos: "
    for costo in v2:
        cad += f"$ {round(costo, 2)} - "
        print(cad, end="")

    print(f"\n$ {prom} - Es el promedio de los montos mostrados anteriormente.", end="\n\n")


def promedio(suma, total):
    prom = 0
    if total > 0:
        prom = round((suma / total), 2)

    return prom


def cargar_nuevo_arreglo(v2, fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear un archivo en el pto 3).", end="\n\n")
        return

    m = open(fd, "rb")
    size = os.path.getsize(fd)
    cant_t, acu_c = 0, 0

    while m.tell() < size:
        evento = pickle.load(m)
        if evento.tip_evento >= 5:
            v2.append(evento.costo)
            acu_c += evento.costo
            cant_t += 1

    m.close()
    prom = promedio(acu_c, cant_t)
    mostrar_arreglo_v2(v2, prom)


def busqueda_binaria(cod, v):
    n = len(v)
    indice = -1
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if cod == v[c].codigo:
            indice = c
            break

        if cod < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    return indice


def buscar_codigo(v):
    if len(v) == 0:
        print("\nPrimero debe cargar el arreglo...", end="\n\n")
        return

    cod = validar_codigo(0, "Ingrese el codigo a buscar: ")
    res = busqueda_binaria(cod, v)
    if res != -1:
        print(f"\nSe encontro el codigo - {v[res].codigo}, sus datos: ", end="\n\n")
        print(to_string(v[res]))
        return v[res].descripcion
    else:
        print(f"\nNo se encontro el codigo - {v[res].codigo}.", end="\n\n")


def crear_matriz(v):
    matriz = [[0] * 20 for f in range(10)]
    for evento in v:
        fila = evento.seg_diario
        columna = evento.tip_evento

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    print("\nResultados: \n")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if c > 7 and matriz[f][c] > 0:
                print("{:>8}{:<5}{}{:<5}{}{}".format("Tip.Evento: ", c, " Seg.Diario: ", f,
                                                     " Cantidad total: ", matriz[f][c]))


def mayusculas(car):
    if "A" <= car <= "Z":
        return True
    return False


def analizar_cadena(cad):
    cant_pal_com_may_y_ts, cant_let_pal = 0, 0
    cumple_1, tiene_t, tiene_s = False, False, False
    for car in cad:
        if car == " " or car == ".":
            if cumple_1 and tiene_t and tiene_s:
                cant_pal_com_may_y_ts += 1

            cumple_1, tiene_t, tiene_s = False, False, False
            cant_let_pal = 0
        else:
            cant_let_pal += 1
            if cant_let_pal == 1 and mayusculas(car):
                cumple_1 = True

            if car == "t":
                tiene_t = True
            if car == "s":
                tiene_s = True

    print(f"{cant_pal_com_may_y_ts} - es la cantidad de palabras que cumplen.")


def main():
    menu = "\n\n\t\t===Eventos de espectaculos===\n" \
           "1). Generar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Generar archivo binario.\n" \
           "4). Mostrar archivo binario.\n" \
           "5). Generar nuevo arreglo.\n" \
           "6). Buscar por codigo un evento.\n" \
           "7). Generar matriz.\n" \
           "8). Analizar cadena.\n" \
           "0). Salir del programa \n"

    v, v2 = [], []
    fd = "eventos.dat"
    paso_primero, existe_en_6 = False, False

    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            cargar_arreglo(v)

        elif opc == 2:
            mostrar_arreglo(v)

        elif opc == 3:
            generar_archivo(v, fd)

        elif opc == 4:
            mostrar_archivo(fd)

        elif opc == 5:
            cargar_nuevo_arreglo(v2, fd)

        elif opc == 6:
            cad = buscar_codigo(v)
            if cad is not None:
                existe_en_6 = True

        elif opc == 7:
            if not paso_primero:
                print("\nPrimero debe cargar el arreglo...")
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)

        elif opc == 8:
            if not existe_en_6:
                print("\nPrimero debe usar la opc 6), y el registro buscado debe existir.")
            else:
                analizar_cadena(cad)

        elif opc == 0:
            print("\nPrograma terminado.")
        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    main()
