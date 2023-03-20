import clase


def main():
    juego = clase.Juego(3, 3, r="*")
    juego.crear_tablero()

    print("\n\t\tTa Te Ti")
    print("*"*25, end="\n\nInstrucciones - filas(0-2) | columnas(0-2)\n"
                      "Debes de colocar las coordenadas del tablero.")
    print()
    juego.mostrar_tablero()
    print()

    jugador_1 = clase.control_nombre(format("{} primer "))
    jugador_2 = clase.control_nombre(format("{} segundo "))

    ganador = False
    cantidad = 0

    while not ganador:
        cantidad += 1
        if cantidad % 2 == 0:
            print(f"\nLe toca a {clase.get_colores(jugador_1, 'red')}.", end="\n\n")
            tiro_1 = False
            while not tiro_1:
                tiro_1 = juego.colocar_x()
            juego.mostrar_tablero()

        else:
            print(f"\nLe toca a {clase.get_colores(jugador_2, 'blue')}", end="\n\n")
            tiro_2 = False
            while not tiro_2:
                tiro_2 = juego.colocar_x(ban=True)
            juego.mostrar_tablero()

        ganador = juego.control_ganador()

    if cantidad % 2 == 0:
        print(f"\t - Ganó el jugador: {clase.get_colores(jugador_1, 'red')}")
    else:
        print(f"\t - Ganó el jugador: {clase.get_colores(jugador_2, 'blue')}")

    print("[Juego terminado]")


if __name__ == "__main__":
    main()
