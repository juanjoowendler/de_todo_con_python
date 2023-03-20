__author__ = "Wendler Juan jose"

# Carga de datos, enfermos por ciudad/pais...

print("Ejemplo 3, Calculo del porcentaje de enfermos en la ciudad: ")
ec = int(input("\nIngresar la cantidad de enfermos en la ciudad: "))
ep = int (input("Ingresar la cantidad de enfermos en el pais: "))

# Procesos...

te = (ep * 100) / ec

# Visualizacion de resultados...

print("\nEl porcentaje de enfermos en el pais es de un: ", te, "% 'actualmente' ")
