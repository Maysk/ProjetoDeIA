import No

__author__ = 'Matheus'
from No import *
from EstruturaDeArvore import *


class Solucionador:
    #Inicializador
    #tabuleiroInicial: list
    def __init__(self, tabuleiroInicial):
        self.arvore = EstruturaDeArvore(tabuleiroInicial)
        self.estadosQueJaPassaramPelaFronteira = {}

    #Soluciona e retorna uma lista de chars onde cada char representa um movimento
    def solucionar(self):
        no = None
        pecasNasPosicoesCorretas = False
        listaDeNosNaFronteiraVazia = False

        while not (pecasNasPosicoesCorretas or self.arvore.listaDeNosNaFronteira == []):
            no = self.arvore.retirarNoDaFronteira()

#            Talvez seja usado, talvez nao
            if (self.estadoJaPassouPelaFronteira(no.estadoTabuleiro)):
               continue
            else:
                self.adicionarAListaDeEstadosQueJaPassaramPelaFronteira(no.estadoTabuleiro)

            self.gerarDescendentesParaNo(no)
            for i in no.nosDescendentes:
                self.arvore.adicionarNoNaFronteira(i)

            pecasNasPosicoesCorretas = no.estadoTabuleiro.isPecasNasPosicoesCorretas()


        if pecasNasPosicoesCorretas:
            return self.gerarListaSolucionadora(no)
        else:
            raise ValueError("Deu Ruim!")


    #Tipo de retorno: list
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

