__author__ = "Wendler Juan Jose"

# Ingresar por teclado las edades de 3 participantes de un concurso.
# Informar si todos cumplen con la edad mínima establecida para el mismo,
# también ingresada por teclado.


print("Edad mínima: ")

e_min = int(input("Ingresar la edad minima para el concurso: "))

p_1 = (input("Nombre del primer participante: "))
pe_1 = int(input("Edad: "))
p_2 = (input("Nombre del segundo participante: "))
pe_2 = int(input("Edad: "))
p_3 = (input("Nombre del tercer participante: "))
pe_3 = int(input("Edad: "))

if pe_1 >= e_min and pe_2 >= e_min and pe_3 >= e_min:
    print("Todos pueden participar.")
else:
    print("Al menos uno de los participantes no cumple con la edad minima.")
