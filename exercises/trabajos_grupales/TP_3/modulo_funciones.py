from modulo_registros import *
import random as psg


#   FUNCION QUE CONTIENE TODOS LOS TITULOS PARA LOS IDIOMAS PEDIDOS.


def Titulos(eleccion):
    """
    Arreglo de titulos en varios idiomas.
    :return: Titulo de libros en Español, Ingles, Frances, Italiano y otros.

    """
    vector_titulos = ["Sacerdote sin conciencia", "Gángster con alas", "Gangsters de la fortuna", "Extranjeros",
                      "Capos y traidores", "Heroes y Búhos", "Carnicería de destrucción", "Varita del fin",
                      "Pesadillas", "Engañando al Maz", "Angel de la Noche", "Enemigo de Occidente", "Arco iris",
                      "Reyes del Fuego", "Guerreros y brujas", "Señores y traidores", "Certeza", "Inspiración",
                      "La vida", "Familia", "Llamar a pesadillas", "La mujer duerme en mi cama",
                      "Estrategia x", "Rompecabezas del ángel", "Gato de las montañas", "Crisis atomica ",
                      "Protector Of Spring", "Medic Of The Banished", "Witches Without Flaws",
                      "Robots And Nymphs", "Inception", "Palace Of Rainbows", "Weep For Shields", "Life At Hope",
                      "Horse Of The South", "Warrior Of The Stockades", "Creators", "Of The Stockades",
                      "Opponents Of Hope", "Collectors And Bakers", "Wives And Rats", "Fate Of ", "Crime",
                      "Death Of Breaking Hearts", "Memories Of A Storm", "Hunting The Past", "Woman Of The "
                                                                                             "Swamp", "Knight Of A Cat",
                      "Bandits Of An Asteroid", "Mice Of The Nether",
                      "Look for things", "Fast but not furious", "Le Seigneur des Anneaux"
                                                                 "Le Hobbit", "Un jeu de trones", "Le nom du vent",
                      "Dune", "Dieux américains",
                      "Chevaucheurs de dragons de Pern", "La voie des rois", "Harry", "La Belgariade",
                      "Le Silmar des millions", "Lapprenti assassin", "Les brumes dAvalon", "Navire vers le bas",
                      "Lhomme peint", "Tigane", "Une pincee de respect", "Sacerdote senza coscienza",
                      "Ufficiale con i peccati", "Straniero di grandezza", "Fabbri con onore", "Soldati DAcqua",
                      "Agenti e cavalieri", "Banditi e fabbri", "Il successo della terra", "Correre tra i leader",
                      "Cresciuto da mio marito", "Corriere", "Il nemico del mare", "Seguaci con debiti",
                      "Fondatori con peccati", "Donne e uomini", "Eserciti e salvatori", "Ascensione del limbo",
                      "Radice degli incubi", "Abbandonare le profondità", "Finendo la mia scuola",
                      "I nemici delle profondità", "Animali con stile", "Topi dei tuoi sogni", "Cavalli e ratti",
                      "Atleti ed erbe", "Il cibo di domani", "Libri del futuro", "Sydens mand", "Ulv uden pligt",
                      "Fjender Af Tid", "Betjente med udødelighed", "Arvinger og forsvar ere", "Jægere og hunde",
                      "Tro med sølv", "Wand med synder", "Besøg The Shadows", "Svartid", "Fanto m uden mod",
                      "Konge af virkeligheden", "Slanger Af Vand", "Nordens slanger", "Træer og forsvarere",
                      "Konger Og Forrædere", "Held med udødelighed", "Skæbne Af Guld", "Hvisker i drømme",
                      "Søger efter afgrunden"]

    titulo = vector_titulos[eleccion]

    return titulo


#   FUNCION PARA VALIDAR LA CANTIDAD DE LIBROS A CARGAR.


