__author__ = "Wendler Juan Jose"

print("Duración de un vuelo: ")

# Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),
# determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto
# al hotel que ha reservado, ¿a qué hora llegara al mismo?


partida = (input("Ingresar el horario de partida en (hh:mm): "))
llegada = (input("Ingresar el horario de llegada en (hh:mm): "))

partidahs = str(partida)[0] + str(partida)[1]
partidamm = str(partida)[3] + str(partida)[4]

# hs a min
hs_a_mm = int(partidahs) * 60

# duracion del viaje toda en min
viaje_en_mm = str(partidamm) + str(hs_a_mm)

# ----------------------------------------


tiempo_final = (int(viaje_en_mm) + 45)/60

tiempo_final1 = str(tiempo_final)

print("Viaje en minutos: ", str(viaje_en_mm) + " minutos.")
print("El viajero llegara a las: ", tiempo_final1[0] + tiempo_final1[1] + tiempo_final1[2] + tiempo_final1[3])


# ----------------------------------------------------------------------------------------------------------------

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

TIEMPO_TAXI = 45

# Titulo y carga de datos
print('Determinacion de tiempo de llegada a aeropuerto')
print('Las horas se ingresaran en formato hh:mm (ejemplo: 14:45 o 05:30)')
partida = input('Ingrese la hora de partida en formato hh:mm :')
llegada = input('Ingrese la hora de llegada en formato hh:mm :')

# Procesos

# Sacamos la hora de partida y la convertimos a número entero...
hp = partida[0] + partida[1]
hora_partida = int(hp)

# Ahora los minutos de esa hora, en formato entero...
mp = partida[3] + partida[4]
minutos_partida = int(mp)

# Sacamos la hora llegada y hacemos lo mismo...
hl = llegada[0] + llegada[1]
hora_llegada = int(hl)

# Igual se procede con los minutos...
ml = llegada[3] + llegada[4]
minutos_llegada = int(ml)

# Transformamos hh de la hora de partida a minutos
# y la acumulamos a los mm de los minutos de partida
minutos_partida = minutos_partida + hora_partida * 60

# Transformamos la hh de la hora de llegada a minutos
# y la acumulamos a los mm de los minutos de llegada
minutos_llegada = minutos_llegada + hora_llegada * 60

# Duracion del viaje...
duracion_viaje_minutos = minutos_llegada - minutos_partida
hora_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) // 60
minutos_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) % 60

# Presentacion de resultados
print('La duracion del viaje es de:', duracion_viaje_minutos, 'minutos')
print('Llega a las', (str(hora_llegada_hotel) + ':' + str(minutos_llegada_hotel)))


