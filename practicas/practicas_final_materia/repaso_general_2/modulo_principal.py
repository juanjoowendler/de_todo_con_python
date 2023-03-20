import modulo_funciones


def main():
    menu = "\t\t\n==Gestion ABM==\n\
    1). Alta de registro en archivo.\n\
    2). Baja logica.\n\
    3). Modificar datos.\n\
    4). Mostrar archivo.\n\
    5). Mostrar datos comprendidos.\n\
    6). Depurar.\n\
    0). Salir del programa."
    
    fail = format("\n[!] {}.")
    fd = "estudiantes.dat"
    
    opc = -1
    while opc != 0:
        print(menu)
        opc = int(input(".Digite su opcion: "))
        
        if opc == 1:
            modulo_funciones.alta(fd)
        
        elif opc == 2:
            modulo_funciones.modificacion(fd)
        
        elif opc == 3:
            pass
        
        elif opc == 4:
            pass
        
        elif opc == 5:
            pass
        
        elif opc == 6:
            pass
        
        elif opc == 0:
            print("\nPrograma terminado.")
            
        else:
            print(fail.format("opcion incorrecta"))

if __name__ == "__main__":
    main()