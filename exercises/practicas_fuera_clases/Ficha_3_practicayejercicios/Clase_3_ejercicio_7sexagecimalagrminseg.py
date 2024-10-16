__author__= "Wendler Juan Jose"

#    El inverso del ejercicio 6

# RESULTADO:
# Angulo expresado en grados, minutos y segundos

# DATOS:
# Angulo expresado en segundos

# PROCESO:
# gr = seg//3600
# resto_gr = seg % 3600
# minutos = resto_gr
# segundos = resto_gr % 60
# resultado en grados, minutos y segundos

print("\t\tConversor de segundos a grados, minutos y segundos: ")

seg = int(input("\nIngresar segundos del angulo: "))

gr = seg // 3600
resto_gr = seg % 3600
min = resto_gr //60
seg = resto_gr % 60

print("\nAngulo sexagecimal:", gr, "°", min, "'", seg, "''")

