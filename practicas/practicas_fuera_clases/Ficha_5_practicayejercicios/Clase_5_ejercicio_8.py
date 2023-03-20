__author__ = "Wendler Juan Jose"

# Se vota una ley en el Senado, y se ingresan votos a favor, en contra y abstenciones de los senadores presentes.
#
# Informar cuál fue el resultado de la votación. Si la ley fue aprobada, indicar si fue por mayoría absoluta
# (más del 50% de los votos) o por mayoría simple.
#
# Por último, considerando que la Cámara está formada por 72 senadores,
# determinar cuantos se encontraban ausentes.

print('VOTACION EN EL SENADO')

# Ingresar votos
favor = int(input('Ingrese votos a favor: '))
contra = int(input('Ingrese votos en contra: '))
abstenciones = int(input('Ingrese abstenciones: '))

# Calcultar total
total = favor + contra + abstenciones

# Definir resultado
if favor > contra and favor > abstenciones:
    resultado = 'La ley fue aprobada'
    porcentaje = favor * 100 / total
    if porcentaje > 50:
        resultado += ' por mayoria absoluta'
    else:
        resultado += ' por mayoria simple'
elif contra > abstenciones:
    resultado = 'La ley fue rechazada'
else:
    resultado = 'La ley deberá volver a tratarse'

# Calcular ausentes
ausentes = 72 - total

print('-' * 60)
print(resultado)
if ausentes >= 0:
    print('Hubo', ausentes, 'senadores ausentes')
else:
    print('HUBO FRAUDE!')
