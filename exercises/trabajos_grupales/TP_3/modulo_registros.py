
#   REGISTRO DE LIBROS.


class Libros:
    def __init__(self, cod, tit, gen, idiom, prec):
        """
        Crea un registro de los libros con los valores que
        se le envian como parametro.

        :param cod: codigo de identificacion del libro.
        :param tit: titulo del libro.
        :param gen: genero del libro.
        :param idiom: idioma del libro.
        :param prec: precio del libro.
        """
        self.codigo = cod
        self.titulo = tit
        self.genero = gen
        self.idioma = idiom
        self.precio = prec


#   FUNCION PARA MOSTRAR LOS DATOS DE LOS LIBROS.


def write(v):
    """
    :param v: arreglo de libros.

    """

    print("{:^50}".format("\nCATALOGO DE LIBROS:\n"))

    for i in range(len(v)):

        print("{:<20} {:<35} {:<20} {:<20} {:<20} {:<20}".format("\x1b[2;33m" + "", "---Titulo---", "---Genero---", "---Idioma---",
        "---Precio---", " ---Codigo---"))
        print("{:<20} {:<35} {:<20} {:<20} {:<20}".format("\x1b[1;35m" + "Libro[" + str(i) + "]", v[i].titulo.upper(), v[i].genero,
        v[i].idioma, "$ " + str(v[i].precio)), v[i].codigo)
        print()


#   FUNCION PARA DETERMINAR EL TIPO DE GENERO.


def contador_por_genero(v, orden):

    """
    :param orden: distintos tipos de genero: "Autoayuda" - "Arte" - "Ficción" - "Computación" - "Economía" - "Escolar"
                - "Sociedad" - "Gastronomía" - "Infantil" - "Otros"

    :param v: arreglo de libos

    :genero_ordenado: arreglo que acumula la cantidad de libros segun su genero.

    :return: arreglo con la cantidad de libro por genero.
    """
    genero_ordenado = [0] * 10


    for i in range(len(v)):
        if v[i].genero == "AUTOAYUDA":
            genero_ordenado[0] += 1

        elif v[i].genero == "ARTE":
            genero_ordenado[1] += 1

        elif v[i].genero == "FICCION":
            genero_ordenado[2] += 1

        elif v[i].genero == "COMPUTACION":
            genero_ordenado[3] += 1

        elif v[i].genero == "ECONOMIA":
            genero_ordenado[4] += 1

        elif v[i].genero == "ESCOLAR":
            genero_ordenado[5] += 1

        elif v[i].genero == "SOCIEDAD":
            genero_ordenado[6] += 1

        elif v[i].genero == "GASTRONOMIA":
            genero_ordenado[7] += 1

        elif v[i].genero == "INFANTIL":
            genero_ordenado[8] += 1

        else:
            genero_ordenado[9] += 1


    indice = ""
    maximo = max(genero_ordenado)

    for i in range(len(genero_ordenado)):

        if genero_ordenado[i] == maximo:
            indice = i

    print()
    for i in range(len(genero_ordenado)):

        print("\x1b[2;33m" + "{:<10} {:<20} {:<20}".format(" ", "---Genero---", "---Cantidad---"))
        print("{:<10} {:<20} {:<20} ".format(" ", orden[i], genero_ordenado[i]))
        print()

    mayor_generos = orden[indice]

    print("\x1b[2;32m" + "Genero con mayor cantidad de libros ofrecidos: ", mayor_generos + ".")

    return orden[indice]
