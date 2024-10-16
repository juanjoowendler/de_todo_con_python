__author__ = "Wendler Juan Jose"

# Desarrollar un programa completo en Python, que a través de un menu de opciones, ejecute los siguientes puntos:
#
# 1) Ingresar el nombre de tres atletas, ademas ingrese también los tiempos que esos lograron en su actividad
# deportiva (expresados en segundos), informe cual fue el nombre del atleta que gano la competición, ademas
# indicar con un mensaje que si el tiempo del ganador es menor a 850 segundos batió el record de la actividad

# 2) Ingresar un texto, el mismo termina con punto, recorrer el texto caracter a caracter y determinar cuantas
# letras 'p' hay en el texto, cuantas letras 'j' hay en el texto. Ademas indique cual es el porcentaje que cada
# conteo representa sobre el total de caracteres del texto.

# 3) Terminar el Programa


print("\n\t\tMenu de opciones: ")
print("-" * 40)

# opciones
img_opciones = "\n1.- Carrera de atletas \n2.- Analisis de texto \n3.-Terminar programa"

print(img_opciones)
opc = int(input("\nIngresar una opcion: "))
batio_record = False

while opc != 3:
    if opc == 1:
        atlet1 = input("-Ingresar el nombre del primer atleta: ")
        tiem1 = int(input("Tiempo logrado por " + str(atlet1) + ": "))
        atlet2 = input("-Ingresar el nombre del segundo atleta: ")
        tiem2 = int(input("Tiempo logrado por " + str(atlet2) + ": "))
        atlet3 = input("-Ingresar el nombre del tercer atleta: ")
        tiem3 = int(input("-Tiempo logrado por " + str(atlet3) + ": "))

        if tiem1 < tiem2 and tiem1 < tiem3:
          men = tiem1
        elif tiem2 < tiem1 and tiem2 < tiem3:
            men = tiem2
        else:
            men = tiem3

        if men < 850:
            batio_record = True

        if tiem1 == men:
            ganador = atlet1
        elif tiem2 == men:
            ganador = atlet2
        else:
            ganador = atlet3

        print("El ganador de la carrera es: ", ganador, "con un tiempo de: ", str(men) + "s")
        if batio_record:
            print("El tiempo del ganador: ", str(men) + "s", "es menor al tiempo record de 850s, batio record !")
        else:
            print("El tiempo record no fue batido por ninguno de los competidores.")

        print(img_opciones)
        opc = int(input("\nIngresar otra opcion: "))

    else:
        if opc == 2:
            clp = clj = ctl = 0
            texto = input("Ingresar un texto (finaliza con un punto): ")
            for car in texto:
                ctl += 1
                if car == " ":
                    ctl -= 1
                if car == ".":
                    ctl -= 1
                    break
                if car == "p" or car == "P":
                    clp += 1
                else:
                    clp += 0
                if car == "j" or car == "J":
                    clj += 1
                else:
                    clj += 0

            porcp = (clp * 100) / ctl
            porcj = (clj * 100) / ctl
            porcj = round(porcj, 2)
            porcp = round(porcp, 2)
            print("Hay una cantidad de: ", clp, "letras 'p' en el texto ingresado.")
            print("Hay una cantidad de: ", clj, "letras 'j' en el texto ingresado.")
            print("El promedio de letras 'p' por sobre el total de letras en el texto es de: " + str(porcp) + " %.")
            print("El promedio de letras 'j' por sobre el total de letras en el texto es de: " + str(porcj) + " %.")
            print("Cantidad de caracteres: ", str(ctl) + ".")

            print(img_opciones)
            opc = int(input("\nIngresar otra opcion: "))

else:
    print("Fin del programa...")





