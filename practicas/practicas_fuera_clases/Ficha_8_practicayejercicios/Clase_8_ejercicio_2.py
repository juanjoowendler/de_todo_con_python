__author__ = "Wendler Juan Jose"

# Desarrollar un programa completo en Python, que a traves de un menú de opciones, ejecute los siguientes puntos:

# 1) Ingresar una secuencia de números, la carga termina cuando el usuario ingrese el numero 0, determinar
# el acumulado total de todos los números que estén entre los valores 15 y 25, ademas determine cual es la
# cantidad de números pares que se ingresaron. Por ultimo muestre y determine el promedio que se obtiene
# entre los valores acumulados entre 15 y 25 y la cantidad total de números procesados para ese rango

# 2) Ingrese  cantidad de toneladas de granos que tres provincias produjeron, calcule el promedio de granos producidos.
# Luego determine cuantos de esas cantidades superan al promedio.

# 3) Terminar el Programa

print("\n\t\tEjemplo de un menu de opciones: ")
print("-" * 50)

img_opciones = "\n1.➾Secuencia de numeros pares/impares\n2.➾Promedio de granos\n3.➾Salir"
separador = "\n｡.｡:+* ﾟ ゜ﾟ *+:｡.｡:+* ﾟ ゜ﾟ *+:｡.｡.｡:+* ﾟ ゜ﾟ *+:｡.｡:+* ﾟ ゜ﾟ *"

print(img_opciones)
opc = int(input("\nIngresar una opcion: "))

while opc != 3:
    if opc == 1:
        nComprendidos = nPares = nt = 0
        n = int(input("Ingresar n° (finaliza con 0) → "))
        while n != 0:
            n = int(input("Ingresar otro n° (finaliza con 0) → "))
            nt += 1
            if 15 < n < 25:
                nComprendidos += 1
            if n % 2 == 0:
                nPares += 1

        promnComprendidos = nComprendidos / nt
        promnComprendidos = round(promnComprendidos, 2)

        print("\n\tResultados:")
        print("/" * 20)
        print("\n➣La cantidad de n° pares ingresados fue de: ", str(nPares) + ".")
        print("➣La cantidad de n° procesados entre 15-25 fue de: ", str(nComprendidos) + ".")
        print("➣El promedio obtenido entre los valores acumulados de (15-25) y el total de n° es: ",
                promnComprendidos)

        print(separador)
        print(img_opciones)
        opc = int(input("\nIngresar otra opcion: "))

    elif opc == 2:
        Ctoneladas1 = float(input("Ingresar tonelada de granos: "))
        Ctoneladas2 = float(input("Ingresar otra cantidad de tonelada de granos: "))
        Ctoneladas3 = float(input("Ingresar otra cantidad de tonelada de granos: "))

        superan = 0
        promT = (Ctoneladas1 + Ctoneladas2 + Ctoneladas3) / 3
        promT = round(promT, 2)
        if Ctoneladas1 > promT or Ctoneladas2 > promT or Ctoneladas3 > promT:
            superan += 1

        print("\nEl promedio de granos es de: ", promT, end=" T | ")
        print("'"+str(superan)+"'", "superan el promedio.")

        print(separador)
        print(img_opciones)
        opc = int(input("\nIngresar otra opcion: "))

else:
    print("\nFin del programa 🤠...")


















