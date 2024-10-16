import modulo_principal
import os.path
import io
import pickle


def legajo(m, fd):
    legajo = ""
    while legajo == "" or buscar_legajo(m, legajo, fd):
        legajo = int(input(".Legajo: "))
        if (legajo > 99999 or legajo < 11111) or buscar_legajo(m, legajo, fd):
            print("repetido o incorrecto")
    
    return legajo


def nombre():
    nombre = ""
    while len(nombre) == 0:
        nombre = input(".Nombre: ")
        _nombre = nombre.ljust(30)
    
    return _nombre


def promedio():
    promedio = 0
    while promedio > 10 or promedio < 1:
        promedio = float(input(".Promedio: "))
        
    return promedio


def buscar_legajo(m, legajo, fd):
    fp_inicial = m.tell()
    
    m.seek(0, io.SEEK_SET)
    
    _presente = False
    t = os.path.getsize(fd)
    while m.tell() < t: 
        estudiante = pickle.load(m)
        if estudiante.legajo == legajo:
            _presente = True
            break
    
    m.seek(fp_inicial, io.SEEK_SET)
    
    return _presente
    
    
        