__author__ = "Wendler Juan Jose"

# Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

#      1.) Ingrese los tiempos en segundos insumidos por tres barcos en una regata. Sin usar las funciones
#      predefinidas min() y max(), determine y muestre el tiempo del ganador. Calcule y muestre las diferencias
#      entre el tiempo del ganador y el tiempo de los otros dos.

#      2.) Ingrese por teclado una secuencia de n números enteros (n se carga por teclado), a razón de uno
#      por vuelta de ciclo. Determine el promedio de todos los números cargados que hayan sido  múltiplos de
#      3. Informe si ese promedio menor, igual o mayor que el promedio de todos los números cargados.

#      3.) Ingrese por teclado una cadena de caracteres. Recorriendo la cadena caracter por caracter e
#      informe la suma de todos los dígitos de la cadena.

#      4.) Terminar el programa.


print("\n\t   MENU DE OPCIONES\n\t  ◝──────•❈•──────◜")

img_opc = "\n ╔════════ ≪ •❈• ≫ ═════════╗\n\t1.➢Opcion 1\n\t2.➢Opcion 2\n\t3.➢Opcion 3\n\t4.➢Opcion 4\n " \
          "╚════════ ≪ •❈• ≫ ═════════╝ \n\n💡 Si ingresa una opcion fuera del rango el programa terminara."

print(img_opc)
opc = int(input("\nIngresar su opcion ➢ "))

while opc != 4 and 0 < opc < 5:
    if opc == 1:
        tBar1 = int(input("Tiempo del primer barco: "))
        tBar2 = int(input("Tiempo del segundo barco: "))
        tBar3 = int(input("Tiempo del tercer barco: "))

        if tBar1 > tBar2 and tBar1 > tBar3:
            may = tBar1
            if tBar2 > tBar3:
                men = tBar3, "3"
                med = tBar2, "2"
            else:
                men = tBar2, "2"
                med = tBar3, "3"
        if tBar2 > tBar1 and tBar2 > tBar3:
            may = tBar2
            if tBar1 > tBar3:
                men = tBar3, "3"
                med = tBar1, "1"
            else:
                men = tBar1, "1"
                med = tBar3, "3"
        if tBar3 > tBar2 and tBar3 > tBar1:
            may = tBar3
            if tBar1 > tBar2:
                men = tBar2, "2"
                med = tBar1, "1"
            else:
                men = tBar1, "1"
                med = tBar2, "2"

            difMenMay = (may + med[0]) - men[0]
            print("\nEl tiempo ganador es para el barco", men[1], "con un tiempo de", men[0], "segundos.")
            print("La diferencia entre el menor tiempo y el tiempo de los otros dos barcos es de", difMenMay, "segundos.\n"
                    "Siendo el tiempo medio de", med[0], "segundos y el tiempo mayor de", may, "segundos.")
        else:
            print("\n! Todos los tiempos fueron iguales.")

        print(img_opc)
        opc = int(input("\nIngresar otra opcion ➢ "))

    elif opc == 2:
            cantidad = int(input("¿Cuantos numeros desea cargar?: "))
            mul3 = acuNcargados = 0
            for num in range(cantidad):
                n = int(input("Ingresar n°: "))
                if n % 3 == 0:
                    mul3 += num
                else:
                    acuNcargados += num

            if mul3 == 0 and acuNcargados == 0 or acuNcargados == 0:
                prom = 0
            else:
                prom = mul3 / acuNcargados

            print("\nEl promedio entre n° multiplos de 3 y el total de n° cargados es de: ", prom)
            if prom > acuNcargados:
                print("\nEl promedio es mayor al total de n's° cargados.")
            elif prom == acuNcargados:
                print("\nEl promedio es igual al total de n's° cargados.")
            else:
                print("\nEl promedio es menor al total de n's° cargados.")

            print(img_opc)
            opc = int(input("\nIngresar otra opcion ➢ "))

    elif opc == 3:
        acudig = 0
        texto = input("Ingresar un texto para recorrer: ")
        for caracter in texto:
            if caracter >= "0" and caracter <= "9":
                num_que_representa_caracter = int(caracter)
                acudig += num_que_representa_caracter

        print("La suma de todos los digitos de la cadena es de: ", acudig)

        print(img_opc)
        opc = int(input("\nIngresar otra opcion ➢ "))

else:
    print("\n\t\tFin del programa 🤠...")



