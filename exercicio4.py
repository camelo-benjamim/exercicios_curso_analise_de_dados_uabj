class Exercicio4:
    def calcularIdadeMedia():
        idades = []
        contador = 1
        continuar = True
        while continuar:
            idade_individuo = int(input("DIGITE A IDADE DO {}º INDIVÍDUO: ".format(str(contador))))
            contador += 1
            if idade_individuo >=0:
                idades.append(idade_individuo)
            else:
                continuar = False
                somatorio=0
                for i in idades:
                    somatorio += i
                    media = somatorio / len(idades)
                print("A MÉDIA DAS IDADAS É {}".format(str(media)))
                