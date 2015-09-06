import No

__author__ = 'Matheus'
from No import *
from EstruturaDeArvore import *


class Solucionador:
    def __init__(self, tabuleiroInicial):
        self.arvore = EstruturaDeArvore(tabuleiroInicial)
        self.estadosQueJaPassaramPelaFronteira = {}


    def solucionar(self):
        no = None
        pecasNasPosicoesCorretas = False
        listaDeNosNaFronteiraVazia = False

        while not (pecasNasPosicoesCorretas or listaDeNosNaFronteiraVazia):
            self.arvore.ordenarListaDeNosNaFronteira()
            no = self.arvore.retirarNoDaFronteira()
            self.gerarDescendentesParaNo(no)

            for i in no.nosDescendentes:
                self.arvore.adicionarNoNaFronteira(i)

            pecasNasPosicoesCorretas = no.estadoTabuleiro.isPecasNasPosicoesCorretas()
            listaDeNosNaFronteiraVazia = self.arvore.listaDeNosNaFronteira == []


        if pecasNasPosicoesCorretas:
            return self.gerarListaSolucionadora(no)
        else:
            raise ValueError("Deu Ruim!")



    def gerarListaSolucionadora(self,no):
        listaSolucionadora = []
        chegouNaRaiz = False
        noCorrente = no
        while not noCorrente.noPai is None:
            listaSolucionadora.insert(0, noCorrente.movimentoGerador)
            noCorrente = noCorrente.noPai
        return listaSolucionadora




    def adicionarAListaDeEstadosQueJaPassaramPelaFronteira(self,estado):
        self.estadosQueJaPassaramPelaFronteira[estado.gerarIdentificador()] = True


    def estadoJaPassouPelaFronteira(self, estado):
        try:
            return self.estadosQueJaPassaramPelaFronteira[estado.gerarIdentificador()]
        except KeyError:
            return False


    def gerarDescendentesParaNo(self, no):
        #Recebe uma lista de tuplas com o formato (movimento, estadoGerado)
        listaDeTuplas = no.estadoTabuleiro.gerarListaDePossibilidades(movimentoAnterior = no.movimentoGerador)

        for (movimentoGerador, estadoGerado) in listaDeTuplas:
            #if(not self.estadoJaPassouPelaFronteira(estadoGerado)):
            novoNo = No(no, movimentoGerador, estadoGerado)
            no.adicionarDescendente(novoNo)

