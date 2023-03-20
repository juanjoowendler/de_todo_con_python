# Una editorial encargada de la publicación de una revista científica ha
# solicitado que se desarrolle un programa para gestionar su operatoria.
# Se deben almacenar en un arreglo unidimensional (un vector) los datos
# relacionados con los artículos disponibles para su publicación
# (cargar por teclado la cantidad n de artículos).

# Cada artículo tiene los
# siguientes datos: código (int), título (cadena), cantidad de páginas,
# tipo de artículo (puede ser un valor entre 0 y 9 identificando el campo
# de aplicación) y el idioma en que está escrito (un valor entre 0 y 5).

# Se pide un programa controlado por menú de opciones que permita:

# 1. Cargar por teclado el arreglo de artículos, que debe quedar ordenado
# alfabéticamente de acuerdo al título de los artículos. Alternativamente, la carga
# puede hacerse en forma automática, generando en forma aleatoria los valores a
# contener en cada registro. Además, verificar que ningún artículo aparezca repetido en
# el arreglo (no permita dos artículos con el mismo título).

# 2. Mostrar el arreglo completo.

# 3. Cargar por teclado el título de un artículo y determinar si existe alguno con ese título.
# Mostrar sus datos si existe, o informar que no existe.

# 4. Cargar por teclado el código de un artículo y determinar si existe alguno con ese
# código. Mostrar sus datos si existe, o informar que no existe.

# 5. Determinar la cantidad de artículos por tipo e idioma que hay en el arreglo (es decir,
# cuántos artículos tipo 0 está escritos en el idioma 0, cuántos tipo 0 están en el idioma
# 1, y así sucesivamente… con un total de 10*6 = 60 contadores).

# 6. Generar un archivo que contenga todos los datos de los artículos cuya cantidad de
# páginas sea superior a 10.

# 7. Mostrar el archivo completo.

import modulo_funciones


def main():
    menu = "\t\t\n==Editorial Menu==\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Buscar por titulo.\n" \
           "4). Buscar por codigo.\n" \
           "5). Generar y mostrar matriz.\n" \
           "6). Generar archivo comprendido.\n" \
           "7). Mostrar archivo completo.\n" \
           "0). Salir del programa.\n"

    fd = "articulos.dat"
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            modulo_funciones.cargar_arreglo(v)

        elif opc == 2:
            modulo_funciones.mostrar_arreglo(v)

        elif opc == 3:
            modulo_funciones.buscar_por_titulo(v)

        elif opc == 4:
            modulo_funciones.buscar_por_codigo(v)

        elif opc == 5:
            matriz = modulo_funciones.generar_matriz(v)
            if matriz is not None:
                modulo_funciones.mostrar_matriz(matriz)

        elif opc == 6:
            modulo_funciones.generar_archivo(fd, v)

        elif opc == 7:
            modulo_funciones.mostrar_archivo(fd)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
