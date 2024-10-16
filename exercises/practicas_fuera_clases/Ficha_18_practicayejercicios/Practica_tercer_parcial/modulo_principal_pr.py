"""
Una tienda dedicada a la venta de ropa para niños, desea un programa para procesar los datos de sus prendas.
Por cada Prenda se tienen los siguientes datos: número de identificación de la prenda, la descripción de la
prenda, el precio de la prenda, la cantidad en stock de la prenda y el tipo de prenda (un valor entre 0 y 14
ambos incluidos, de la forma 0: Remera, 1: Pantalón, 2: Buzo, etc.). Se desea almacenar la información referida
a las n prendas en un arreglo de registros de tipo Prenda (definir el tipo Prenda y cargar n por teclado).
Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de las n prendas. Valide que el tipo de prenda sea un valor entre 0 y 14
(ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de las prendas, en un listado ordenado de menor a mayor según el tipo de prenda.

3- Usando el arreglo creado en el punto 1, determine el stock total que se tiene por cada tipo de prenda
(o sea, 15 contadores). Muestre sólo los resultados mayores a 0.

4- Determinar la prenda que posee el mayor precio y mostrar sus datos. Si existe más de un registro que
 posea el mayor precio, mostrar sólo uno.

5- Determinar si existe una prenda cuya descripción sea igual a x, siendo x un valor que se carga por teclado.
 Si existe, mostrar sus datos junto con el importe que representa (stock * precio). Si no existe, informar con
 un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar todos los
 que encuentre.


"""

from modulo_funciones_pr import *


def principal():
    paso_primera = False
    mensaje_error = "Debes cargar los datos antes.."

    opc = 1
    while opc != 6:

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primera = True
            n = validate(0, "Cantidad de prendas a cargar: ", "Error ! ingrese mayor a cero..")
            v = [None] * n
            cargar_vector(v)

        elif opc == 2:
            if paso_primera:
                print("---CATALOGO---")
                mostrar_vector(v)
            else:
                print(mensaje_error)

        elif opc == 3:
            if paso_primera:
                cont = stock_total_tipo_prenda(v)
                # mostrar_vector(cont)
            else:
                print(mensaje_error)

        elif opc == 4:
            if paso_primera:
                pass
            else:
                print(mensaje_error)

        elif opc == 5:
            if paso_primera:
                pass
            else:
                print(mensaje_error)

        else:
            print("Error ! valor incorrecto.")


if __name__ == "__main__":
    principal()
