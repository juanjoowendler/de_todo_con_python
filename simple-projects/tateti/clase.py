import juego


colores = {
    "red": "\033[31m",
    "blue": "\033[34m",
    "_end": "\033[39m"
}


def get_colores(valor, color):
    return colores[color] + valor + colores["_end"]


def control_nombre(valor):
    nombre = ""
    while len(nombre) == 0:
        nombre = input("Nombre del "+valor.format("")+"jugador: ")

    return nombre


class Juego:
    def __init__(self, f, c, tablero="", r=0):
        self.filas = f
        self.columnas = c
        self.relleno = r
        self.tablero = tablero

    def crear_tablero(self):
        self.tablero = [[self.relleno] * self.columnas for _ in range(self.filas)]

    def mostrar_tablero(self):
        for filas in range(len(self.tablero)):
            print("")
            for columnas in range(len(self.tablero[filas])):
                print(f"{self.tablero[filas][columnas]}", end=" ")
        print()

    def colocar_x(self, ban=False):
        fila = 4
        while fila > 2 or fila < 0:
            fila = int(input("fila: "))
            if fila > 2 or fila < 0:
                continue

            columna = 4
            while columna > 2 or columna < 0:
                columna = int(input("columna: "))
                if columna > 2 or columna < 0:
                    continue

        if not ban:
            if self.tablero[fila][columna] == get_colores("o", "blue"):
                print("\n[!] Lugar ocupado.")

                return False
            else:
                self.tablero[fila][columna] = get_colores("x", "red")

                return True

        elif self.tablero[fila][columna] == get_colores("x", "red"):
            print("\n[!] Lugar ocupado.")

            return False
        else:
            self.tablero[fila][columna] = get_colores("o", "blue")

            return True

    def control_ganador(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == get_colores("o", "blue") or \
                    self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == get_colores("x", "red"):

                return True

        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] == get_colores("o", "blue") or \
                    self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] == get_colores("x", "red"):

                return True

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == get_colores("o", "blue") or \
                self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == get_colores("x", "red"):

            return True

        elif self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == get_colores("o", "blue") or \
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == get_colores("x", "red"):

            return True


if __name__ == "__main__":
    juego.main()

