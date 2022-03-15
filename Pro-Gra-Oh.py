import os
import random
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

        for m in lineas:
            monstruo=m.strip().split(",")
            self.mazo.append(monstruo)
        self.mazo.remove(['nombre', 'ataque', 'defensa'])
       
    
    def repartir_cartas(self):
        rangot=10
        rangom=5
        random.shuffle(self.mazo)
        for i in range(0,rangom):
            self.j1.append(self.mazo[i])
        for k in range(rangom,rangot):
            self.j2.append(self.mazo[k])
    
    def atacar(self, atacante, defensor):
        random.shuffle(atacante)
        random.shuffle(defensor)
        ptos_ataque=atacante[0][1]
        ptos_defensa=defensor[0][2]
        if ptos_ataque > ptos_defensa:
            defensor.pop(0)
            print(f"El jugador atacante gana este turno")

        elif ptos_defensa > ptos_ataque:
            atacante.pop(0)
            print(f"El jugador defensor gana este turno")

        else:
            print("Empate")

    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if len(self.j1)>0 and len(self.j2)>0:
                if i % 2:
                    print(f"Ataca el jugador 1")
                    self.atacar(self.j1,self.j2)
                    cartasj1=len(self.j1)
                    cartasj2=len(self.j2)
                    print(f"Al jugador 1 le quedan {cartasj1} cartas y al jugador 2 le quedan {cartasj2} cartas")
                
                else:
                    print(f"Ataca el jugador 2")
                    self.atacar(self.j2,self.j1)
                    cartasj1=len(self.j1)
                    cartasj2=len(self.j2)
                    print(f"Al jugador 1 le quedan {cartasj1} cartas y al jugador 2 le quedan {cartasj2} cartas")
    
            elif len(self.j1) == 0:
                print("Ha ganado el jugador 2")
                break
            elif len(self.j2) == 0:
                print("Ha ganado el jugador 1")
                break
        print("Juego terminado")


juego = Juego(10)