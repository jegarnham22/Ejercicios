import os
import random as rm
class Juego:
    
    def __init__(self, turnos):
        
        self.mazo = []
        self.j1 = []
        self.j2 = []
        
        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)
    
    def read_file(self):
        rutaarchivo=os.path.join("cartas.csv")
        with open(rutaarchivo, "rt") as archivo:
            lineas=archivo.readlines()
        mazo=[]
        for m in lineas:
            monstruo=m.strip().split(",")
            mazo.append(monstruo)
        mazo.remove(['nombre', 'ataque', 'defensa'])
        print(mazo)
    
    def repartir_cartas(self):
        j1=[]
        j2=[]
        rangot=10
        rangom=5
        random.shuffle(mazo)
        for i in range(0,rangom):
            j1.append(mazo[i])
        for k in range(rangom,rangot):
            j2.append(mazo[k])
    
    def atacar(self, atacante, defensor):
        random.shuffle(j1)
        random.shuffle(j2)
        ataque=atacante[0][1]
        defensa=defensa[0][2]
        ptos_ataque = atacante.ataque
        ptos_defensa = defensor.defensa
        # if ptos_ataque > ptos_defensa:

        # # Rellenar aquí
    
    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                # Ataca el jugador 1
                # Rellenar aquí
                pass
            else:
                # Ataca el jugador 2
                # Rellenar aquí
                pass


juego = Juego(10)