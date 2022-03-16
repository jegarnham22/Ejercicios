from random import randint
conjunto=set()
for i in range(100):
    conjunto.add(randint(0,100))
print(conjunto)

copia=[]
for n in conjunto:
    copia.append(n)
print(copia)
