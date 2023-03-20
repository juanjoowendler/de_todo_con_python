import time
green = '\033[32m'

barra, dentro = "", green+"▀"

print("\nBuscando...")
for i in range(6):
    barra += dentro
    print(barra, end="")
    time.sleep(.3)




