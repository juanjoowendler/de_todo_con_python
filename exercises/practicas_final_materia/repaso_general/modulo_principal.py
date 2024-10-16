__author__ = "Wendler Juan José"

import modulo_funciones
import modulo_validaciones


def main():
    menu = "\n\t\t==Centro Investigacion==\n" \
           "\t1). Crear arreglo.\n" \
           "\t2). Mostrar arreglo.\n" \
           "\t3). Generar archivo.\n" \
           "\t4). Mostrar archivo.\n" \
           "\t5). Buscar por nombre.\n" \
           "\t6). Crear y mostrar matriz.\n" \
           "\t7). Procesar cadena.\n" \
           "\t0). Salir del programa.\n"

    error = format("- [!] Primero debe crear el arreglo{}")
    cadena = ""
    fd = "proyectos.dat"
    paso_primero, ok = False, False
    v = []
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            modulo_funciones.cargar_arreglo(v, "\nArreglo cargado exitosamente.")
            paso_primero = True

        elif opc == 2:
            if not paso_primero:
                print(error.format("."))
            else:
                modulo_funciones.mostrar_arreglo(v, "\nArreglo de registros completo: ")

        elif opc == 3:
            if not paso_primero:
                print(error.format("."))
            else:
                modulo_funciones.generar_archivo(v, fd, "\nArchivo comprendido creado exitosamente.")

        elif opc == 4:
            modulo_funciones.mostrar_archivo(fd, "\nArchivo de registros completo: ")

        elif opc == 5:
            if not paso_primero:
                print(error.format("."))
            else:
                nom = modulo_validaciones.validar_nombre("", "Nombre del proyecto: ")
                cadena = modulo_funciones.buscar_nombre(v, nom)
                ok = True

        elif opc == 6:
            matriz = modulo_funciones.crear_matriz(v)
            if matriz is not None:
                modulo_funciones.mostrar_matriz(matriz, "Contenido de la matriz: ")
            else:
                print(error.format("."))

        elif opc == 7:
            if not ok:
                print(error.format(" y/o encontrar un nombre en el Pto 5)."))
            else:
                modulo_funciones.procesar_cadena(cadena)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
