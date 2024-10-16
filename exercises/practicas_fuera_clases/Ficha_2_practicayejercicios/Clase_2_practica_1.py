__author__ = "Wendler Juan Jose"

# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
# (cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen
# un descuento del 35%. Mostrar el precio actual, el monto del descuento y el monto final a pagar.

print("Descuento en medicinas: ")

precio_medicamento = float(input("\nPrecio del medicamento: "))
descuento = (35 * precio_medicamento) / 100
monto_final = precio_medicamento - descuento
print("Precio del medicamento: ", str(precio_medicamento) + "$", "\nCon 35% off: ", "-" + str(descuento) + "$"
      ,"\nA pagar: ", str(monto_final) + "$")


