# Longitudes Menores
# Cargar por teclado una frase separada por espacios y termina
# con un punto (el cual no forma parte de la frase a procesar).

# Se debe establecer cuántas palabras de la frase están antecedidas
# por otra palabra de menor o igual longitud (la primer palabra de la
# frase nunca podrá ser contabilizada ya que no posee palabra antecesora).

# Por ejemplo, la frase “Este es un ejercicio un poco complicado.”
# tiene 4 palabras cuya antecesora es igual o más corta en longitud
# (“un”, “ejercicio”, “poco”, “complicado”).


def main():
    texto = input("Ingrese la frase a procesar: ")
    texto = texto.lower()

    cant_let_pal = cant_let_anterior = cantidad_palabras = 0
    for car in texto:
        if car != " " and car != ".":
            cant_let_pal += 1
        else:
            if cant_let_anterior != 0 and cant_let_anterior <= cant_let_pal:
                cantidad_palabras += 1

            cant_let_anterior = cant_let_pal
            cant_let_pal = 0

    print(f"Hay {cantidad_palabras} cantidad de palabras antecedidas por otra de menor cantidad.")


if __name__ == "__main__":
    main()
