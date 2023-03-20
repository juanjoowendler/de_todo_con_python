import modulo_validaciones
import modulo_registro
import pickle


def alta(fd):
    m = open(fd, "a+b")
    
    print("\n-Alta de estudiante-")
    legajo = modulo_validaciones.legajo(m, fd)
    nombre = modulo_validaciones.nombre()
    promedio = modulo_validaciones.promedio()
    
    estudiante = modulo_registro.Estudiante(legajo, nombre, promedio)
    pickle.dump(estudiante, m)
    m.flush()
    m.close()

    input("Alta completa <ENTER> terminar.")


def modificacion(fd):
    m = open(fd, "a+b")
    
    legajo = modulo_validaciones.legajo(m, fd)
    # terminar