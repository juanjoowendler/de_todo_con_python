__author__ = "Wendler Juan Jose "

# Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una
# dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:

#Componer la dirección de correo de la siguiente manera:
#<primera letra del nombre><apellido>@<dominio>
#Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= frc.utn.edu.ar la dirección de mail sería:
#fsteffolani@frc.utn.edu.ar

# Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
# <nombre>.<apellido>@<dominio>
# Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
# soledad.steffolani@colegiorosarito.edu.ar


print("\n\t\tGenerador de correo electronico:")
print("\nIngresa tus datos: ")

nombre = input("\n-Ingresar nombre: ")
apellido = input("-Ingresar apellido: ")
dominio = input("-Ingresar dominio: ")

if nombre[0] != apellido[0]:
    correo = nombre[0] + apellido + "@" + dominio
    print("\nTe sugerimos usar el siguiente correo: ", correo)

if nombre[0] == apellido[0]:
    correo = nombre + "." + apellido + "@" + dominio
    print("\nTe sugerimos usar el siguiente correo: ", correo)
