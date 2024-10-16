__author__ = "Wendler Juan Jose"

print("Conversión de medidas: ")

# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
#
#             yardas
#             pulgadas
#             centímetros
#             metros
#
# Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros

pies = float(input("Ingresar medida en pies: "))


yardas = pies / 3
pulgadas = pies * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

# Presentacion de resultados
print('En', pies, 'pies hay', yardas, 'yardas')
print('En', pies, 'pies hay', pulgadas, 'pulgadas')
print('En', pies, 'pies hay', centimetros, 'centimetros')
print('En', pies, 'pies hay', metros, 'metros')