def validate(inf, mensaje, mensaje_error, mensaje_error_1):
    """

    :param inf: valor inferior para validar.
    :param mensaje:mensaje para la carga.
    :param mensaje_error: mensaje de error al ingresar incorrectamente.
    :param mensaje_error_1: mensaje de error al ingresar fuera de rango.
    :return: la cantidad de libros a cargar.

    """
    n = inf
    while inf >= n or n > 115:
        n = int(input(mensaje))
        if n <= 0:
            print(mensaje_error)
        if n > 115:
            print(mensaje_error_1)
    return n


#   FUNCION PARA REDIRECCIONAR SEGUN EL TIPO DE CARGA.


def cargar_libros(v, articulos):
    """
    :param v: arreglo de los libros.
    :param articulos: bandera, True = carga automatica, False = carga manual.

    """
    if articulos:
        random_read(v)

    elif not articulos:
        read(v)


#   FUNCION PARA VALIDAR SI EL CODIGO ESTA YA EN MEMORIA DE FORMA AUTOMATICA.


def validar_en_memoria_automatico(v, bandera, arreglo):
    """
    Validar si el codigo ya existe en el registro.
    :param bandera: bandera de control para la generacion y busqueda en memoria.
    :param arreglo: codigos ingresados por teclado a buscar.
    :param v: arreglo de los libros cargados.
    :return: un valor Booleano, True = esta, False = no esta.

    """
    n = len(v)
    if bandera:
        if n == 1:
            return True
        else:
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if v[i].codigo == v[j].codigo:
                        print("\x1b[0;31m" + "[!] Ya existe un libro que posee ese ISBN." + "\033[0;m")
                        return False

                    if v[i].titulo == v[j].titulo:
                        print("\x1b[0;31m" + "[!] Ya existe un libro que posee ese titulo." + "\033[0;m")

                        return False
                return True
    else:
        for i in range(n):
            if v[i].codigo == arreglo:
                return i
        return None


#   FUNCION PARA VALIDAR SI EL CODIGO ESTA YA EN MEMORIA DE FORMA MANUAL.


def validar_en_memoria_manual(v, ch, codigo_actual, titulo_actual):
    """
    Validar si el codigo ya existe en el registro.
    :param titulo_actual: titulo actual del libro.
    :param codigo_actual: codigo actual del libro.
    :param ch: cantidad de codigos cargados en memoria a comparar.
    :param v: arreglo de los libros cargados.
    :return: un valor Booleano, True = esta, False = no esta.

    """
    for i in range(ch):

        if v[i].codigo == codigo_actual:
            print("\x1b[0;31m" + "[!] Ya existe un libro que posee ese ISBN." + "\033[0;m")

            return False

        if v[i].titulo == titulo_actual:
            print("\x1b[0;31m" + "[!] Ya existe un libro que posee ese titulo." + "\033[0;m")

            return False

    return True


#   FUNCION PARA VALIDAR LA CARGA DLE ISBN MANUAL.


def validar_isbn_manual(mensaje):
    """
    Validar la carga manual del ISBN.
    :param mensaje: mensaje visual para la carga del codigo ISBN.
    :return: codigo ISBN valido.
    """
    codigo = ""
    band_guiones = anterior_guion = False

    while not band_guiones:

        cont_guiones = acu = cont_vueltas = vueltas = 0
        band_guiones = True
        codigo = input(mensaje)

        if len(codigo) < 13 or len(codigo) > 13:
            band_guiones = False

        if band_guiones:
            for car in codigo:

                if car != "-":
                    car_int = int(car)

                    acu += (car_int * (10 - cont_vueltas))
                    cont_vueltas += 1

                vueltas += 1

                if (vueltas == 1 and car == "-") or (vueltas == 13 and car == "-"):
                    band_guiones = False

                if car == "-" and anterior_guion:
                    band_guiones = False

                if car == "-":
                    anterior_guion = True
                    cont_guiones += 1

                else:
                    anterior_guion = False

        if acu % 11 != 0:
            band_guiones = False

        if cont_guiones != 3:
            band_guiones = False

    return codigo


#   FUNCION PARA GENERAR EL CODIGO ISBN.


