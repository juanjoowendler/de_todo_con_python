__author__ = "Wendler Juan Jose"

print("Numeros pares e impares")

print("*"*50)

acu = cont_par = cont_impar = 0
anterior = 2
hay_cero = False
estan_alternados = True

num = int(input("Ingresar un n° (finaliza con un n° negativo) "))

while num >= 0:
    if num >= 50 and num <= 100:
        acu += num
    paridad = num % 2
    if paridad == 0:
        cont_par += 1
    else:
        cont_impar += 1
    if num == 0:
        hay_cero = True
    if anterior == paridad:
        estan_alternados = False
    anterior = paridad
    num = int(input("Ingresar otro n° (finaliza con un n° negativo)"))

print("Sumatoria de n° enteros entre 50 y 100: ", acu)
print("Cantidad de valores pares: ", cont_par)
print("Cantidad de valroes impares: ", cont_impar)

if hay_cero:
    print("Hubo al menos un '0' ")
if estan_alternados:
    print("Los valores alternados")

# asi se escoje una parte nueva

for i in range(n):
    print("caca")

