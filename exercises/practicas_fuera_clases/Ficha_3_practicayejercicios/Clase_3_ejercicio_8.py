__author__ = "Wendler Juan Jose"

print("Costos del Proyecto: ")

# Una pequeña empresa de informática tiene que desarrollar un sistema de información y para ello tiene
# un presupuesto de x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar
# al menos 17% por el proyecto, determine cuál es el valor máximo que pueden alcanzar los costos del proyecto.

presupuesto = float(input("\nIngresar el presupuesto inicial: "))
asegurado = (17 * presupuesto)/100
valor_maximo = presupuesto - asegurado
print("El valor maximo que pueden alcanzar los costos del proyecto es de: ", str(valor_maximo) + "$" " y al menos, "
      "ganando el 17% tendrian un total de: ", str(asegurado) + "$.")


