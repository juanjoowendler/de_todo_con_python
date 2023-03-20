__author__ = "Wendler Juan Jose"

print("Polinomio de segundo grado: ")

# Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
# y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado).
# Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la
# fórmula para el cálculo de las raíces de la ecuación.

x = float(input("\nValor de la variable x: "))
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
discriminante = b**2 - 4 * a * c

polinomio = a * (x**2) + b * x + c

print("discriminante: ", discriminante, "y polinomio: ", polinomio)

