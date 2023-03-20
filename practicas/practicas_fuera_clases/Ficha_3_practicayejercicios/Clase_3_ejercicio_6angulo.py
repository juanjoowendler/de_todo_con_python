__author__ = "Wendler Juan Jose"

#   A partir de un angulo expresado en sexagesimal
#   convertir al mismo en solo grados, solo minutos
#   y solo segundos

# RESULTADO:
# Angulo expresado en grados, minutos y segundos

# DATOS:
# Angulo expresado en sexagesimal

# NOMBRES:
# grados = gr; minutos = min; segundos = seg
# resultados grados = rgr; resultados minutos = rmin;
# resultado segundos = rseg

print("\t\tConversor de angulo a grados, min y segundos: ")

gr = int(input("\n-Grados: "))
min = int(input("-Minutos: "))
seg = int(input("-Segundos: "))


rgr = gr + min /60 + seg/3600
rmin = gr * 60 + min + seg/60
rseg = gr * 3600 + min * 60 + seg


redgr = round(rgr, 0)
redmin = round(rmin, 0)

print("\n","El resultado es expresado en : \n", "\n-Grados: ",redgr, "°" "\n-Minutos: ", redmin,"'" "\n-Segundos: ", rseg,"''" )




