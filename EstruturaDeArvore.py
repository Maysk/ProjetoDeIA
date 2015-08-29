__author__ = 'Matheus'

from No import *

class EstruturaDeArvore:
    def __init__(self, estadoInicialDoTabuleiro):
        self.raiz = No(None,None,estadoInicialDoTabuleiro)
        self.listaDeVerticesNaFronteira = []
        self.listaDeVerticesNaFronteira.append(self.raiz)


    def retirarNoDaFronteira(self):
        return None

    def adicionarNoNaFronteira(self):
        return None