# Servicios Agropecuarios

# Una empresa de servicios agropecuarios necesita
# un programa para gestionar los datos de los 
# distintas productos y servicios que tiene a 
# para ofrecer a sus clientes.

# Por cada producto/servicio
# se conoce su número de identificación (un entero), 
# su descripción o título (una cadena), un número 
# entero entre 0 y 14 que indica el tipo de producto/servicio, 
# otro número entero entre 0 y 4 que indica la calidad del 
# mismo y finalmente el precio de venta de ese producto/servicio.

# Se pide:

# x. Desarrollar un programa completo con menú de opciones
# que permita cumplir los requerimientos que se indican a continuación.

# 1. Cargar los datos de n productos (ingrese el valor de n por teclado)
# en un arreglo unidimensional. Realice las validaciones que considere
# necesarias. Puede desarrollar este punto haciendo que el programa 
# genere en forma aleatoria el contenido de cada registro.

# 2. Mostrar los datos de todos los productos del vector,
# ordenados por número de identificación. 

# 3. Generar otro arreglo que contenga los datos de todos
# los productos del arreglo original que sean de tipo menor a 10.
# El agregado en este nuevo arreglo debe hacerse de forma que 
# vaya quedando siempre ordenado de menor a mayor por precio de venta.

# 4. Mostrar el nuevo arreglo, a razón de un registro por línea.

# 5. Usando el segundo arreglo, mostrar los datos de todos
# los productos cuyo precio sea menor o igual a un valor p 
# que se carga por teclado. 

# 6. Usando el segundo arreglo, determinar y mostrar la cantidad
# de productos que por cada tipo posible y por cada indicador de
# calidad posible. Es decir, se quiere saber cuántos existen del
# tipo 0 que sean de calidad 0, cuántos del tipo 0 y calidad 1, etc.

# 7. Grabar en un archivo todos los datos del segundo arreglo.

# 8. Mostrar el archivo que se acaba de crear en el punto anterior.

# -------------------------------------------------------------------

import modulo_funciones


def main():
    menu = "\t\t\n==Agropecuarios Menu==\n" \
           "1). Cargar arreglo.\n" \
           "2). Mostrar arreglo.\n" \
           "3). Cargar otro arreglo.\n" \
           "4). Mostrar otro arreglo.\n" \
           "5). Mostrar otro arreglo comprendido.\n" \
           "6). Crear y mostrar matriz.\n" \
           "7). Crear archivo de otro arreglo.\n" \
           "8). Mostrar archivo de otro arreglo.\n" \
           "0). Salir del programa.\n"

    error = format("\nError ! primero debe cargar el arreglo en el Pto {}).")
    paso_primero, paso_segundo = False, False
    v, v2 = [], []
    fd = "agropecuarios.dat"

    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            modulo_funciones.cargar_arreglo(v)
            paso_primero = True

        elif opc == 2:
            if not paso_primero:
                print(error.format("1"))
            else:
                modulo_funciones.ordenamiento(v)
                modulo_funciones.mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error.format("1"))
            else:
                modulo_funciones.cargar_otro_arreglo(v, v2)
                paso_segundo = True

        elif opc == 4:
            if not paso_segundo:
                print(error.format("3"))
            else:
                modulo_funciones.mostrar_arreglo(v2)

        elif opc == 5:
            if not paso_segundo:
                print(error.format("3"))
            else:
                modulo_funciones.mostrar_arreglo(v2, ban=False)

        elif opc == 6:
            if not paso_segundo:
                print(error.format("3"))

            else:
                matriz = modulo_funciones.crear_matriz(v2)
                if matriz is not None:
                    modulo_funciones.mostrar_matriz(matriz)

        elif opc == 7:
            if not paso_segundo:
                print(error.format("3"))
            else:
                modulo_funciones.crear_archivo(v2, fd)

        elif opc == 8:
            modulo_funciones.mostrar_archivo(fd)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
