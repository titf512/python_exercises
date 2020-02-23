class imc:
    def dados (self):
        nome_lista = []
        peso_lista = []
        altura_lista = []
        i=0
        while i<2:
            nome = input(str("Escreva o seu nome"))
            nome_lista.append(nome)
            peso = input("Qual é o seu peso?")
            peso_lista.append(peso)
            altura = input("Qual é a sua altura")
            altura_lista.append(altura)
            i=i+1

        return nome_lista, peso_lista, altura_lista

    def IMC (self,peso_lista,altura_lista):
        i=0
        imc_calculo = []
        while i<2:
            imc_calculo2 = float(peso_lista[i])/(float(altura_lista[i])**2)
            imc_calculo.append(imc_calculo2)
            i=i+1

        return imc_calculo

    def resultado(self, imc_calculo, nome_lista):
        i=0
        while i<2:
            if imc_calculo[i]<30.0 and imc_calculo[i]>=25.0:
                print(nome_lista[i] + " Está em sobrepeso.")

            if imc_calculo[i]<25.0 and imc_calculo[i]>=18.5:
                print(nome_lista[i] + " Tem o peso normal.")

            if imc_calculo[i]<18.5:
                print(nome_lista[i] + " Está a baixo do peso normal.")
            i=i+1

myobject=imc()
nome_lista,peso_lista,altura_lista = myobject.dados()
imc_calculo = myobject.IMC(peso_lista, altura_lista)
myobject.resultado(imc_calculo, nome_lista)


