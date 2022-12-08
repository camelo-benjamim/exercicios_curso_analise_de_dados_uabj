class Exercicio5:
    def calculaSalario():
        salario_bruto = float(input("Digite o salário bruto: "))
        inss = salario_bruto * 0.11
        imposto_de_renda = salario_bruto * 0.15
        salario_liquido = salario_bruto - inss - imposto_de_renda

        print("O SALÁRIO LÍQUIDO É {}".format(str(salario_liquido)))

    