p1 = [6, 5, 4, 3, 2, 1]
p2 = []
p3 = []

def mover_disco(pilar_origen, pilar_destino): 
    stack1=pilar_origen
    stack2=pilar_destino

    salida=stack1.pop()
    stack2.append(salida)

def ToH(n , p1, p2, p3):
    if n==1:
        print("Disk 1 from",p1,"to",p2)
        mover_disco(p1,p2)
        return 
    ToH(n-1, p1, p3, p2)
    print("Disk",n,"from",p1,"to",p2)
    mover_disco(p1,p2)
    ToH(n-1, p3, p2, p1)
          
#################
dic={"Mensaje":["main.py", "windows.py", "user.txt"]}
print(dic)

