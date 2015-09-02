__author__ = 'Matheus'

from No import *

class EstruturaDeArvore:
    def __init__(self, estadoInicialDoTabuleiro):
        self.raiz = No(None,None,estadoInicialDoTabuleiro)
        self.listaDeNosQueJaPassaramPelaFronteira = []
        self.listaDeNosNaFronteira = []
        self.listaDeNosNaFronteira.append(self.raiz)


    def retirarNoDaFronteira(self):
        return self.listaDeNosNaFronteira.pop()

    def adicionarNoNaFronteira(self, no):
        return self.listaDeNosNaFronteira.append(no)

    #def noJaPassouPelaFronteira(self, no)

