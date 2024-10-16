__author__ = "Wendler Juan Jose"

# Para calcular el premio de un vendedor, se ingresan 3 montos correspondientes a sus ventas mensuales
# del último trimestre.
#
# El premio es equivalente al 50% del menor monto vendido. Si además todos los montos superan los $1000,
# se agrega un 10% adicional al premio calculado.

print("\t\t\t\tPremio por Ventas: ")
print("*" * 50)

monto1 = float(input("\n-Ingresar el primer monto: "))
monto2 = float(input("-Ingresar el primer monto: "))
monto3 = float(input("-Ingresar el primer monto: "))

superada = False

if monto1 < monto2 and monto1 < monto3:
    men = monto1
elif monto2 < monto3:
    men = monto2
else:
    men = monto3

premio = men * 0.5
print("\nEl menor de los montos fue: ", str(men) + " $, el premio a recibir sera de: ", str(premio) + " $.")

if monto1 and monto2 and monto3 >= 1000:
    superada = True

if superada:
    premio1 = premio + premio * 0.10
    print("\nComo todos los montos superaron los 1000 $, el premio adicional sera de: ", str(premio1) + " $.")
    print("premio final: ", premio1 + premio)

