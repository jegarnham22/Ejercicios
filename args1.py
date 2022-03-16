def imprimir(numeros, separador,fin="\n"):
    for fila in numeros:
        print(*fila, sep=separador,end=fin)

numeros = [[str((fila * 10 + columna)).zfill(2) for columna in range(10)] for fila in range(10)]

print("con espacios:")
imprimir(numeros," ")
print("con guiones:")
imprimir(numeros,"-")
print("con > y sin saltos:")
imprimir(numeros,">","")