__author__ = 'Matheus'

from No import *
from GerenciadorDaFronteira import *

class Solucionador:
    #Inicializador
    #tabuleiroInicial: list
    def __init__(self, tabuleiroInicial):
        self.raiz = No(None, None, tabuleiroInicial)
        self.fronteira = GerenciadorDaFronteira()
        self.estadosJaAvaliados = {}

    #Soluciona e retorna uma lista de chars onde cada char representa um movimento
    def solucionar(self, metodoEscolhido):
        no = None
        self.fronteira.adicionarNoNaFronteira(self.raiz)
        pecasNasPosicoesCorretas = False

        iteradorInutil = 0
        while not (pecasNasPosicoesCorretas or self.fronteira.isVazia()):
            iteradorInutil = iteradorInutil + 1
            no = self.fronteira.retirarNoDaFronteira()

            if (self.estadoJaFoiAvaliado(no.estadoTabuleiro)):
               continue
            else:
                self.adicionarAoEstadosJaAvaliados(no.estadoTabuleiro)

            self.gerarDescendentesParaNo(no)
            for i in no.nosDescendentes:
                self.fronteira.adicionarNoNaFronteira(i)

            pecasNasPosicoesCorretas = no.estadoTabuleiro.isPecasNasPosicoesCorretas()


        print(iteradorInutil)
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


    def adicionarAoEstadosJaAvaliados(self,estado):
        self.estadosJaAvaliados[estado.gerarIdentificador()] = True


    def estadoJaFoiAvaliado(self, estado):
        try:
            return self.estadosJaAvaliados[estado.gerarIdentificador()]
        except KeyError:
            return False


    def gerarDescendentesParaNo(self, no):
        #Recebe uma lista de tuplas com o formato (movimento, estadoGerado)
        listaDeTuplas = no.estadoTabuleiro.gerarListaDePossibilidades(movimentoAnterior = no.movimentoGerador)

        for (movimentoGerador, estadoGerado) in listaDeTuplas:
            #if(not self.estadoJaPassouPelaFronteira(estadoGerado)):
            novoNo = No(no, movimentoGerador, estadoGerado)
            no.adicionarDescendente(novoNo)

