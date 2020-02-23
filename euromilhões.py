import random
lista=[]
i=0
while i<5:
    numero = random.randrange(1, 50)

    if numero in lista:
        i=i
    else:
        lista.append(int(numero))
        i=i+1

print(lista)
lista2=[]
j=0
while j<2:
    numero = random.randrange(1, 50)

    if numero in lista2:
        j=j
    else:
        lista2.append(int(numero))
        j=j+1
print(lista2)

