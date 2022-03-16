from time import time
from random import randint

def pertenencia_cronometrada(elemento, estructura):
    inicio = time()
    elemento in estructura
    fin = time()
    return fin - inicio

ELEMENTOS = 10 ** 7
lista_gigante = list(range(ELEMENTOS))
set_gigante = set(range(ELEMENTOS))

tiempo_total_set=0
tiempo_total_lista=0

for i in range(100):
    elemento=randint(0,ELEMENTOS)
    tiempo_set=pertenencia_cronometrada(elemento,set_gigante)
    tiempo_total_set=tiempo_total_set+tiempo_set
    tiempo_lista=pertenencia_cronometrada(elemento,lista_gigante)
    tiempo_total_lista=tiempo_total_lista+tiempo_lista
    print(f"set  -- La búsqueda de {elemento} demoró... {tiempo_set:.6f} segundos.")
    print(f"list -- La búsqueda de {elemento} demoró... {tiempo_lista:.6f} segundos.")

lista_promedio=tiempo_total_lista/100
set_promedio=tiempo_total_set/100

print(f"set  -- La búsqueda en promedio demoró... {set_promedio:.6f} segundos.")
print(f"list -- La búsqueda en promedio demoró... {lista_promedio:.6f} segundos.")
print(f"La búsqueda en la lista fue {lista_promedio / set_promedio:.2f} veces más lenta que en el set.")