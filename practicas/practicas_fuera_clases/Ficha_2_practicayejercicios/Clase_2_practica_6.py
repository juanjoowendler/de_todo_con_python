__author__ = "Wendler Juan Jose"

print("Votación en el Congreso: ")

# En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita
# ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.


cant_vfavor = int(input("Ingresar la cantidad de votos a favor: "))
cant_vcontra = int(input("Ingresar la cantidad de votos en contra: "))
total = cant_vfavor + cant_vcontra

porc_vfavor = (cant_vfavor * 100) / total
porc_vcontra = (cant_vcontra * 100) / total

print("\nVotos en contra de un: ", str(round(porc_vcontra, 2)) + " %", "\nVotos a favor de un: ",
      str(round(porc_vfavor, 2)) + " %")
