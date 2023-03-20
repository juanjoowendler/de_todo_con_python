__author__ = "Wendler Juan Jose"

# El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de un
# programa que facilite la gestión de las tareas realizadas en el día.
#
# El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos:
# número de identificación de la PC, tiempo de reparación (expresado en minutos) y la causa de mantenimiento
# (1- Problema de Hardware 2-Problema de Software)
#
#               Los requerimientos funcionales son:
#
# a)  ¿Cuál es el tiempo total de las tareas de mantenimiento?
#
# b)  ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?
#
# c)  Tiempo promedio de tareas de mantenimiento.
#
# d)  Informar con un mensaje si todas las PC (Número de identificación) que se les ha realizado
# mantenimiento tuvieron problemas de Hardware.

print("\n\t\t\tMantenimiento Informático: ")
print("*" * 60)


print("\n\tIngresar los datos de la PC (1): ")
num_i1 = int(input("-Ingresar el numero de identificacion: "))
rep_t1 = int(input("-Ingresar el tiempo de reparacion (en minutos): "))
man_causa1 = int(input("\n1. Problema de Hardware \t\t2. Problema de software \t-> "))

print("\n\tIngresar los datos de la PC (2): ")
num_i2 = int(input("-Ingresar el numero de identificacion: "))
rep_t2 = int(input("-Ingresar el tiempo de reparacion (en minutos): "))
man_causa2 = int(input("\n1. Problema de Hardware \t\t2. Problema de software \t-> "))

print("\n\tIngresar los datos de la PC (3): ")
num_i3 = int(input("-Ingresar el numero de identificacion: "))
rep_t3 = int(input("-Ingresar el tiempo de reparacion (en minutos): "))
man_causa3 = int(input("\n1. Problema de Hardware \t\t2. Problema de software \t-> "))

tt_man_causa = rep_t1 + rep_t2 + rep_t3

if rep_t1 > rep_t2 and rep_t1 > rep_t3:
    may = rep_t1
elif rep_t2 > rep_t3:
    may = rep_t2
else:
    may = rep_t3

if may == rep_t1:
    mensaje = "El equipo: ", num_i1, "llevo mas tiempo para la reparacion."
elif may == rep_t2:
    mensaje = "El equipo: ", num_i2, "llevo mas tiempo para la reparacion."
else:
    mensaje = "El equipo: ", num_i3, "llevo mas tiempo para la reparacion."

t_prom = (rep_t1 + rep_t2 + rep_t3) / 3

if man_causa1 == 1 and man_causa2 == 1 and man_causa3 == 1:
    mensaje1 = "Todas las PC's tuvieron problemas de Hardware."
else:
    mensaje1 = "Las PC's tuvieron problemas diversos."


print("\n\t-El tiempo total de las tareas de mantenimiento fue de: ", str(tt_man_causa) + " minutos.")

if rep_t1 == rep_t2 == rep_t3:
    print("\t-Todas las reparaciones llevaron el mismo tiempo.")
else:
    print("\t-La PC que llevo un mayor tiempo en las tareas de mantenimiento fue: ", str(mensaje) + ".")

print("\t-El tiempo promedio en las tareas de mantenimiento fue de: ", round(t_prom, 0), " minutos.")
print("\n\t->", str(mensaje1))



