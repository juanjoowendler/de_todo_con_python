__author__ = "Wendler Juan Jose"

print("Control electoral: ")

# Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen,
# para cierto candidato: apellido, nombre y cantidad de votos. Luego presentar en pantalla un
# resumen que muestre: iniciales del candidato, cantidad de votos entre paréntesis, y debajo una
# línea con tantas  "x" como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, deberá
# aparecer una línea como esta:  "xxxx"  con cuatro letras "x") (Asumimos que en el centro vecinal
# no hay demasiados electores, de forma que podamos estar seguros que no habrá miles o millones de votos...
# sólo unos pocos para darle sentido al enunciado).

nom = input("Nombre del candidato: ")
apellido = input("Apellido del candidato: ")
cant_v = int(input("Ingresar la cantidad de votos: "))
cant_x = "x" * cant_v
print("RESUMEN: ")
print(nom[0] + apellido[0] + ": " + cant_x)

