__author__ = 'Matheus'

from No import *

class EstruturaDeArvore:

    #Inicializador
    #estadoInicialDoTabuleiro: list
    def __init__(self, estadoInicialDoTabuleiro):
        self.listaDeNosNaFronteira = []
        self.raiz = No(None,None, estadoInicialDoTabuleiro)
        self.adicionarNoNaFronteira(self.raiz)

    #Adiciona um no a listaDeNosNaFronteira
    def adicionarNoNaFronteira(self, no):
        self.listaDeNosNaFronteira.append(no)
        self.ordenarListaDeNosNaFronteira()


    #Retira o no com menor numeroDeOrdem
    def retirarNoDaFronteira(self):
        return self.listaDeNosNaFronteira.pop(0)

    def ordenarListaDeNosNaFronteira(self):
        self.listaDeNosNaFronteira.sort()


