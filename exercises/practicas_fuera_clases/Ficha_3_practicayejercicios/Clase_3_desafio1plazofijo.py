__author__ = "Wendler Juan Jose"

#   Desarrollar un programa que cargue por teclado la cantidad de dinero
#   depositada en plazo fijo por un cliente de un banco y calcular el
#   saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el
#   interes pactado era de 2.3% y que el banco cobra una tasa fija
#   de gastos por servicios financieros igual $20 por cuenta

# PSEUDOCODIGO
# 1. Cargar nom_cl (nombre del cliente)
# 2. Cargar ap_cl (apellido del cliente)
# 3. Sea nom_fin = nom_cl + ap_cl (nombre completo)
# 4. Sea int_pact = (mont * 2.3%) / 100 - (interes pactado)
# 5. Sea gast_serv = int_pact - 20$
# 6. Mostrar nom_final, Cargar mont (monto a ingresar)
# 7. Mostrar int_pact (interes pactado)
# 8. Mostrar gast_serv (gasto por servicios)

print("\n\t\tCUENTA POR PLAZO FIJO: ")
nom_cl = input("\nNombre: ")
ap_cl = input("Apellido: ")
nom_fin = nom_cl + ap_cl
mont = float(input("Monto a cargar: "))
int_pact = (mont * 2.3)/100
gast_serv = int_pact - 20
gan = gast_serv + mont

print("\nUsuario: ", nom_fin, ",Interes: ", int_pact, "$", ",Gastos administrativos: 20 $",  "\n\n\t\t\t\t- Interes neto: ",gast_serv, "$")
print("\n\t\t-Las ganancias obtenidas son de: ", gan, "$")
