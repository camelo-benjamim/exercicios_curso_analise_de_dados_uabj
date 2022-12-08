from math import fabs
class Exercicio2:
    def duracaoPartida():
        continuar = True
        while continuar:
            ##COMO NÃO EXISTE HORA NEGATIVA, IREI CONVERTER OS VALORES PARA POSITIVO, POS CASO
            ##O USUÁRIO PASSE COMO INPUT UMA HORA NEGATIVA O RESULTADO SERÁ SEU MÓDULO.
            hora_inicio = fabs(int(input("Digite a hora de início do jogo: ")))
            ## FOI ADICIONADO UM TRATAMENTO DE DADOS POIS UM DIA SÓ POSSUI 24 HORAS E UMA HORA POSSUI 60 MINUTOS
            while hora_inicio > 24:
                print("UM DIA SÓ POSSUI 24 HORAS")
                hora_inicio = fabs(int(input("Digite a hora de início do jogo: ")))
            minuto_inicio = fabs(int(input("Digite o minuto de início do jogo: ")))
            while minuto_inicio > 60:
                print("UMA HORA SÓ POSSUI 60 MINUTOS")
                minuto_inicio = fabs(int(input("Digite o minuto de início do jogo: ")))
            hora_fim = fabs(int(input("Digite a hora de fim do jogo: ")))
            while hora_fim > 24:
                print("UM DIA SÓ POSSUI 24 HORAS")
                hora_fim = fabs(int(input("Digite a hora de fim do jogo: ")))
            minuto_fim = fabs(int(input("Digite o minuto de fim do jogo: ")))
            while minuto_fim > 60:
                print("UMA HORA SÓ POSSUI 60 MINUTOS")
                minuto_fim = fabs(int(input("Digite o minuto do fim do jogo: ")))
            conv_hora_inicio_min = hora_inicio * 60
            conv_hora_fim_min = hora_fim * 60
            
            if conv_hora_fim_min + minuto_fim < conv_hora_inicio_min + minuto_inicio:
                total_tempo_min = 1440 - (conv_hora_inicio_min - conv_hora_fim_min) - (minuto_inicio - minuto_fim)
                total_horas = int(total_tempo_min/60)
                total_minutos = total_tempo_min%60
                print ("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(total_horas),str(total_minutos)))
                continuar = False
            elif conv_hora_fim_min == conv_hora_inicio_min and minuto_inicio == minuto_fim:
                ##NESTE CASO IREI CONSIDERAR VALORES IGUAIS COMO 0 MINUTOS AO INVÉS DE 24H 
                print ("ERRO, O JOGO NÃO PODE DURAR 0 MINUTOS")
            else:
                total_tempo_min = (conv_hora_fim_min + minuto_fim) - (conv_hora_inicio_min + minuto_inicio)
                total_horas = int(total_tempo_min/60)
                total_minutos = total_tempo_min%60
                print ("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(str(total_horas),str(total_minutos)))
                continuar = False