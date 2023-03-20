__author__ = "Wendler Juan Jose"

# Carga de los datos del empleado...
print("Ejemplo 2, Calculo del sueldo del empleado")
nom = input("Nombre del empleado: ")
horas = int(input("Ingresar la cantidad de horas que trabaja el empleado:"))
monto = float(input("Ingrese el monto a cobrar por hora del empleado: "))

# Procesos...
sueldo = horas * monto

# Visualizacion de resultados...
print("\nNombre del empleado: ", nom, "\nSueldo del empleado: ", sueldo, "Ars")


