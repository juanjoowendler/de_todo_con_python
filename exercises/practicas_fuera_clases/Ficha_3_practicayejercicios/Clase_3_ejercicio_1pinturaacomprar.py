__author__ = "Wendler Juan jose"

# PROBLEMA:

#       Dada la altura y el ancho de una pared
#       determinar la cantidad de pintura a comprar
#       teniendo en cuenta que el latex para cada litro   rinde 10m^2

# INFORMACION:

#       Resultado/s: cantidad de pintura a comprar por litro
#       Datos: altura y ancho; rendimiento de la pintura
#       Tipo de dato: sup: float; cant_pintura:float
#       Proceso: sup_ altura * ancho (m^2)

# REGLA DE 3:

#       10 m^2_________1lt
#       sup m^2______sup*1lt/10lt's = cant_pintura

# PSEUDOCODIGO:

#       1. Cargar altura (altura de la pared en m)
#       2. Cargar ancho  (ancho de la pared en m)
#       3. Sea sup = altura * ancho
#       4. Sea cant_pintura = sup / 10
#       5. Mostrar cant_pintura

#   Cargamos datos Titulo;1;2;
print("Calcular cantidad de pintura en base a la superficie: ")
altura = float(input("\nIngresar altura de la pared: "))
ancho = float(input("Ingresar ancho de la pared: "))

#   Proceso
sup = altura * ancho
cant_pintura = sup / 10

#   Mostrar
print("\nLa cantidad de pintura a comprar es de", cant_pintura, "lt's")








