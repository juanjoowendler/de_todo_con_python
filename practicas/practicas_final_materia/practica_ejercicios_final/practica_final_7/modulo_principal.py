import modulo_registro
import modulo_validaciones
import random
import pickle
import os.path


def add_in_order(traslado, v):
    n = len(v)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der)//2

        if traslado.identificacion == v[c].identificacion:
            pos = c
            break

        if traslado.identificacion < v[c].identificacion:
            der = c-1
        else:
            izq = c+1

    if izq > der:
        pos = izq

    v[pos:pos] = [traslado]


def cargar_arreglo(v):
    n = modulo_validaciones.validar_positivo(0, "Ingrese la cantidad de traslados: ")
    nombres = ("Juan", "Pedro", "Seba", "Caro", "Milagros", "Pepe", "Carlos", "Juana", "Alfonso", "Alvaro",
               "Ernando", "Agostina", "Lucas8", "Lucia", "Maria")
    apellidos = ("Wendler", "Lambrusqui", "Paredes1", "Maceira", "Armando", "Londo",
                 "Pearson", "Wenjshac", "Smoll0")

    for i in range(n):
        identificacion = random.randint(1000, 9999)
        cliente_nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        importe = random.uniform(100, 9999)
        destino = random.randint(0, 22)
        forma_pago = random.randint(0, 4)

        traslado = modulo_registro.Traslado(identificacion, cliente_nombre, importe,
                                            destino, forma_pago)

        # ordenado por identificacion de menor a mayor
        add_in_order(traslado, v)


def mostrar_arreglo(v):
    print("\nSe muestra a continuacion el contenido del arreglo completo: ")
    for traslado in v:
        print(modulo_registro.to_string(traslado))


def busqueda(nom, v):
    for i in range(len(v)):
        if v[i].cliente_nombre == nom:
            return v[i]

    return -1


# validar que solo tenga letras y espacios, no numeros
# agregar un * (asterisco) en caso de que no cumpla
def validar_nombre(nom):
    tiene_digitos = False
    for car in nom:
        if car == " " or car == ".":
            tiene_espacio = True
            if tiene_espacio and not tiene_digitos:
                return True
            else:
                return False
        else:
            if car in "1234567890":
                tiene_digitos = True


def buscar_por_nombre(v):
    nom = modulo_validaciones.validar_cadena(0, "Ingrese el nombre a buscar: ")
    registro = busqueda(nom, v)
    if registro != -1:
        print("\nEncontrado ! sus datos: ")
        print(modulo_registro.to_string(registro))
        res = validar_nombre(registro.cliente_nombre)

        if not res:
            registro.cliente_nombre += " *"
            print("\nEl nombre ha sido marcado como no valido.")

    else:
        print(f"\nNo hemos encontrado el nombre {nom}...")


# solo aquellos cuya forma de pago sea 0 y cuyo importe se
# encuentre entre entre dos valores cargados por teclado
# mi importe va de [100-9999] $
def generar_archivo(v, fd):
    m = open(fd, "wb")
    imp1 = modulo_validaciones.validar_rango(100, 9999, "Ingrese primer importe: $ ")
    imp2 = modulo_validaciones.validar_rango(100, 9999, "Ingrese segundo importe: $ ")

    for traslado in v:
        if traslado.forma_pago == 0 and (imp1 <= traslado.importe <= imp2):
            pickle.dump(traslado, m)

    m.close()

    print(f"\nSe ha generado el archivo {fd} correctamente.")


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nPrimero debe crear el archivo en el Pto 4).", end="\n\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    print(f"\nSe muestra a continuacion el contenido del archivo comprendido {fd}: ")
    while m.tell() < tam:
        traslado = pickle.load(m)
        print(modulo_registro.to_string(traslado))

    m.close()


def main():
    menu = "\t\t\n===Empresa de Mudanzas===\n" \
           "1). Cargar arreglo completo.\n" \
           "2). Mostrar arreglo completo.\n" \
           "3). Buscar por nombre.\n" \
           "4). Crear archivo comprendido.\n" \
           "5). Mostrar archivo completo.\n" \
           "0). Salir del programa.\n"

    error = "\nError ! primero debe cargar el arreglo en el Pto 1)."
    v = []
    fd = "traslados.dat"
    opc = -1
    paso_primero = False
    while opc != 0:
        print(menu)
        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            cargar_arreglo(v)
            paso_primero = True

        elif opc == 2:
            if not paso_primero:
                print(error)
            else:
                mostrar_arreglo(v)

        elif opc == 3:
            if not paso_primero:
                print(error)
            else:
                buscar_por_nombre(v)

        elif opc == 4:
            if not paso_primero:
                print(error)
            else:
                generar_archivo(v, fd)

        elif opc == 5:
            mostrar_archivo(fd)

        elif opc == 0:
            print("Programa terminado.")

        else:
            print("Error ! opcion incorrecta.")


if __name__ == "__main__":
    main()
