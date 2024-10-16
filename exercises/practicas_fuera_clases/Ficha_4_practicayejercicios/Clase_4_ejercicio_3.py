__author__ = "Wendler Juan Jose"

print("Jornal de un Operario: ")

# Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal
# de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
# (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
#
# La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el
# turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora,
# si lo hace en el turno diurno cobra 35.50 pesos la hora.


nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
cod_turno = float(input("Ingrese el codigo de turno (1- Diurno y 2- Nocturno): "))
cant_hs = float(input("Ingresar la cantidad de hs trabajadas: "))
gan_tnoc = 40.60
gan_tdiu = 35.50

if cod_turno == 1:
    gan_trabajador = cant_hs * 35.50
    print("El trabajador: ",  str(nombre) + " " + str(apellido) + ", obtendra: ", str(gan_trabajador) + " $.")
elif cod_turno == 2:
    gan_trabajador = cant_hs * 40.60
    print("El trabajador: ",  str(nombre) + " " + str(apellido) + ", obtendra: ", str(gan_trabajador) + " $.")

