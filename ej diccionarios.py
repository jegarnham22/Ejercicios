from string import ascii_lowercase as letras
Abecedario = {}
largo=len(letras)
for letra in range(largo):
    Abecedario[letra]=letras[letra]
print(Abecedario)
for i in list(Abecedario):
    if i%3==0 and i>0:
        Abecedario.pop(i)
print(Abecedario)