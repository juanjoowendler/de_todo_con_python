__author__ = "Wendler Juan Jose"

print("Galería de arte: ")

# Una galería de arte desea preparar un catálogo de sus cuadros más famosos.
#
# Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá:
#
# Verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado.
# Se inició en el año 1901 y terminó en el año 2000).
# Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
# Informar la diferencia en años entre la obra más nueva y la más antigua.


c1 = int(input("Año en el que fue creado: "))
c2 = int(input("Año en el que fue creado: "))
c3 = int(input("Año en el que fue creado: "))

if c1 <= 1901 and c2 <= 1901 and c3 <= 1901:
    print("Los cuadros son anteriores al siglo XX")
else:
    print("No todos los cuadros son anteriores al siglo XX")

anio = int(input("Ingresar el año de una obra: "))

if anio == c1 or anio == c2 or anio == c3:
    print("Alguna de las obras fue creada en ese año")
else:
    print("Ninguna de las obras fue creada en ese año")

c_n = max(c1, c2, c3)
c_v = min(c1, c2, c3)

diferencia = c_n - c_v

print("La diferencia de años entre la obra mas vieja y la mas nueva es de: ", str(diferencia) + ".")
