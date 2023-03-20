__author__ = "Wendler Juan Jose"

#   Programa para cargar nombre de estudiante, profesor
#   y promedio general (decimales); y mostrar estos mismos
#   con el prefijo 'est.' para alumno y 'prof.' para maestro
#   el promedio del alumno debe ser mostrado redondeado entero.

# PSEUDOCODIGO
# 1. Cargar n_est  (nombre del estudiante)
# 2. Cargar n_prof (nombre del profesor)
# 3. Cargar p_est  (promedio del estudiante)
# 4. Sea prefinal_est = "est." + n_est
# 5. Sea prefinal_prof = "prof." + n_prof
# 6. Sea promfinal_est = round(p_est)
# 7. Mostrar prefinal_est
# 8. Mostrar promfinal_est
# 9. Mostrar prefinal_prof
print("\n")
print("\tRegistro  de las notas: ")

n_est = input("\nIngresar nombre del estudiante: ")
a_est = input("Ingresar apellido del estudiante: ")
n_prof = input("\nIngresar nombre del profesor: ")
a_prof = input("Ingresar apellido del profesor: ")

p_est = float(input("\nPromedio del estudiante: "))

prefinal_est = " est." + n_est + a_est
prefinal_prof = " prof." + n_prof + a_prof
promfinal_est = round(p_est)

print("\nNombre Completo:", prefinal_est, "\t- Profesor:", prefinal_prof)
print("Promedio general:", promfinal_est)






