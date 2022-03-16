from string import ascii_lowercase as letras
Abecedario = {}
largo=len(letras)
for letra in range(largo):
    Abecedario[letra]=letras[letra]
print(Abecedario)
for i in Abecedario:
    if i%3==0:
        Abecedario[i]=" "
print(Abecedario)