__author__ = "Wendler Juan Jose" # NO FUNCIONA !

#n = int(input("Ingresar la cantidad de n° a cargar: "))
#num = int(input("Ingrese el primero de los n°: "))
#may = num
#men = num

#for n in range(n-1):
   # num = int(input("Ingresar otro n°: "))
    #if num > may:
       # may = num
   # if num < men:
        #men = num

#print("El mayor es: ", may)
#print("El menor es: ", men)

#---------------------------------------------------------------------------------------------------------------------


# Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
# b) Determinar en qué mes recibió el sueldo más bajo del período.
# c) Informar el sueldo promedio del semestre.

print("\n\t\tSueldos y aguinaldo: ")
print("-" * 40)

semestre = ("Febrero", "Marzo", "Abril", "Mayo", "Junio")
sueldo = float(input("Ingresar el primer sueldo para Enero: "))

men = sueldo
may = sueldo
acu_sueldo = 0

for mes in semestre:
    int(input("Ingresar sueldo para " + str(mes) + ": "))
    if sueldo > may:
        may = sueldo
    if sueldo > may:
        may = sueldo
    if sueldo < men[0]:
        men = sueldo, mes

aguinaldo = may / 2
prom = acu_sueldo / len(semestre)-1
print("El aguinaldo es de: ", str(aguinaldo) + "$.")
print("El menor sueldo fue de $", men[0], "y lo obtuvo en el mes de", men[1])
print("El sueldo promedio del semestre es de: ", str(prom) + "$.")




