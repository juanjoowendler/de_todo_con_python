__author__ = "Wendler Juan Jose"

# Desarrollar un programa completo en Python, que a través de un menú de opciones, ejecute los siguientes puntos
# (sin usar las funciones min() y max()):

# 1) Ingresar las notas de los alumnos de un curso (finaliza cuando se ingresa nota -1).
# Determinar la cantidad de alumnos aprobados (nota de 4 o más) y la nota promedio entre todos los alumnos.

# 2) Ingresar el nombre y la cantidad de lluvia caída de 3 ciudades.
# Determinar la ciudad con menor y con mayor cantidad de lluvias, y la diferencia entre ambas.

# 3) Ingresar las temperaturas tomadas durante un mes en distintos lugares del país (son 30 temperaturas).
# Indicar la cantidad de temperaturas bajo 0. Determinar el porcentaje que las temperaturas entre 10 y 20 grados
# (ambos incluidos) representan sobre el total. Determinar la diferencia entre la menor y la mayor temperatura.

# 4) Ingresar una cadena de caracteres. Determinar cuántos caracteres fueron dígitos.

# 5) Terminar el Programa.

print("*" * 35)
print("\t\tMenu de opciones: ")
print("*" * 35)

img_opc = "\n++++++++++++++++++++++++++++++\n1.---------Nota de alumnos\n2.---------Registro de lluvias\n3.---------" \
          "Registro de temperaturas\n4.---------Texto a procesar\n5.---------Salir\n++++++++++++++++++++++++++++++"

print(img_opc)
opc = int(input("\nElegir una opcion: "))

while opc != 5 and 0 < opc < 6:
    if opc == 1:
        nota = 1
        aprob = acuNotas = cantAlumnos =  0
        while nota >= 0:
            nomAlumno = input("Nombre: ")
            nota = int(input("Nota: "))
            cantAlumnos += 1
            if nota >= 4:
                aprob += 1
                acuNotas += nota
            else:
                acuNotas += nota
            if nota < 0:
                break
        promNotas = acuNotas / (cantAlumnos)
        promNotas = round(promNotas, 2)
        print("La cantidad de alumnos aprobados es", aprob, end=", ")
        print("la nota promedio entre todos los alumnos es", str(promNotas) + ".")

        print(img_opc)
        opc = int(input("Elegir otra opcion: "))

    elif opc == 2:
        ciudad1N = input("Nombre de la primera ciudad: ")
        cantLl1 = float(input("Cantidad de lluvia caida en la primer ciudad: "))
        ciudad2N = input("Nombre de la segunda ciudad: ")
        cantLl2 = float(input("Cantidad de lluvia caida en la segunda ciudad: "))
        ciudad3N = input("Nombre de la tercer ciudad: ")
        cantLl3 = float(input("Cantidad de lluvia caida en la tercer ciudad: "))

        if cantLl1 > cantLl2 and cantLl1 > cantLl3:
            may = cantLl1, ciudad1N
            if cantLl2 > cantLl3:
                men = cantLl3, ciudad3N
            else:
                men = cantLl2, ciudad2N
        elif cantLl2 > cantLl1 and cantLl2 > cantLl3:
            may = cantLl2, ciudad2N
            if cantLl1 > cantLl3:
                men = cantLl3, ciudad3N
            else:
                men = cantLl1, ciudad1N
        elif cantLl3 > cantLl1 and cantLl3 > cantLl2:
            may = cantLl3, ciudad3N
            if cantLl1 > cantLl2:
                men = cantLl2, ciudad2N
            else:
                men = cantLl1, ciudad1N

        difmenmayLl = may[0] - men[0]

        print("\nEn la ciudad"+"'"+str(ciudad1N)+"'", "cayeron", cantLl1, "Lt/s de lluvia.")
        print("En la ciudad"+"'"+str(ciudad2N)+"'", "cayeron", cantLl2, "Lt/s de lluvia.")
        print("En la ciudad"+"'"+str(ciudad3N)+"'", "cayeron", cantLl3, "Lt/s de lluvia.")
        print("La ciudad con menor cantidad de lluvia es", men[1], "con", men[0], "Lt/s")
        print("La ciudad con mayor cantidad de lluvia es", may[1], "con", may[0], "Lt/s")
        print("La diferencia entre la 'menor' y 'mayor' cantidad de lluvia es de: ", difmenmayLl, "Lt/s")


        print(img_opc)
        opc = int(input("Elegir otra opcion: "))

    elif opc == 3:
        tem = float(input("Ingresar primer temperatura: "))
        menT = tem
        mayT = tem
        bajoCero = comprendidas = acuTem = 0
        for i in range(30):
            tem = float(input("Ingresar otra temperatura: "))
            acuTem += 1
            if tem < 0:
                bajoCero += 1
            if 10 <= tem <= 20:
                comprendidas += tem
            if tem > may:
                may = tem
            elif tem < men:
                men = tem

            difmenmayT = may - men
            porcComprendidas = (comprendidas * 100) / acuTem
            print("La diferencia entre la mayor y menor t° es de", str(difmenmayT) + "°")

        print(img_opc)
        opc = int(input("Elegir otra opcion: "))

    elif opc == 4:
        texto = input("Ingresar un texto: ")
        acuDig = 0
        for caracter in texto:
            if caracter in "123456789":
                acuDig += 1
        print(acuDig, "fueron digitos.")

        print(img_opc)
        opc = int(input("Elegir otra opcion: "))

else:
    print("\nFin del programa 🤠...")




















