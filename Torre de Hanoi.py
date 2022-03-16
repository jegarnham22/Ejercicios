class TorreDeHanoi:
    
    def __init__(self):
        self.p1 = [6, 5, 4, 3, 2, 1]
        self.p2 = []
        self.p3 = []
        
    def mover_disco(self, pilar_origen, pilar_destino): 
        stack1=pilar_origen
        stack2=pilar_destino
        salida=stack1.pop()
        stack2.append(salida)

    def ToH(self, n , p1, p2, p3):
        if n==1:
            print("Disk 1 from",p1,"to",p2)
            mover_disco(p1,p2)
            return 
        ToH(n-1, p1, p3, p2)
        print("Disk",n,"from",p1,"to",p2)
        mover_disco(p1,p2)
        ToH(n-1, p3, p2, p1)
    
    def __str__(self):
        output = ""
        # Range termina con -1 para recorrer al revés
        for i in range(5, -1, -1):
            fila = " "  # Armamos una fila a la vez, desde arriba
            # Pilar 1
            if len(self.pilar_1) > i:
                fila += str(self.pilar_1[i]) + " "
            else:
                fila += "x "
            # Pilar 2
            if len(self.pilar_2) > i:
                fila += str(self.pilar_2[i]) + " "
            else:
                fila += "x "
            # Pilar 3
            if len(self.pilar_3) > i:
                fila += str(self.pilar_3[i]) + " "
            else:
                fila += "x "
            output += fila + "\n"
        output += "=" * 7 + "\n"
        return output

