__author__ = "Wendler Juan Jose"

print("Importe como cadena")

# Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado
# como número en coma flotante y muestre un mensaje con esa cantidad pero en dos formatos:
# en uno debe aparecer precedida por el signo '$' y en el otro debe aparecer precedida por la palabra "pesos".


importe = float(input("Ingresar importe en $ Ars: "))

print("El importe realizado fue de: ", str(importe) + " $.")
print("El importe realizado fue de: ", importe, "pesos.")
