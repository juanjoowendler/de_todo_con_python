import modulo_funciones


def principal():
    menu = "\n\t\t==TV+Internet Menu==\n" \
           "1). Cargar arreglo de 'n' facturas ordenado por n° identificacion.\n" \
           "2). Mostrar todo el contenido del arreglo.\n" \
           "3). Buscar factura por n° identificacion.\n" \
           "4). Cantidad de clientes por tipo cliente - tipo producto.\n" \
           "5). Generar un archivo comprendido y mostrar.\n" \
           "6). Calcular porcentaje facturado de un producto 'x' sobre el total.\n" \
           "0). Salir del programa.\n"

    v = []

    error = "\nError ! primero debe cargar el arreglo."
    paso_primero = False
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            paso_primero = True
            modulo_funciones.cargar_arreglo(v)

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                modulo_funciones.mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                modulo_funciones.buscar_por_identificacion(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                matriz = modulo_funciones.generar_matriz(v)
                modulo_funciones.mostrar_matriz(matriz)
        elif opc == 5:
            if not paso_primero:
                print(error)
            else:
                modulo_funciones.crear_archivo(v)

        elif opc == 6:
            if not paso_primero:
                print(error)
            else:
                modulo_funciones.facturado_para_x_cliente(v)

        elif opc == 0:
            print("\nPrograma terminado.")
        else:
            print("\nError ! opcion incorrecta.")


if __name__ == "__main__":
    principal()
