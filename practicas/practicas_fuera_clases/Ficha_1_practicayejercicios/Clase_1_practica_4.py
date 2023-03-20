__author__ = "Wendler Juan Jose"

print("Últimos dígitos: ")

# ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero?
# ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado,
# y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado)
# [Ayuda: ¿cuáles son los posibles restos que se obtienen de dividir un número cualquiera por 10?]

num = int(input("Cargar el n° entero: "))
unidad = num % 10
decenas = num % 100

print("Ultimo digito: ", str(unidad) + ", ultimos dos digitos: ", decenas)
