__author__ = "Wendler Juan Jose"

# Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
#
# Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar
# cualquier otro valor para sexo.

#                                    El programa debe informar:

# a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
# b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
# c) Si hay algún varón que supere los 80 años de edad

print("\n\t\t\tCenso: ")
print("-" * 30)

hab = 0
mas = 0
fem = 0
cant_femscolar = 0
sup_masedad = False

sexo = input("Ingresar el sexo de la persona, (M/F): ")
while sexo == "M" or sexo == "m" or sexo == "F" or sexo == "f":
    hab += 1
    edad = int(input("Ingresar edad de la persona: "))
    if sexo == "m" or sexo == "M":
        mas += 1
        if edad > 80:
            sup_masedad = True

    else:
        if sexo == "f" or sexo == "F":
            fem += 1
            if 4 <= edad <= 18:
                cant_femscolar += 1
    sexo = input("Ingresar el sexo de la persona, (M/F): ")
else:
    print("\nfin del programa...")

if mas > fem:
    print("\nLa mayor cantidad de habitantes corresponde a hombres.")
elif fem > mas:
    print("La mayor cantidad de habitantes corresponde a mujeres.")
else:
    print("Hay igual cantidad de hombres y de mujeres.")
print("La cantidad de mujeres en edad escolar es de: ", cant_femscolar)
if sup_masedad:
    print("Hay al menos un hombre que supera los 80")
else:
    print("Ningun hombre supera los 80")
