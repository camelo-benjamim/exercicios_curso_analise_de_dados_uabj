class Exercicio6:
    def valorPagamento():
        continuar = True
        while continuar:
            total_valor_dia = 0
            total_prestacoes_dia = 0
            multa = 0.03
            juros_dia = 0.01
            valor_prestacao = float(input("VALOR DA PRESTAÇÃO:  "))
            numero_dias_atraso = int(input("NÚMERO DE DIAS DE ATRASO: "))
            
            if valor_prestacao == 0:
                print("RELATÓRIO: ")
                print("VALOR TOTAL DAS PRESTAÇÕES PAGAS NO DIA {}".format(str(total_valor_dia)))
                print("TOTAL DE PRESTAÇÕES PAGAS NO DIA {}".format(str(total_prestacoes_dia)))
            else:
                if numero_dias_atraso == 0:
                    continuar = False
                    valor_total = valor_prestacao
                    print(valor_total)
                else:
                    multa = valor_prestacao * multa
                    juros =(1 + juros_dia) ** numero_dias_atraso
                    valor_c_juros = juros * valor_prestacao
                    valor_total = multa + valor_c_juros
                    ##ARREDONANDO VALOR TOTAL PARA 3 CASAS DECIMAIS
                    valor_total = round(valor_total,3)
                    print("O VALOR TOTAL É {}".format(str(valor_total)))
                    total_valor_dia += valor_total
                    total_prestacoes_dia += 1
