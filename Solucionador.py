import No

__author__ = 'Matheus'
from No import *
from EstruturaDeArvore import *


class Solucionador:
    def __init__(self, tabuleiroInicial):
        self.arvore = EstruturaDeArvore(tabuleiroInicial)

    def solucionar(self):
        no = self.arvore.retirarNoDaFronteira()

        while(not no.estadoTabuleiro.isPecasNasPosicoesCorretas() or self.arvore.listaDeNosNaFronteira == []):
            self.gerarDescendentesParaNo(no)

            for i in no.nosDescendentes:
                self.arvore.adicionarNoNaFronteira(i)

            no = self.arvore.retirarNoDaFronteira()


    def gerarDescendentesParaNo(self, no):
        listaDeTuplas = no.estadoTabuleiro.gerarListaDePossibilidades(movimentoAnterior = no.movimentoGerador) #Recebe uma lista de tuplas com o formato (movimento, estadoGerado)

        for (movimentoGerador, estadoGerado) in listaDeTuplas:
            novoNo = No(no, movimentoGerador, estadoGerado)
            #if(not self.arvore.noJaPassouPelaFronteira(novoNo)):
            no.adicionarDescendente(novoNo)