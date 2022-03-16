from random import choice, randint
from collections import namedtuple, defaultdict # Puedes usar defaultdict si lo deseas

def dic1(paises,personas):
    personas_por_paises={}
    for pais in paises:
        personaspais=[]
        for pp in range(0,len(personas)):
            if pais==personas[pp][1]:
                personaspais.append(personas[pp])
        personas_por_paises[pais]=personaspais

    print(personas_por_paises)

def dic2(personas):
    i = 0
    personas_por_edad={}
    while i < 100:
        edadpersonas=[]
        tuplaedad=(i,i+10)
        for e in range(0,len(personas)):
            if personas[e][0] > i and personas[e][0] <= i+10:
                edadpersonas.append(personas[e])
        personas_por_edad[tuplaedad]=edadpersonas
        i=i+10

    print(personas_por_edad)
    
paises = ['Argentina', 'Bolivia', 'Chile', 'Perú','Colombia']
Persona = namedtuple("Persona", 'edad, nacionalidad')

personas = []
for i in range(100):
    nueva_persona = Persona(randint(0, 100), choice(paises))
    personas.append(nueva_persona)

dic1(personas)





