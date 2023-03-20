__author__ = "Wendler Juan Jose"

print("Tirada de moneda: ")

# Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente.
# Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.


import random

cara_moneda = random.randint(0, 2)

apuesta = input("Apuestas cara o cruz: ")

if apuesta == "cara" and cara_moneda == 0:
    print("Salio cara, felicidades !")
elif apuesta == "cruz" and cara_moneda == 1:
    print("Salio cruz, felicidades !")
else:
    print("No salio la cara que apostaste...")
