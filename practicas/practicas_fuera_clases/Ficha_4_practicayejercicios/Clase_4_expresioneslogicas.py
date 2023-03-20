__author__ = "Wendler Juan Jose"

# Considere estas variables con estos valores:

# a, b, c, d, e = 3, 5, 7, 2, 3

# Ejemplo: valor final asignado en r1: True
# r1 = a > 2 and c == 3*d or not e != 3

# Desarrollo paso a paso: reemplazo de variables por sus valores
# r1 = 3 > 5 and 7 == 3*2 or not 3 != 3

# Desarrollo paso a paso: primero los operadores aritmeticos
# r1 = 3 > 5 and 7 == 3*2 or not 3 != 3
# r1 = 3 > 5 and 7 == 6 or not 3 != 3

# Desarrollo paso a paso: segundo los operadores relacionales
# r1 = 3 > 5 and 7 == 6 or not 3 != 3
# r1 = False and False or not False

# Desarrollo paso a paso: Tercero los not, and y or en ese orden...
# r1 = False and False or not False
# r1 = False and False or True
# r1 = False or True
# r1 = True

#---------------------------------------------------------------------------------------

# Mismo ejemplo pero cambiando las presedencias con los ()

# Considere estas vatriables con estos valores:
# a, b, c, d, e = 3, 5, 7, 2, 3

# Ejemplo: valor final asignado en r1: False
# r1 = a > b and (c == 3*d or not e != a)

# Desarrollo paso a paso: reemplazo de variables por sus valores:
# r1 = 3 > 5 and (7 == 3 * 2 or not 3 != 3)

# Desarrollo paso a paso: primero los operadores aritmeticos:
# r1 = 3 > 5 and (7 == 3*2  or not 3 != 3)
# r1 = 3 > 5 and (7 == 6 or not 3 != 3)

# Desarrollo paso a paso: segundo los operadores relacionales:
# r1 = 3 > 5 and (7 == 6 or not 3 != 3)
# r1 = 3 > 5 and (False or not False)

# Desarrollo paso a paso: Tercerolos not, and y or en ese orden...
#... primero resolviendo los parentesis antes de aplicar and y or...
# r1 = False and (False or not False)
# r1 = False and (False or True)
# r1 = False and True
# r1 = False




