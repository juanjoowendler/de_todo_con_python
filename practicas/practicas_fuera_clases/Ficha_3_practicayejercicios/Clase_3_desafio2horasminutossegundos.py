__author__ = "Wendler Juan Jose"

# PSEUDOCODIGO:
# 1. cant_s (Cargar la cantidad de segundos)
# 2. Sea s = cant_s % 60
# 2,1 Sea cos = cant_s/60
# 3. Sea min = s % cos
# 4. Sea h = s/cos

print("\n\t\tConversor de segundos a h,min y seg: ")
s = int(input("\nTiempo en segundos: "))
min = s//60
seg_resto = s % min
h = min//60
min_resto = min % 60

print("Datos convertidos: {}:{}:{}". format(h, min_resto,seg_resto))
