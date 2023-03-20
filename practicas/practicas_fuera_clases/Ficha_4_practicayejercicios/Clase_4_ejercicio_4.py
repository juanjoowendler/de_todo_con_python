__author__ = "Wendler Juan Jose"

print("Temperatura diaria: ")

# Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a
# diferentes momentos de un día y determinar:
#
#     Cual es el promedio de las temperaturas.
#     Si existe alguna temperatura que sea mayor al promedio.


t1 = float(input("Primera temperatura registrada: "))
t2 = float(input("Segunda temperatura registrada: "))
t3 = float(input("Tercera temperatura registrada: "))

prom = (t1 + t2 + t3)/3
print("El promedio de las temperaturas es de: ", round(prom, 2))
if t1 > prom:
    print(str(t1) + ":t1 es la mayor del promedio.")
elif t2 > prom:
    print(str(t2) + ":t2 es la mayor del promedio.")
elif t3 > prom:
    print(str(t3) + ":t3 es la mayor del promedio.")
elif t1 == t2 and t1 == t3 or t2 == t1 and t2 == t3 or t3 == t1 and t3 == t2:
    print(str(t1) + "|" + str(t2) + "|" + str(t3), ":Todas las temperaturas registradas fueron iguales.")