def generador_ISBN():
    """
    :return: isbn.
    """
    x = [0] * 10
    acumulador = 1

    while acumulador % 11 != 0:
        acumulador = 0

        for i in range(10):
            x[i] = psg.randint(0, 9)

        for i in range(10):
            acumulador += x[i] * (10 - i)

    x = validar_isbn_automatico(x)

    return x


#   FUNCION PARA VALIDAR LA CARGA AUTOMATICA DEL CODIGO ISBN.


def validar_isbn_automatico(isbn_codigo):
    """
    :param isbn_codigo: codigo isbn cargado.
    :return: string del codigo isbn validado.

    """
    a = None
    bandera_ciclo = False
    copia_isbn = [0] * len(isbn_codigo)

    while not bandera_ciclo:
        vuelta = 0
        copia_isbn[:] = isbn_codigo

        anterior_guion = False
        bandera_ciclo = True

        for i in range(3):
            a = psg.randint(1, 9 + i)

            copia_isbn[a:a] += "-"

        for car in copia_isbn:
            vuelta += 1

            if car == "-" and vuelta == 1 or car == "-" and vuelta == 13:
                bandera_ciclo = False

            if car == "-" and anterior_guion:
                bandera_ciclo = False

            if car == "-":
                anterior_guion = True
            else:
                anterior_guion = False

    for i in range(len(copia_isbn)):
        if i == 0:
            a = str(copia_isbn[i])
        else:
            a += str(copia_isbn[i])

    return a


#   FUNCION PARA LA GENERACION MANUAL POR CARGA.


def read(v):
    """
    :param v: arreglo de los libros.

    """

    for i in range(len(v)):

        print("\nLibro[{}]".format(i))
        bandera_memoria = False

        while not bandera_memoria:
            mensaje_idioma ="\x1b[1;32m" + "Ingresar el idioma del libro que deseas conocer el mayor precio:\n"\
                             "\x1b[1;35m" + "Lista de idiomas: (Español - Ingles - Frances - Italiano - Otros)\n" + "\033[0;m"

            codigo = validar_isbn_manual("\x1b[3;36m" + "Ingresar codigo ISBN: \n")
            titulo = input("\x1b[3;36m" + "Ingresar titulo: \n").upper()
            genero = validar_gen()
            idioma = validar_idioma(mensaje_idioma).upper()
            precio = validar_positivo(True, "\x1b[3;36m" + "Ingresar precio: \n")

            v[i] = Libros(codigo, titulo, genero, idioma, precio)

            bandera_memoria = validar_en_memoria_manual(v, i, codigo, titulo)


#   GENERACION AUTOMATICA POR RANDOMIZACION.

def validar_gen():
    validacion = ["AUTOAYUDA", "ARTE", "FICCION", "COMPUTACION", "ECONOMIA", "ESCOLAR", "SOCIEDAD",
                  "GASTRONOMIA", "INFANTIL", "OTROS"]
    band = False
    genero = input("\x1b[3;36m" + "Ingresar genero: \n").upper()

    while not band:
        for i in range(len(validacion)):
            if validacion[i] == genero:
                band = True
        if not band:
            print(validacion)
            genero = (input("\x1b[3;36m" + "Ingresar un genero de la lista: \n")).upper()

    return genero


def random_read(v):
    """
    Genera de forma aleatoria los datos de los libros dentro de parametros pre-establecidos.
    :param v: arreglo de los libros.

    """
    libro = k = 0

    lista_idiomas = ["Español", "Ingles", "Frances", "Italiano", "Otros"]

    genero_ = ["AUTOAYUDA", "ARTE", "FICCION", "COMPUTACION", "ECONOMIA", "ESCOLAR", "SOCIEDAD",
               "GASTRONOMIA", "INFANTIL", "OTROS"]

    for i in range(len(v)):

        codigo = generador_ISBN()
        titulo = Titulos(libro).upper()
        genero = psg.choice(genero_)
        idioma = lista_idiomas[k].upper()
        precio = psg.randint(1000, 5000)

        if libro == 25 or libro == 51 or libro == 67 or libro == 94:
            k += 1

        libro += 1

        v[i] = Libros(codigo, titulo, genero, idioma, precio)


