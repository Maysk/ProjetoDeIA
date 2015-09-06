__author__ = 'Matheus'

from No import *

class EstruturaDeArvore:
    def __init__(self, estadoInicialDoTabuleiro):
        self.listaDeNosNaFronteira = []
        self.raiz = No(None,None,estadoInicialDoTabuleiro)
        self.adicionarNoNaFronteira(self.raiz)


    def adicionarNoNaFronteira(self, no):
        return self.listaDeNosNaFronteira.append(no)

    def retirarNoDaFronteira(self):
        return self.listaDeNosNaFronteira.pop(0)

    def ordenarListaDeNosNaFronteira(self):
        self.listaDeNosNaFronteira.sort()


