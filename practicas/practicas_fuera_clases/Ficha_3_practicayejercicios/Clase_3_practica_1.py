__author__ = "Wendler Juan Jose"

print("Fecha como cadena: ")

# Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato
# 'dd/mm/aaaa', y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada es '16/03/2016'
# el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.+


fecha = input("Ingresar fecha en formato (dd/mm/aaaa)- 'incluir los 0': ")

dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]
aaa = fecha[6] + fecha[7] + fecha[8] + fecha[9]

print("-dia: ", dia, "-mes: ", mes, "año: ", aaa)
