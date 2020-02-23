def data_por_extenso ():
    data=input("Escreva a data no tipo DD/MM/AAAA)")
    var = data.split('/')
    d=int(var[0])
    a=int(var[2])
    opcao="válida"
    if var[1]=="01":
        mes="janeiro"
    if var[1]=="02":
        mes="fevereiro"
    if var[1]=="03":
        mes="março"
    if var[1]=="04":
        mes="abril"
    if var[1]=="05":
        mes="maio"
    if var[1]=="06":
        mes="junho"
    if var[1] == "07":
        mes = "julho"
    if var[1] == "08":
        mes = "agosto"
    if var[1]=="09":
        mes="setembro"
    if var[1]=="10":
        mes="outubro"
    if var[1]=="11":
        mes="novembro"
    if var[1]=="12":
        mes="dezembro"
    if var[1]=="02":
        if a%4==0:
            if d>29:
                opcao="invalida"
        if a%4 != 0:
            if d>28:
                opcao="invalida"

    if var[1]=="04" or var[1]=="06" or var[1]=="09" or var[1]=="11":
        if d>30:
            opcao="invalida"

    if var[1]=="01" or var[1]=="03" or var[1]== "5" or var[1]== "7" or var[1]=="8" or var[1]=="10" or var[1]=="12":
        if d>31:
            opcao="invalida"

    if a<1900:
        opcao="invalida"


    if opcao == "válida":
        resultado =(var[0]+ " de "+ mes + " de "+ var[2])
    if opcao == "invalida":
        resultado = "Opção inválida"

    return resultado



data_extenso = data_por_extenso()
print(data_extenso)
