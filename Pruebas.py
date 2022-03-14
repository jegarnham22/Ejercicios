import os
import random
################################################### importar cartas
rutaarchivo=os.path.join("cartas.csv")
with open(rutaarchivo, "rt") as archivo:
    lineas=archivo.readlines()
cartas=[]
for m in lineas:
    monstruo=m.strip().split(",")
    cartas.append(monstruo)
cartas.remove(['nombre', 'ataque', 'defensa'])
################################################### repartir cartas
j1=[]
j2=[]
rangot=10
rangom=5
random.shuffle(cartas)
for i in range(0,rangom):
    j1.append(cartas[i])
for k in range(rangom,rangot):
    j2.append(cartas[k])
rangoj1=len(j1)
rangoj2=len(j2)
print(rangoj1)
print(rangoj2)
################################################### ataque


