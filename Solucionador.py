import No

__author__ = 'Matheus'
from No import *
from EstruturaDeArvore import *


class Solucionador:
    def __init__(self, tabuleiroInicial):
        self.arvore = EstruturaDeArvore(tabuleiroInicial)

    def solucionar(self):
        no = self.arvore.retirarNoUmDaFronteira()

        #while(not no.estadoTabuleiro.isPecasNasPosicoesCorretas()):
        #nao sei o que coolocar aqui ainda


    def gerarDescendentesParaNo(self, no)
        listaDeTuplas = no.estadoTabuleiro.gerarListaDePossibilidades(movimentoAnterior = no.movimentoGerador) #Recebe uma lista de tuplas com o formato (movimento, estadoGerado)

        for (movimentoGerador, estadoGerado) in listaDeTuplas:
            novoNo = No(no, movimentoGerador, estadoGerado)
            no.adicionarDescendente(novoNo)







