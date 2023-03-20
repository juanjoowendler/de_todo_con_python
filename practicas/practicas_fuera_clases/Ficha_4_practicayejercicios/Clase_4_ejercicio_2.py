__author__ = "Wendler Juan Jose"

print("Suma - División - Potencia: ")

# Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10
# dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
c = int(input("Tercer numero: "))

sum = a + b + c

if sum > 10:
    print("Es mayor a 10 la suma, dividimos por dos.")
    div = sum//10
    print("El resultado es: ", div)
else:
    print("Es menor a 10 la suma, elevamos al cubo")
    elv = sum**3
    print("El resultado es: ", elv)


