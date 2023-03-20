__author__ = "Wendler Juan Jose"

print("Cálculo de sueldo: ")

# Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual pertenece.
# Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual y
# un descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:
#
#        Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx
#
#        Área Funcional:  xxxxxxxxxxxx
#
#        Salario Actual: $ xxxx
#

# Constantes

nom = input("\nNombre del empleado: ")
ape = input("Apellido del empleado: ")
ar_f = input("Area funcional: ")
sal = int(input("Salario del empleado: "))

# Procesos

n_sal = (5.5 * sal)/100 + sal

# Mostramos

print("\n\t\tNombre del empleado: ", nom, "\t\tNuevo salario: ", n_sal, "\n\t\tArea funcional: ", ar_f,
      "\n\t\tSalario actual: ", sal)

