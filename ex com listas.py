notas =[]
nota=0
i=0
soma=0
nr_elementos = 0
while nota!= -1:
    nota = float(input("Escreva a sua nota."))
    if nota>=0 and nota<=20:
        soma = soma + nota
        notas.append(float(nota))
    else:
        input("opção inválida")

nr_elementos=len(notas)
media=soma/nr_elementos

print("O número de notas é ",nr_elementos)

lista_lado=""
while i<nr_elementos:
    if i==0:
        lista_lado=lista_lado+str(notas[i])
    else:
        lista_lado=lista_lado+"|"+str(notas[i])
    i=i+1
print(lista_lado)


i=nr_elementos-1
while i>=0:
    print(notas[i])
    i=i-1

print("A soma é ",soma)
print("A média é ",media)

i=0
nr_notas_acima=0
while i<nr_elementos:
    if media<notas[i]:
        nr_notas_acima=nr_notas_acima+1
    else:
        nr_notas_acima=nr_notas_acima
    i=i+1
print("O número de notas a cima da média é ",nr_notas_acima)

i=0
nr_notas_abaixo=0
while i<nr_elementos:
    if notas[i]<10:
        nr_notas_abaixo=nr_notas_abaixo+1
    else:
        nr_notas_abaixo=nr_notas_abaixo
    i=i+1
print("O número de notas abaixo de 10 é ", nr_notas_abaixo)
print("Obrigada amiguitos, voltem sempre, não se esqueçam da joinha!")









