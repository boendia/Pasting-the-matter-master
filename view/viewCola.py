from model import modelCola
from controller import controllerCola

class View(object):

    def selecionaMenu(self, materia):
        print ("Sua cola é: %s\n" %materia)


    def start(self):
        print("Bem vindo ao Pasting the Matter\n")
        return self.menu_materia()

    def menu_materia(self):
        print("Escolha uma das materias abaixo para visualizar a cola: \n")
        print("1-MATEMATICA\n2-PORTUGUES\n3-HISTORIA\n4-GEOGRAFIA\n5-BIOLOGIA\n6-INGLES\n")

        return int(raw_input("Digite a opção: "))

    def menu_matematica(self):
        print("Selecione o topico abaixo:\n 1-FUNÇÃO\n 2-FRAÇÃO")
        return int(raw_input("Digite a opção: "))

    def menu_portugues(self):
        print("Selecione o topico abaixo:\n 1-GRAMATICA\n 2-LITERATURA")
        return int(raw_input("Digite a opção: "))

    def menu_historia(self):
        print("Selecione o topico abaixo:\n 1-BRASIL COLONIA\n 2-IMPERIO")
        return int(raw_input("Digite a opção: "))

    def menu_geografia(self):
        print("Selecione o topico abaixo:\n 1-ESTADOS\n 2-CAPITAIS")
        return int(raw_input("Digite a opção: "))

    def menu_biologia(self):
        print("Selecione o topico abaixo:\n 1-CORPO HUMANO\n 2-VIRUS")
        return int(raw_input("Digite a opção: "))

    def menu_ingles(self):
        print("Selecione o topico abaixo:\n 1-GRAMATICA\n 2-INTERPRETAÇÃO")
        return int(raw_input("Digite a opção: "))

    @staticmethod
    def funcao():
        print("FUNÇÃO: Uma função é uma regra que relaciona cada elemento de um conjunto a um único elemento de outro."
              " O primeiro conjunto é chamado de domínio, e o segundo, contradomínio da função."
              "A função determina uma relação entre os elementos de dois conjuntos. Podemos defini-la utilizando uma "
              "lei de formação, "
              "em que, para cada valor de x, temos um valor de f(x). Chamamos x de domínio e f(x) ou y de imagem da "
              "função. "
              "A formalização matemática para a definição de função é dada por: "
              "Seja X um conjunto com elementos de x e Y um conjunto dos elementos de y, temos que: f: x → y")

    @staticmethod
    def fracao():
        print("Na matemática, as frações correspondem a uma representação das partes de um todo. "
              "Ela determina a divisão de partes iguais sendo que cada parte é uma fração do inteiro. "
              "Como exemplo podemos pensar numa pizza dividida em 8 partes iguais, sendo que cada fatia corresponde a "
              "1/8 (um oitavo) de seu total. "
              "Se eu como 3 fatias, posso dizer que comi 3/8 (três oitavos) da pizza."
              "Importante lembrar que nas frações, o termo superior é chamado de numerador enquanto o termo inferior "
              "é chamado de denominador.")

    def gramatica(self):
        print()

    def literatura(self):
        print()

    def brasil_colonia(self):
        print()

    def imperio(self):
        print()

    def estados(self):
        print()

    def capitais(self):
        print()

    def corpo_humano(self):
        print()

    def virus(self):
        print()

    def gramatica(self):
        print()

    def interpretacao(self):
        print()
