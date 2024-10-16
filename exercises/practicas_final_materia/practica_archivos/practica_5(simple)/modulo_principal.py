from modulo_funciones import *
from modulo_registro import *
import random
import pickle
import os.path


def add_in_order(articulo, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    
    while izq <= der:
        c = (izq + der)//2
        
        if v[c].titulo == articulo.titulo:
            pos = c

        if articulo.titulo < v[c].titulo:
            der = c-1
        else:
            izq = c+1
            
    if izq > der:
        pos = izq
    
    v[pos:pos] = [articulo]
    

def cargar_arreglo(v):
    n = validar_positivo(0, "Ingrese la cantidad de articulos a cargar: ")

    for i in range(n):
        titulos_1 = ("Patata", "Minion", "Joven", "Pepe", "Loco", "Spider", "Nene", "Super", "Abuelo")
        titulos_2 = ("Dura", "Feliz", "Triste", "Furioso", "Normal", "Serio", "Cool", "Musical")
        
        codigo = random.randint(0, 999999999)
        titulo = f"{random.choice(titulos_1)} {random.choice(titulos_2)}"
        cant_paginas = random.randint(1, 30)
        tipo = random.randint(0, 9)
        idioma = random.randint(0, 5)
        articulo = Articulo(codigo, titulo, cant_paginas, tipo, idioma)
        add_in_order(articulo, v)

    print("\nSe ha cargado exitosamente el arreglo ordenado por titulo.")


def mostrar_arreglo(v):
    print("\nSe muestran a continuacion los datos del arreglo generado: ", end="\n\n")
    for articulo in v:
        print(to_string(articulo))


def buscar_por_titulo(v):
    tit = validar_cadena("", "Ingrese el titulo a buscar: ")
    n = len(v)
    indice = -1
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if tit == v[c].titulo:
            indice = c
            break
        if tit < v[c].titulo:
            der = c-1
        else:
            izq = c+1

    if indice != -1:
        print(f"\nSe ha encontrado el titulo - '{tit}', sus datos: ", end="\n\n")
        print(to_string(v[indice]))
    else:
        print(f"\nLo sentimos... No hemos encontrado el titulo - '{tit}' en la libreria.", end="\n\n")


def buscar_por_codigo(v):
    cod = validar_positivo(0, "Ingrese el codigo a buscar: ")
    indice = -1

    for i in range(len(v)):
        if v[i].codigo == cod:
            indice = i
            break

    if indice != -1:
        print(f"\n Bien ! hemos encontrado algo con el codigo - '{cod}', sus datos: ", end="\n\n")
        print(to_string(v[indice]))
    else:
        print(f"\nLo sentimos... No hemos encontrado el codigo - '{cod}' en la libreria.", end="\n\n")


def crear_matriz(v):
    matriz = [[0] * 10 for f in range(6)]
    for articulo in v:
        fila = articulo.idioma
        columna = articulo.tipo
        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    print()
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] > 0:
                print(f"Idioma: {convertir_codigo(f, ban=True)} - Tipo: {convertir_codigo(c, ban=False)} "
                      f"- CANTIDAD: {matriz[f][c]}")


def generar_archivo_comprendido(v, fd):
    m = open(fd, "wb")
    for articulo in v:
        if articulo.cant_paginas > 10:
            pickle.dump(articulo, m)

    m.close()

    print(f"\nSe ha creado exitosamente el archivo: {fd}.", end="\n\n")


def mostrar_archivo_comprendido(fd):
    if not os.path.exists(fd):
        print(f"El archivo que intenta mostrar no existe.", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestra a continuacion el contenido completo del archivo: ", end="\n\n")
    while m.tell() < tam:
        articulo = pickle.load(m)
        print(to_string(articulo))

    m.close()


def principal():
    menu = "\n\t\tEDITORIAL MENU: \n\n\
        1). Cargar arreglo 'articulos' ordenado por titulo.\n\
        2). Mostrar completo el arreglo 'articulos' creado.\n\
        3). Buscar un articulo por titulo.\n\
        4). Buscar un articulo por codigo.\n\
        5). Cantidad de articulos por tipo-idioma y mostrar.\n\
        6). Generar archivo con articulos cuya Cant.Pag sea mayor a 10.\n\
        7). Mostrar completo el archivo.\n\
        0). Salir del programa.\n"

    error = "\nError ! Primero debe generar el arreglo."
    paso_primero = False
    v = []
    fd = ""
    
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
                buscar_por_titulo(v)
            
        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                buscar_por_codigo(v)
        
        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                matriz = crear_matriz(v)
                mostrar_matriz(matriz)
        
        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                fd = validar_cadena("", "Ingrese el nombre del archivo (sin extension): ")
                fd = f"{fd}.dat"
                generar_archivo_comprendido(v, fd)
        
        elif opc == 7:
            if not paso_primero:
                print(error)
            else:
                mostrar_archivo_comprendido(fd)
        
        elif opc == 0:
            print("\nPrograma terminado.")
       
        else:
            print("\nError ! opción incorrecta.")
            

if __name__ == "__main__":
    principal()
