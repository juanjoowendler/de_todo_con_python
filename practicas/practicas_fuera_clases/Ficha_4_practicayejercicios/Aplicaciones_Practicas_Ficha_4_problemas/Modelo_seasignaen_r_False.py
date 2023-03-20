__author__ = "Wendler Juan Jose"

a, b, c, d, e = 10, 4, 5, 5, 3

# Asignacion en r del valor False...

r = a and b > d or c != e and not (d or b)



# Desarrollo paso a paso: reemplazo las variables por sus valores...

r = 10 and 4 > 5 or 5 != 3 and not (5 or 4)



# Desarrollo paso a paso: se aplican los operadores relacionales...

r = 10 and 4 > 5 or 5 != 3 and not (5 or 4)
r = 10 and False or True and not (5 or 4)



# Desarrollo paso a paso: se aplican los conectores logicos...
# Primero los que vengan entre ()...

r = 10 and False or True and not (5 or 4)
r = 10 and False or True and not True

# Desarrollo paso a paso: se aplican los conectores logicos(2)...
# Luego los not...

r = 10 and False or True and not True
r = 10 and False or True and False

# Desarrollo paso a paso: se aplican los conectores logicos(3)...

r = 10 and False or True and False
r = False or False

# Desarrollo paso a paso: se aplican los conectores logicos(4)...
# y finalmente los or...

r = False or False
r = False


