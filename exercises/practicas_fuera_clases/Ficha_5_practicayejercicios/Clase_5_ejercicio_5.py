__author__ = "Wendler Juan Jose"

# Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:
#
# Si la opción es 1 mostrar la superficie de un triángulo. Para calcular la superficie debe usarse la fórmula de Herón:
#
# Si la opción ingresada es 2 mostrar el perímetro del triángulo.
# Si la opción ingresada es 3 informar la longitud del lado menor.
# Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.
# Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.


print("\t\t\tMenu de opciones: ")
print("*" * 60)

print("-Ingresar los lados antes de comenzar: ")
lado1 = int(input("\nIngresar el primero de los lados: "))
lado2 = int(input("Ingresar el segundo de los lados: "))
lado3 = int(input("Ingresar el tercero de los lados: "))

opc = int(input("\n\t\t¿Que operacion desea realizar? \n\t1. Superficie de un triangulo \t2. Perimetro del triangulo"
                "\t3. Longitud del lado menor -> "))
tr_sup = (lado1 + lado2 + lado3) / 2

if opc == 1:
    result = (tr_sup*(tr_sup - lado1)*(tr_sup - lado2)*(tr_sup-lado3))**0.5
    round(result, 2)
    print("El perimetro del triangulo es de: ", str(result) + ".")
elif opc == 3:
   if lado1 < lado2 and lado1 < lado3:
       men = lado1
   elif lado2 < lado1 and lado2 < lado3:
       men = lado2
   else:
       men = lado3
       print("El menor de los lados es: ", str(men) + ".")
elif opc == 2:
    tr_per = lado1 + lado2 + lado3
    print("El perimetro del triangulo es de: ", str(tr_per) + ".")
else:
    print("La opcion es erronea, fin del programa...")

