i=1
contar=0
divisores=[]
numero = input("Escreva um número.")
while int(i)<=int(numero):
    if int(numero)%i==0:
        contar=contar+1
        divisores.append(i)
    i=i+1
if contar<=2:
    print ("O número é primo.")
else:
    print("O número não é primo")
print(divisores)