#   FUNCION PARA ORDENAR LA LISTA.


def mostrar_ascendente(v, bandera, genero):
    """
    :param v: arreglo de los libros cargados.
    :param bandera: bandera para determinar el tipo de ordenamiento que ejecutara-False: ordenar
    libros por precio del genero con mayor cant. Libros.; True: ordenar el arreglo en orden alfabetico.
    :param genero: generos de libro.

    """
    n = len(v)

    if bandera:
        for i in range(n - 1):
            for j in range(i + 1, n):
                if v[i].titulo > v[j].titulo:
                    v[i], v[j] = v[j], v[i]

    else:
        for i in range(n - 1):
            if v[i].genero == genero:
                for j in range(i + 1, n):
                    if v[j].genero == genero:
                        if v[i].precio < v[j].precio:
                            v[i], v[j] = v[j], v[i]

        print("\x1b[4;35m" + "\n GENERO CON MAYOR CANTIDAD DE LIBROS IDENTIFICADOS EN EL PUNTO 3: " + "\033[0;m")
        print("*" * 100)

        for i in range(n):
            if v[i].genero == genero:
                print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format("\x1b[2;34m" + "\n Codigo: ", v[i].codigo,
                                                            " | ", "Titulo: ", v[i].titulo, " | ", "Genero: ",
                                                            v[i].genero, " | ", "Idioma: ", v[i].idioma, " | ",
                                                            "Precio: ", "$ " + str(v[i].precio)))


#   FUNCION PARA VALIDAR LA CORRECTA CARGA DEL IDIOMA.


def validar_idioma(mensaje):
    """
    :param mensaje: mensaje para la carga.

    """
    idioma = ["ESPAÑOL", "INGLES", "FRANCES", "ITALIANO", "OTROS"]

    bandera_codigo_pais = False
    n = None
    while not bandera_codigo_pais:

        print("")
        n = input(mensaje).upper()

        for i in range(len(idioma)):
            if idioma[i] == n:
                bandera_codigo_pais = True

        if bandera_codigo_pais:
            return n
        else:
            print("\x1b[0;33m" + "[?] Ingrese correctamente el idioma, puede copiarlo de la lista de arriba." + "\033[0;m")

#   FUNCION PARA BUSCAR EL MAYOR PRECIO DE UN LIBRO PARA UN IDIOMA.


def buscar_mayor(n, v):
    """
    :param n: idioma ingresado por teclado.
    :param v: arreglo de libros.
    :return: retorna la posicion en memoria.

    """
    mayor = 0
    idioma = False
    memoria = None

    for i in range(len(v)):

        if v[i].idioma == n:
            idioma = True  # ver modificar - bandera

            if mayor < v[i].precio:
                mayor = v[i].precio
                memoria = i

    if idioma:
        return memoria
    else:
        return None


#   FUNCION PARA LA BUSQUEDA DE ISBN.


def busqueda_por_isbn(v):
    """
    :param v: arreglo de libros.
    """

    codigo = validar_isbn_manual("\x1b[3;36m" + "Ingresar codigo ISBN a buscar: \n")

    for i in range(len(v)):

        if v[i].codigo == codigo:
            print("\x1b[0;33m" + "Precio anterior:", "$ " + str(v[i].precio) + ".\n")

            v[i].precio = v[i].precio + v[i].precio * 0.1

            print("{}{}{}{}{}{}{}{}{}{}{}".format("\x1b[2;34m" + "\n Se encontro el libro: ", v[i].titulo,
                                                  " | ", "Genero: ", v[i].genero, " | ", "Idioma: ", v[i].idioma, " | ",
                                                  "Precio actualizado: ", "$ " + str(v[i].precio) + "."))

            return
    print("\x1b[0;33m" + "[?] No se encontro un libro con el codigo:", codigo + "." + "\033[0;m")


