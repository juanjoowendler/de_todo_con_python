# Gestionar las notas de los n alumnos de un curso
# en un parcial. Para ello se pide:

# 1) Ingresar en un arreglo las n notas, n se ingresa por teclado.
# Las notas son un valor entre 0-10
# 2) Determinar la nota promedio obtenida.
# 3) Mostrar índice y nota de alumnos que obtuvieron una nota
# mayor al promedio.
# 4) Determinar la nota promedio entre los que aprobaron el
# parcial (se aprueba con nota >= 4)
# 5) Buscar la menor nota (si hubiera más de una,
# responder sólo una).


def validate(mensaje, mensaje_error):
    n = -1
    while n <= 0:
        n = int(input(mensaje))
        if n <= 0:
            print(mensaje_error)
            continue
    return n


def carga_notas(n, mensaje):
    notas = list()
    for i in range(1, n + 1):
        nota = validate(mensaje, "Nota incorrecta.")
        notas.append(nota)
    return notas


def suma_total(n):
    suma = 0
    for elemento in n:
        suma += elemento
    return suma


def promedio(total, suma):
    if total == 0:
        return 0
    return round(suma/total, 2)


def mayor_al_promedio(prom, notas):
    mayores = list()
    for i in notas:
        if i > prom:
            mayor = i
            mayores.append(mayor)
    return mayores


def aprobados(notas):
    aprobados = list()
    for i in notas:
        if i >= 4:
            aprobados.append(i)
    return suma_total(aprobados)


def test():
    n = validate("Ingresar cantidad de alumno: ", "Error ! Ingrese mayor a 0.")
    notas = carga_notas(n, "Ingresar nota ")
    sum = suma_total(notas)
    prom = promedio(n, sum)
    mayor = mayor_al_promedio(prom, notas)
    aprobadoss = aprobados(notas)
    print("Las notas ingresadas son:", notas)
    print("El promedio de notas es:", prom)
    print("Indice de notas mayor al promedio: ", mayor)
    print("Promedio de los que aprobaron: ", promedio(notas, aprobadoss))

if __name__ == "__main__":
    test()
