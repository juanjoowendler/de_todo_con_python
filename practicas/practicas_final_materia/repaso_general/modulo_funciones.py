import modulo_validaciones
import modulo_registro
import random as rd
import pickle
import os.path


def add_in_order(proyecto, v):
    """
    :param proyecto: registro
    :param v: arreglo de proyectos procesandose
    :return: None
    """

    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if proyecto.identificacion == v[c].identificacion:
            pos = c
            break

        if proyecto.identificacion < v[c].identificacion:
            der = c - 1
        else:
            izq = c + 1
    # cargado
    v[pos:pos] = [proyecto]


def cargar_arreglo(v, mensaje_terminal):
    """
    :param v: arreglo vacio
    :return: None
    """
    descripciones = ("Reducir poblacion.", "Mejorar productos.", "Tratamiento X.",
                     "Calcular desastres.", "Encontrar talentos.", "Producir masas.",
                     "Viajes lunares.", "Produccion primaria.", "Produccion ultra.",
                     "Desarrollo agro.", "Tratamiento flex.")

    n = modulo_validaciones.validar_positivo(0, "Cantidad de proyectos [mayor a cero]: ")
    for i in range(n):
        identificacion = rd.randint(100, 999)
        nombre = f"Proy.{identificacion}/{identificacion - 1}"
        descripcion = rd.choice(descripciones)
        monto = rd.uniform(10000, 999999)
        area_aplicacion = rd.randint(1, 39)
        tipo_proyecto = rd.randint(0, 9)

        proyecto = modulo_registro.Proyecto(identificacion, nombre, descripcion, monto, area_aplicacion, tipo_proyecto)
        # ordenado por ID
        add_in_order(proyecto, v)

    print(mensaje_terminal)


def mostrar_arreglo(v, tit):
    """
    :param v: arreglo de registros
    :return: None
    """
    print(tit)
    for proyecto in v:
        print(modulo_registro.to_string(proyecto))


def generar_archivo(v, fd, mensaje_terminal):
    """
    :param v: arreglo de registros
    :param fd: file object
    :return: None
    """
    archivo = open(fd, "wb")
    for proyecto in v:
        if proyecto.tipo_proyecto not in [0, 1]:
            pickle.dump(proyecto, archivo)

    archivo.close()
    print(mensaje_terminal)


def promedio(cantidad, total):
    """
    :param cantidad: $ acumulado
    :param total: == cantidad
    :return: promedio
    """
    prom = 0
    if total > 0:
        prom = round(cantidad / total, 2)

    return prom


def mostrar_archivo(fd, mensaje_terminal):
    """
    :param fd: file object
    :return: None
    """
    if not os.path.exists(fd):
        print("- [!] Primero debe crear el archivo.")
        return

    print(mensaje_terminal)
    acumulado, cantidad = 0, 0

    archivo = open(fd, "rb")
    tam = os.path.getsize(fd)

    while archivo.tell() < tam:
        proyecto = pickle.load(archivo)
        acumulado += proyecto.monto
        cantidad += 1
        print(modulo_registro.to_string(proyecto))

    archivo.close()

    print(f"El monto promedio de los registros mostrados es de $ {promedio(acumulado, cantidad)}.")


def buscar_nombre(v, nom):
    """
    :param v: arreglo de registros
    :param nom: nombre de proyecto
    :return: descripcion ó mensaje
    """
    for proyecto in v:
        if proyecto.nombre == nom:
            print(f"Encontrado ! datos de {nom}: ")
            print(modulo_registro.to_string(proyecto))
            return proyecto.descripcion

    return "No existe."


def crear_matriz(v):
    """
    :param v: arreglo de registros
    :return: matriz de conteo
    :var fila: Tp.Proyecto
    :var columna: Ar.Aplicacion
    """
    matriz = [[0] * 39 for _ in range(10)]
    for proyecto in v:
        fila = proyecto.tipo_proyecto
        columna = proyecto.area_aplicacion - 1

        matriz[fila][columna] += 1

    return matriz


def mostrar_matriz(matriz, mensaje_terminal):
    """
    :param matriz: matriz de conteo
    :return: None
    :var fila: Tp.Proyecto
    :var columna: Ar.Aplicacion
    """
    print(mensaje_terminal)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] > 0:
                print("{:>8}{:<10}{}{:<10}{}{}".format("Ar.Aplicacion: ", columna + 1,
                                                       "Tp.Proyecto: ", fila,
                                                       "Cantidad: ", matriz[fila][columna]))


def es_digito(car):
    """
    :param car: caracter
    :return: valor boolean
    """
    if "0" <= car <= "9":
        return True
    return False


def es_vocal(car):
    """
    :param car: caracter
    :return: valor boolean
    """
    if car in "aeiou":
        return True
    return False


def procesar_cadena(cadena):
    """
    Al menos un digito y 2 vocales seguidas
    :param cadena: texto a ser procesado
    :return: None
    """
    cant_pal = 0
    anterior = ""
    ban1, ban2 = False, False

    for car in cadena:
        if car == " " or car == ".":
            if ban1 and ban2:
                cant_pal += 1

            ban1, ban2 = False, False
        else:
            if es_digito(car):
                ban1 = True

            if es_vocal(anterior) and es_vocal(car):
                ban2 = True

            anterior = car

    print(f"\nCantidad de palabras buscadas: {cant_pal}.")