#   FUNCION PARA LA CONSULTA POR PRECIO.


def Consulta_de_precio_por_grupo(v):
    """
    Permite  cargar el listado de los ISBN's por teclado, verifica que sean codigos validos y busca cuáles de
    estos libros se encuentran en su catálogo mostrandolos o informando en caso de no ser encontrados.
    :param v: arreglo de libros.
    """
    cant = validar_positivo(False, "\x1b[3;36m" + "¿Cuantos codigos va a cargar?: \n")

    arreglo = [0] * cant
    posT = posF = total = 0
    direccion_en_vector_total = no_encontrados = []

    for i in range(cant):
        arreglo[i] = validar_isbn_manual("\x1b[3;36m" + "Ingresar el codigo a buscar: \n")

    for i in range(len(arreglo)):

        encontrados_direccion = validar_en_memoria_automatico(v, False, arreglo[i])

        if encontrados_direccion is not None:
            if posT == 0:

                direccion_en_vector_total = [encontrados_direccion]
                posT += 1

            else:

                direccion_en_vector_total.append(encontrados_direccion)
        else:

            if posF == 0:

                no_encontrados = [arreglo[i]]
                posF += 1

            else:
                no_encontrados.append(arreglo[i])

    if len(direccion_en_vector_total) > 0:

        for i in range(len(direccion_en_vector_total)):
            print("\x1b[2;34m" + "\nSe encontro el codigo: " + v[direccion_en_vector_total[i]].codigo, end=" | ")
            print("Titulo: " + v[direccion_en_vector_total[i]].titulo, end=" | ")
            print("Precio: $", v[direccion_en_vector_total[i]].precio)

            total += int(v[direccion_en_vector_total[i]].precio)

        if total > 0:
            print("\x1b[4;35m" + "PRECIO TOTAL: " + "$ " + str(total) + "." + "\033[0;m")
    else:
        print("\x1b[0;33m" + "[?] Ninguno de los codigos ISBN que ingreso se encuentran en el catalogo." + "\033[0;m")

    if len(no_encontrados) > 0:

        for i in range(len(no_encontrados)):
            print("\x1b[2;33m" + "Codigos no encontrados: ", str(no_encontrados[i]) + ".")


#   FUNCION PARA VALIDAR QUE EL VALOR INGRESADO SEA POSITIVO.


def validar_positivo(bandera, mensaje="Ingresar una cantidad (superior a cero): "):
    """
    :param bandera: True: valida precio superior a cero; False: valida cantidad de codigos isbn a ingresar por teclado.
    :param mensaje: mensaje para la carga.
    :return: valor cargado.
    """
    num = 0

    while num <= 0:

        if bandera:
            num = float(input(mensaje))

            if num <= 0:
                print("\x1b[0;31m" + "[!] No puede ser un valor inferior o igual a 0(cero)." + "\033[0;m")

        else:
            num = int(input(mensaje))

            if num <= 0:
                print("\x1b[0;31m" + "[!] No puede ser un valor inferior o igual a 0(cero)." + "\033[0;m")
    return num


#   FUNCION PARA EL MENU DE OPCIONES, DONDE SE INICIALIZAN ALGUNAS VARIABLES.


