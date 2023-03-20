__author__ = "Wendler Juan Jose"

print("Precio del boleto")

# Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
# Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
# más un valor extra calculado en base a la cantidad de kilómetros a recorrer:
# Por cada kilómetro a recorrer se cobra $0.30 de adicional.

monto_base = float(input("Ingresar monto base: "))
cant_km = float(input("Cantidad de km a recorrer: "))
adicional = cant_km * 0.30
print("El pasajero debe de abonar: ", monto_base + adicional, "$")


