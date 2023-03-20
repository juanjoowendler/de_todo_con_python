author = "Wendler  Juan Jose"

import random

print("\n\t\tPIEDRA, PAPEL O TIJERAS:")

jugador_1 = input("\nIngresar el nombre del primer jugador: ")
jugador_2 = input("Ingresar el nombre del segundo jugador: ")

opciones = ("piedra", "papel", "tijeras")
opc_usr = int(input("\nIngrese su opcion: 0 = Piedra, 1 = Papel, 2 = Tijeras: "))
opciones_pc = random.choice(opciones)
opcion_usuario = opciones[opc_usr]

if opciones_pc == opcion_usuario:
    ganador = "Empate"
else:
    if (opcion_usuario == "Papel" and opciones_pc == "Piedra") or (opcion_usuario == "Piedra" and opciones_pc  == "Tijera") or \
        (opcion_usuario == "Tijera" and opciones_pc == "Papel"):
        ganador = "Ganaste"
    else:
        ganador = "Perdiste"

print("-Opcion de la PC: ", opciones_pc)
print("-Opcion del usuario: ",opcion_usuario)
resultado = print("\n\t\tResultado: ", ganador)