def menu():
    print("\n-------------------REGISTRO DE LIBRERIA-------------------")

    n = validate(0, "\x1b[3;36m" + "\nCantidad de libros que ofrece la libreria: " + "\033[0;m", "\x1b[0;31m" + "[!] El valor ingresado es incorrecto." + "\033[0;m",
                 "\x1b[0;33m" + "[?] Solo se disponen de 115 libros." + "\033[0;m")

    v = [None] * n
    control_menu_bandera = False

    mensaje_advertencia = "\x1b[0;31m" + "[!] Debes cargar los datos de los libros antes..." + "\033[0;m"

    mensaje_idioma ="\x1b[1;32m" + "Ingresar el idioma del libro que deseas conocer el mayor precio:\n" \
                    "\x1b[1;35m" + "Lista de idiomas: (Español - Ingles - Frances - Italiano - Otros)\n" + "\033[0;m"

    punto3 = ["AUTOAYUDA", "ARTE", "FICCION", "COMPUTACION", "ECONOMIA", "ESCOLAR", "SOCIEDAD",
              "GASTRONOMIA", "INFANTIL", "OTROS"]

    genero_max_cant = None

    opc = "1"

    while opc != "8":

        print("\x1b[1;31m" + "╔══════════════════════════════════════════════════╗"
              "\x1b[3;33m" + "\n                -MENU DE OPCIONES-\n"
              "\x1b[1;31m" + " ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
              "\x1b[2;36m" + "➣ 1 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Generacion y carga.\n"
              "\x1b[2;36m" + "➣ 2 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Mostrar.\n"
              "\x1b[2;36m" + "➣ 3 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Conteo y genero mas popular.\n"
              "\x1b[2;36m" + "➣ 4 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Busqueda de mayor.\n"
              "\x1b[2;36m" + "➣ 5 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Busqueda por ISBN.\n"
              "\x1b[2;36m" + "➣ 6 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Consulta de un genero.\n"
              "\x1b[2;36m" + "➣ 7 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Consulta de precio por grupo.\n"
              "\x1b[2;36m" + "➣ 8 ╴ ╴ ╴ ╴ ╴ ╴ ╴   Salir."
              "\x1b[1;31m" + "\n╚══════════════════════════════════════════════════╝")

        opc = input("{:>40}".format("\x1b[3;36m" + ">>> [Ingrese su opcion:] <<< "))

        if opc == "1":

            control_menu_bandera = True

            eleccion = input("\x1b[3;36m" + "¿ Desea cargar de forma manual o automatica ? (Ingrese 'M' o 'A'): ")

            if eleccion.upper() == "M":
                cargar_libros(v, False)

            else:
                bandera_memoria = False

                while not bandera_memoria:
                    cargar_libros(v, True)
                    bandera_memoria = validar_en_memoria_automatico(v, True, 0)


        elif opc == "2":

            if not control_menu_bandera:
                print(mensaje_advertencia)

            else:
                mostrar_ascendente(v, True, None)
                write(v)

        elif opc == "3":

            if not control_menu_bandera:
                print(mensaje_advertencia)

            else:
                genero_max_cant = contador_por_genero(v, punto3)

        elif opc == "4":

            if not control_menu_bandera:
                print(mensaje_advertencia)

            else:
                mayor_precio_idioma = buscar_mayor(validar_idioma(mensaje_idioma), v)
                if mayor_precio_idioma is not None:

                    print("\x1b[2;34m" + "Titulo: ", v[mayor_precio_idioma].titulo + " | " + " Idioma: ",
                          v[mayor_precio_idioma].idioma, "| Precio: " + "$", v[mayor_precio_idioma].precio)

                else:
                    print("\x1b[0;31m" + "[!] El libro del idioma ingresado no existe." + "\033[0;m")

        elif opc == "5":

            if not control_menu_bandera:
                print(mensaje_advertencia)

            else:
                busqueda_por_isbn(v)

        elif opc == "6":

            if not control_menu_bandera:
                print(mensaje_advertencia)

            else:

                if genero_max_cant is None:
                    print("\x1b[0;33m" + "[?] Primero, debes ejecutar el punto 3, luego, con esos datos podremos consultar segun el genero..." + "\033[0;m")
                else:
                    mostrar_ascendente(v, False, genero_max_cant)

        elif opc == "7":

            if not control_menu_bandera:
                print(mensaje_advertencia)

            else:
                Consulta_de_precio_por_grupo(v)


        elif opc == "8":
            print("\x1b[0;31m" + "Programa terminado." + "\033[0;m")

        else:
            print("\x1b[0;31m" + "[!] Opcion incorrecta." + "\033[0;m")
