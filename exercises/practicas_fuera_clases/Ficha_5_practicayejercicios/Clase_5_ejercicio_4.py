__author__ = "Wendler Juan Jose"

# Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día.
# Se solicita el desarrollo de un programa que facilite información estadísticas de ellas.
#
# El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).
#
#           Los requerimientos funcionales son:
#
# a) Promedio de temperatura diaria.
#
# b) Temperatura máxima.
#
# c) Temperatura mínima.
#
# d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio.

print("\t\t\tObservatorio meteorológico: ")
print("-" * 60)

tem_1 = int(input("-Ingresar la primer temperatura: "))
tem_2 = int(input("-Ingresar la segunda temperatura: "))
tem_3 = int(input("-Ingresar la tercer temperatura: "))
tem_4 = int(input("-Ingresar la cuarta temperatura: "))

tem_prom = (tem_1 + tem_2 + tem_4) / 4

if tem_1 > tem_2 and tem_1 > tem_3 and tem_1 > tem_4:
    may = tem_1
elif tem_2 > tem_3 and tem_2 > tem_4:
    may = tem_2
elif tem_3 > tem_4:
    may = tem_3
else:
    may = tem_4

if tem_1 < tem_2 and tem_1 < tem_3 and tem_1 < tem_4:
    men = tem_1
elif tem_2 < tem_3 and tem_2 < tem_4:
    men = tem_2
elif tem_3 < tem_4:
    men = tem_3
else:
    men = tem_4


if tem_1 or tem_2 or tem_3 or tem_4 > tem_prom:
    mensaje = "La temperatura: ", str(may) + "°", "supero al promedio."
else:
    mensaje = "Ninguna de las temperaturas supero la temperatura promedio."

print("La temperatura maxima fue: ", str(may) + "°.")
print("La temperatura minima fue: ", str(men) + "°.")
print(mensaje)
