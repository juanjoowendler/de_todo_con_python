__author__ = "Wendler Juan Jose"

print("Triángulo Rectángulo: ")

# Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:
#
#     Valor de la hipotenusa (redondeado a 2 decimales)
#
#     Valor del lado mayor
#
#     Valor del lado menor


c1 = float(input("\nIngresar el valor del primer cateto: "))
c2 = float(input("Ingresar el valor del segundo cateto: "))

h = pow(c1**1 + c2**2, 0.5)
lmax = max(c1, c2, h)
lmin = min(c1, c2, h)

print("\nEl valor de la hipotenusa es de: ", str(round(h, 2)) + ".", "\nEl valor del menor de los lados es de: ", str(lmin) + ".", "\n"
      "El valor del mayor de los lados es de: ", str(lmax) + ".")
