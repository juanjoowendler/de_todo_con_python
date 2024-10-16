__author__ = "Wendler Juan Jose"

#  Conociendo el precio de lista de un artículo, determinar:
#
#     Precio de venta al contado (10% de descuento)
#     Precio de venta con tarjeta (5% de recargo)

precio_original = float(input("Ingresar precio de venta: "))

des_contado = (precio_original * 10)/100
precio_finalcontado = precio_original - des_contado

des_tarjeta = (precio_original * 5)/100
precio_finaltarjeta = precio_original + des_tarjeta

print("\nPrecio a abonar: ", str(precio_original) + "$", "\nMonto por contado: ", str(precio_finalcontado) + "$",
      "\nMonto por tarjeta: ", str(precio_finaltarjeta) + "$", "\t\t-Se desconto por contado: ", "-" + str(des_contado)
      + "$" + ", -Se desconto por tarjeta: ", "-" + str(des_tarjeta) + "$")


