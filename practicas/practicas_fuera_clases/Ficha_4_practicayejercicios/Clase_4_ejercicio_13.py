__author__ = "Wendler Juan Jose"

# La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y,
# por tal motivo, el día de hoy ofrece premios a a sus clientes.

# Estos premios se calculan de la siguiente manera:

# 1) Cada vez que pasa un cliente, se sortea un número del 0 al 9. Si el número coincide con el
# último dígito de la patente del vehículo, se le cobra la tarifa promocional de $50, si no,
# se le cobra la tarifa estándar de $90
#
# 2) Independientemente de la tarifa que deba pagar, si el último dígito de la patente es 7,
# entonces recibe un descuento del 50%, en caso contrario un descuento del 10%.
#
# Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente
# (únicamente los dígitos), simule su paso por el peaje e indique el monto a abonar.

print("Tarifas de Peaje: ")

import random as rd

num_pat = int(input("Ingrese los numeros de su patente: "))
ultimo_num = num_pat % 10
num_sorteado = rd.randint(0, 9)

if ultimo_num == num_sorteado:
    print("Felicidades obtienes la tarifa promocional, deberas abonar 50$ Ars.")
else:
    print("No coinciden, la tarifa estandar a abonar es de 90 $ Ars.")

descuento_7 = 90 - (90 * 0.5)
descuento_general = 90 - (90 * 0.10)
if ultimo_num == 7:
    print(" Pero tu patente termina en '7', abonas un 50 % menos: ", str(descuento_7) + "$ Ars.")
else:
    print("Pero tienes un descuento del 10 %, abonas: ", str(descuento_general) + "$ Ars.")



