__author__ = "Wendler Juan Jose"

print("Cálculo de ángulos: ")

# Se sabe que la suma de dos ángulos desconocidos (alfa + beta) es igual a cierto valor x que se carga por teclado.
# Además se sabe que la diferencia entre esos mismos dos ángulos (alfa - beta) es igual a otro valor y que también
# se carga por teclado. Desarrolle un programa que dados los valores x e y, determine
# el valor de los dos ángulos alfa y beta. No es necesario convertir a grados,
# minutos y segundos el valor de cada ángulo: expréselos como números reales, tal cual hayan sido obtenidos.


x = float(input("La suma de los angulos desonocidos es: "))
y = float(input("La diferencia de los angulos desconocidos es: "))

# De donde:
# x = alfa + beta
# =>  alfa = x - beta

# Por lo tanto:
# y = alfa - beta
# => y = x - beta - beta
# => y = x - 2*beta
# => y + 2*beta = x
# => 2*beta = x - y
# => beta = (x-y)/2

# Entonces:
# Si y = alfa - beta
# => alfa = y + beta

beta = (x-y)/2
alfa = y + beta


print('Valor del angulo alfa:', str(alfa) + "°")
print('Valor del angulo beta:', str(beta) + "°")
