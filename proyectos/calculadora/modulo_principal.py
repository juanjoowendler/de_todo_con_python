from tkinter import *

# // control de los botones
i = 0


def boton_click(valor):
    global i
    texto_entrada.insert(i, valor)
    i += 1


def borrar_click():
    texto_entrada.delete(0, END)
    i = 0


def evaluar():
    operacion = texto_entrada.get()
    resultado = eval(operacion)
    texto_entrada.delete(0, END)
    texto_entrada.insert(0, resultado)
    i = 0


ventana = Tk()
ventana.title("Calculadora")

# Entrada de texto
texto_entrada = Entry(ventana, font="Arial 12")
texto_entrada.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

# Botones

boton1 = Button(ventana, text="1", width=5, height=2, command=lambda: boton_click(1))
boton2 = Button(ventana, text="2", width=5, height=2, command=lambda: boton_click(2))
boton3 = Button(ventana, text="3", width=5, height=2, command=lambda: boton_click(3))
boton4 = Button(ventana, text="4", width=5, height=2, command=lambda: boton_click(4))
boton5 = Button(ventana, text="5", width=5, height=2, command=lambda: boton_click(5))
boton6 = Button(ventana, text="6", width=5, height=2, command=lambda: boton_click(6))
boton7 = Button(ventana, text="7", width=5, height=2, command=lambda: boton_click(7))
boton8 = Button(ventana, text="8", width=5, height=2, command=lambda: boton_click(8))
boton9 = Button(ventana, text="9", width=5, height=2, command=lambda: boton_click(9))
boton0 = Button(ventana, text="0", width=5, height=2, command=lambda: boton_click(0))

boton_borrar = Button(ventana, text="AC", width=5, height=2, command=lambda: borrar_click())

boton_parentesis1 = Button(ventana, text="(", width=5, height=2, command=lambda: boton_click("("))
boton_parentesis2 = Button(ventana, text=")", width=5, height=2, command=lambda: boton_click(")"))
boton_punto = Button(ventana, text=".", width=5, height=2, command=lambda: boton_click("."))
boton_division = Button(ventana, text="/", width=5, height=2, command=lambda: boton_click("/"))
boton_multiplicacion = Button(ventana, text="x", width=5, height=2, command=lambda: boton_click("x"))
boton_suma = Button(ventana, text="+", width=5, height=2, command=lambda: boton_click("+"))
boton_resta = Button(ventana, text="-", width=5, height=2, command=lambda: boton_click("-"))

boton_igual = Button(ventana, text="=", width=14, height=2, command=lambda: evaluar())

# Agregar en pantalla

boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_division.grid(row=1, column=3, padx=5, pady=5)
boton_multiplicacion.grid(row=2, column=3, padx=5, pady=5)
boton_punto.grid(row=2, column=2, padx=5, pady=5)
boton_suma.grid(row=2, column=1, padx=5, pady=5)
boton_resta.grid(row=2, column=0, padx=5, pady=5)
boton_igual.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# // botones de numeros

boton1.grid(row=3, column=0, padx=5, pady=5)
boton2.grid(row=3, column=1, padx=5, pady=5)
boton3.grid(row=3, column=2, padx=5, pady=5)
boton4.grid(row=3, column=3, padx=5, pady=5)
boton5.grid(row=4, column=0, padx=5, pady=5)
boton6.grid(row=4, column=1, padx=5, pady=5)
boton7.grid(row=4, column=2, padx=5, pady=5)
boton8.grid(row=4, column=3, padx=5, pady=5)
boton9.grid(row=5, column=0, padx=5, pady=5)
boton0.grid(row=5, column=1, padx=5, pady=5)

ventana.mainloop()

