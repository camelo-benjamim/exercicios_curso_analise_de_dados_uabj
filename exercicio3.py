class Exercicio3:
    def leituraSenha():
        while True:
            senha = input("DIGITE A SENHA: ")
            if senha == "2002":
                print("ACESSO PERMITIDO")
                break
            else:
                print("SENHA INVÁLIDA")
            