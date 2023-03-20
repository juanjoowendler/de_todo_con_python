__author__ = "Wendler Juan Jose"

# Cargar por teclado3 n° enteros que se supone representan las edades de 3 personas.
# Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en la
# patalla con un mensaje, si todos los valores resultan + o 0, informe que todos los datos
# son correctos

# PSEUDOCOGIGO:
# 1. Cargar n1, n2 y n3
# 2. Si n1 < 0 o n2 < 0 o n3 < 0
# 2.1 mensaje = "Alguna es incorrecta: valor negativo."
# 3. sino
# 3.1 mensaje = "Los datos ingresados son correctos."

n1 = int(input("Ingresar primer edad: "))
n2 = int(input("Ingresar segunda edad: "))
n3 = int(input("Ingresar tercera edad: "))

if n1 < 0 or n2 < 0 or n3 < 0:
    mensaje = "Alguno es incorrecta: valor negativo."
else:
    mensaje = "Los datos ingresados son correctos."

print("Resultado del control: ", mensaje)

