lista=[]
listapares=[]
i=0
while i<10:
    numero=input("Introduza um número")
    lista.append(int(numero))
    i = i + 1
lista_ordenada=sorted(lista)
print(lista_ordenada)

i=0
while i<10:
    resto=int(lista_ordenada[i]%2)
    if resto==0:
        print(lista_ordenada[i])
    i=i+1



