__author__ = "Wendler Juan Jose"


def promedio(a, b):
    if longitud != 0:
        prom = a / b
    else:
        prom = 0
    return prom


print("\n\t\tSucecion de Collatz")
print("*"*35)

acuvalores = 0

num = int(input("\n-Ingresar el n° a iterar -> "))

while num <= 0:
    print("¡Se pidio cargar un numero positivo, ingrese nuevamente!...")
    num = int(input("-Ingresar el n° a iterar -> "))

orbita = [num]
acuvalores += num

while num != 1:
    if num % 2 == 0:
        num = num // 2
        orbita.append(num)
    else:
        num = (num * 3) + 1
        orbita.append(num)

    acuvalores += num

longitud = len(orbita)
promm = promedio(acuvalores, longitud)

mayor = max(orbita)

print("\n\tEl numero cargado fue el ", orbita[0], end=" ")
print("y su orbita es ", orbita, end="\n")
print("\n\tCantidad de valores cargados: ", longitud)
print("\n\tEl promedio de todos los valores de la orbita es: ", str(round(promm, 1)) + " %")
print("\n\tEl mayor de los numeros de la orbita es el", mayor, end="\n\nfin del programa...")


