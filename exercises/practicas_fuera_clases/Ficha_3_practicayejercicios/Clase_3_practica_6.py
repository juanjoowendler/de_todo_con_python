__author__ = "Wendler Juan Jose"

print("Cálculo presupuestario: ")

# En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología.
# El presupuesto anual del hospital se reparte de la siguiente manera:

#                       Área              Presupuesto
#                      Urgencias              37%
#                      Pediatría              42%
#                      Traumatología          21%

# Cargar por teclado el monto del presupuesto total del hospital,
# y calcular y mostrar el monto que recibirá cada área.


#   Carga

p_total = float(input("\nPresupuesto total del hospital: "))

#   Procesos
urgencias = (37 * p_total)/100
pediatria = (42 * p_total)/100
traumatologia = (21 * p_total)/100

#   Mostramos


print("\nUrgencias recibira: ", str(urgencias) + "$", "Traumatologia recibira: ", str(traumatologia) + "$",
      "Pediatria recibira: ", str(pediatria) + "$.")


