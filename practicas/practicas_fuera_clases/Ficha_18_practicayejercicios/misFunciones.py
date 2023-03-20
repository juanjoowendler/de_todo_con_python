"""
v1.2.5
"""
import random


# validación
def cargar_entre(desde, hasta, mensaje="Ingrese un valor:"):
    val = int(input(mensaje))
    while val < desde or val > hasta:
        print("Error, el valor debe estar entre", desde, "y", hasta, "!")
        val = int(input(mensaje))
    return val


def cargar_mayor_que(valor, mensaje="Ingrese un valor:"):
    num = int(input(mensaje))
    while num <= valor:
        print('Error, debe ingresar un valor mayor que', valor)
        num = int(input(mensaje))
    return num


def cargar_nombre(mensaje='Ingrese un nombre:'):
    nombre = input(mensaje)
    while len(nombre) == 0:
        print("Error en el texto ingresado.")
        nombre = input(mensaje)
    return nombre


def cargar_texto(mensaje='Ingrese un texto (finaliza con punto):'):
    texto = input(mensaje)
    while len(texto) == 0 or texto[-1] != '.':
        print("Error en el texto ingresado.")
        texto = input(mensaje)
    return texto


# caracteres
def es_digito(car):
    return car in "0123456789"


def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"


def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


def es_letra(car):
    return es_vocal(car) or es_consonante(car)


def es_mayuscula_v1(car):
    return car in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def es_mayuscula_v2(car):
    return es_letra(car) and car == car.upper()


# generar nombres
def generar_nombre():
    nombres = "Juan", "Pedro", "Pablo", "Raúl", "José", "Sara", "María", "Julia", "Marta", "Paula"
    apellidos = "Perez", "Gomez", "Rodriguez", "Gimenez", "Lopez", "Rinaldi", "Estevez", "Etchegaray", "Martinez", "Juarez"
    res = random.choice(nombres) + " " + random.choice(apellidos)
    return res


# arreglos / vectores
def generar_vector_enteros(cant_elem, desde=0, hasta=99):
    v = [0] * cant_elem
    for i in range(len(v)):
        v[i] = random.randint(desde, hasta)
    return v


def select_sort_asc(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def busqueda_binaria_asc(v, x):
    izq = 0
    der = len(v) - 1
    c = (izq + der) // 2
    while izq <= der and x != v[c]:
        if x > v[c]:
            izq = c + 1
        else:
            der = c - 1
        c = (izq + der) // 2
    if izq > der:
        res = -1
    else:
        res = c
    return res


def add_in_order(vec, x):
    n = len(vec)
    pos = n
    izq = 0
    der = n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c] == x:
            pos = c
            break
        if x < vec[c]:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [x]


# función de prueba
def prueba():
    pass


# script principal
if __name__ == '__main__':
    prueba()
