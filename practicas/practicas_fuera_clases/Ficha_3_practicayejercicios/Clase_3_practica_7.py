__author__ = "Wendler Juan Jose"

print("Calculo Distancia de Viaje: ")

# Un persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir los puntos mas extremos
# (Ushuahia y La Quiaca) en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.
# Nuestro aventurero efectivamente inició la travesía pero se accidentó y sólo recorrió x metros según su GPS.
# Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro aventurero y qué
# porcentaje represento lo recorrido del total de kms a recorrer de Ushuahia a La Quiaca
# (para el porcentaje usted deberá realizar los calculos en metros).

tkm = 3641.3
x = float(input("\nCantidad de km recorridos: "))
kmaM = x * 1000

porc_rec = (x * 100)/3641.3

print("Porcentaje recorrido: ", str(round(porc_rec, 2)) + " %")






