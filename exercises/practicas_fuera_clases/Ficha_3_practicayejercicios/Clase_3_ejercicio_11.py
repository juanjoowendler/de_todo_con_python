__author__ = "Wendler Juan Jose"

print("Calculo de Posta de Natacion: ")

# En la disciplina olímpica una de las pruebas mas esperadas en la natacion es la posta 4x100.
# En esta disciplina el equipo ganador registró los siguientes tiempos en cada estilo:
#
#     Espalda: 52 segundos 15 centésimas.
#     Pecho: 1 minuto 2 segundos 75 centésimas.
#     Mariposa: 59 segundos 80 centésimas.
#     Libre: 48 segundos 15 centésimas.
#
# Usted debe averiguar el tiempo total de la carrera del equipo ganador y
# representarlo en minutos, segundos y centésimas.
#
#
#           Para recordar:
#
#     1 minutos son 60 segundos.
#     1 segundo son 100 centesimas.

print('Calculo tiempo ganador de posta 4x100')
print('*' * 80)

# tomar cada estilo y pasarlo a centésimas para sumar
espalda = 52*100 + 15
pecho = 62*100 + 75
mariposa = 59*100 + 80
crol = 48*100 + 15

total = espalda + pecho + mariposa + crol

# convertir el total a minutos, segundos y centésimas para el tiempo total
# total de centésimas por minuto:
# 1 min -> 60 seg y 1 seg -> 10 cs => 1 min = 60 * 100 = 6000 centésimas.

minutos = total // 6000
resto = total % 6000

segundos = resto // 100
centesimas = resto % 100

print('Total:', minutos, 'minutos', segundos, 'segundos y', centesimas, 'centesimas')
