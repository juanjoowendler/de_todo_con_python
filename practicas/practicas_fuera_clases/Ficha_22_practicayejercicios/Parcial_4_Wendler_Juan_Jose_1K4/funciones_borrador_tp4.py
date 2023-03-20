def busqueda_titulo(libros, titulo):
    pos = 0
    for i in range(len(libros)):
        if libros[i].titulo == titulo:
            libros[i].revision += 1
            pos = i
            return pos
        else:
            return -1


def mayor_revision(libros):
    may = 0
    pos = -1
    for i in range(len(libros)):
        if libros[i].revision > may:
            may = libros[i].revision
            pos = i
    return pos


