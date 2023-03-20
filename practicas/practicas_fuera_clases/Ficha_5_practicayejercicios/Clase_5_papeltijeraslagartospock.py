__author___ = "Wendler Juan Jose"

import random
print("*"*50)
print("\t\tA PAPEL TIJERAS LAGARTO SPOCK:")
print("*"*50)
jugador_1 = input("\nIngresar el nombre del primer jugador: ")
jugador_2 = input("Ingresar el nombre del segundo jugador: ")

opciones = ("Piedra", "Papel", "Tijeras", "Lagarto", "Spock")
opc_usr = int(input("\nIngrese su opcion: 0 = Piedra, 1 = Papel, 2 = Tijeras, 3 = lagarto, 4 = spock "))
opciones_pc = random.choice(opciones)
opcion_usuario = opciones[opc_usr]

if opciones_pc == opcion_usuario:
    ganador = "Empate"
else:
    if (opcion_usuario == "Papel" and opciones_pc == "Piedra") or (opcion_usuario == "Piedra" and opciones_pc  == "Tijera") or \
        (opcion_usuario == "Tijera" and opciones_pc == "Papel") or (opcion_usuario == "Piedra" and opciones_pc == "Lagarto") or \
        (opcion_usuario == "Lagarto" and opciones_pc == "Spock") or (opcion_usuario == "Spock" and opciones_pc == "Tijeras") or \
        (opcion_usuario == "Tijeras" and opciones_pc == "Lagarto") or (opciones_pc == "Lagarto" and opciones_pc == "Papel") or \
        (opcion_usuario == "Papel" and "Spock") or (opcion_usuario == "Spock" and opciones_pc == "Piedra") or \
            (opcion_usuario == "Spock" and opciones_pc == "Piedra"):
        ganador = "Ganaste"
    else:
        ganador = "Perdiste"


print("-Opcion de la PC: ", opciones_pc)
print("-Opcion del usuario: ",opcion_usuario)
resultado = print("\n\t\tResultado: ", ganador)
