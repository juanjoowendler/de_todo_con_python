__author__ = "Wendler Juan Jose"

print("\n\t\tConversor de h,min,s a seg: ")
h = int(input("\n-Ingresar horas: "))
min = int(input("-Ingresar minutos: "))
s = int(input("-Ingresar segundos: "))

h_a_seg = h * 3600
min_a_seg = min * 60
seg_t = h_a_seg + min_a_seg + s
print("\n♦ Tiempo convertido: ", seg_t)
