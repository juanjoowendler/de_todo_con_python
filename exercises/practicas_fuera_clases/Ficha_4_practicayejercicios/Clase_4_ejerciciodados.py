__author__ = "Wendler Juan Jose"

# Simular un juego en el que se lanzan dos dasos, si ambos dados son
# iguales o la suma entre ellos es impar, gana el usuario. En el caso
# contrario, gana la maquina.

# Resultado: ganador del juego (str)
# Datos: el valor de 2 dados (int) entre (1,6)
# Procesos:
# usuario = "nombre"
# dado 1 = random.randit(1,6)
# dado 2 = random.randrange(1,7)
# suma = dado 1 + dado 2
# if = dado 1 == dado 2 or suma % 2  print("ha ganado: ", usuario)
# else = dado 1 != dado 2 print("ha ganado la maquina ")
# ganador = print(ganador)

# import random

# a = random.random()-----> devuelve un valor flotante
# b = random.randrange (v1,v2)---> valor entero entre v1 y v2, v2 no incluido
# c = random.randint ----> valor entero entre v1 y v2 ambos incluidos

# Valor aleatorio en una tupla
# tupla = ("ganador", "perdedor", "empate")
# resultado = random.choise(tupla)
# cadena = "abcdefghijklmñopqrstuvwxyz"
# letra = random.choise (cadena)---> nos da una letra de la cadena

print("\t\t\nJUEGO DE DADOS:")

jugador = (input("\nIngresar tu nombre de usuario: "))


import random

dado1 = random.randint(1,6)
dado2 = random.randrange(1,7)

print("\n-Valor del dado 1: ", dado1)
print("-Valor del dado 2: ", dado2)

suma = dado1 + dado2

if dado1 == dado2 or suma%dado2 == 1:
    ganador = print("\nGanador: ", jugador)

else:
    ganador = print("\nGanador: PC")

