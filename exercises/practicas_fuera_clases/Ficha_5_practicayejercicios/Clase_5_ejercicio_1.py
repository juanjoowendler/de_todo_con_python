__author__ = "Wendler Juan Jose"

# Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es el
# resto de la división de los dos primeros.

print("Operaciones de orden con 3 nros: ")

a = int(input("\nIngresar el primer numero: "))
b = int(input("Ingresar el segundo numero: "))
c = int(input("Ingresar el tercer numero: "))

if a > b and a > c:
    may = a
    if b > c:
        men = c
        med = b
    else:
        men = b
        med = c
    print("mayor: ", str(may) + ".")
    print("mediano: ", str(med) + ".")
    print("menor: ", str(men) + ".")

else:
    if b > c and b > a:
        may = b
        if a > c:
            men = c
            med = a
        else:
            men = a
            med = c
        print("mayor: ", str(may) + ".")
        print("mediano: ", str(med) + ".")
        print("menor: ", str(men) + ".")

    else:
        if c > a and c > b:
            may = c
            if a > b:
                men = b
                med = a
            else:
                men = a
                med = b
            print("mayor: ", str(may) + ".")
            print("mediano: ", str(med) + ".")
            print("menor: ", str(men) + ".")

if a == b == c:
    print("Los tres numeros son iguales.")
else:
    if a == b != c:
        print("El primer numero es igual al segundo")
    else:
        if a == c != b:
            print("El primer numero es igual al tercero")

if a != b != c:
    print("Todos los numeros fueron distintos.")

res = a % b

if c == res:
    print("El tercer numero es igual al resto de dividir el primero entre el segundo.")


