class Exercicio1:
    def ler5inteiros():
        quant_valores_pares = 0
        for i in range(5):
            x = int(input("DÍGITE O {}º NÚMERO: ".format(str(i+1))))
            if x%2 == 0:
                quant_valores_pares += 1
        print ("foram digitados {} valores pares".format(str(quant_valores_pares)))

