__author__ = 'Matheus'

from No import *
from GerenciadorDaFronteira import *

class Solucionador:
    #Inicializador
    #tabuleiroInicial: list
    def __init__(self, tabuleiroInicial, metodoEscolhido):
        self.funcaoHeuristicaEscolhida = self.retornarMetodoEscolhido(metodoEscolhido)
        estadoTabuleiroInicial = EstadoTabuleiro(tabuleiroInicial, self.funcaoHeuristicaEscolhida)
        self.raiz = No(None, None, estadoTabuleiroInicial)
        self.fronteira = GerenciadorDaFronteira()
        self.estadosJaAvaliados = {}


    def retornarMetodoEscolhido(self, metodoEscolhido):
        if(metodoEscolhido == 1):
            return lambda x: 0
        elif(metodoEscolhido == 2):
            return self.funcaoHeuristicaDistanciaAteObjetivo
        elif(metodoEscolhido == 3):
            return self.funcaoHeuristicaParaPecasForaDoLugar


    #Soluciona e retorna uma lista de chars onde cada char representa um movimento
    def solucionar(self):
        no = None
        self.fronteira.adicionarNoNaFronteira(self.raiz)
        pecasNasPosicoesCorretas = False

        iteradorInutil = 0
        while not (pecasNasPosicoesCorretas or self.fronteira.isVazia()):
            iteradorInutil = iteradorInutil + 1
            print(iteradorInutil)

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



    def funcaoHeuristicaParaPecasForaDoLugar(self, listaRepresentandoTabuleiro):
        totalDePecasForaDoLugar = 0

        for i in range(len(listaRepresentandoTabuleiro)-1):
            if(listaRepresentandoTabuleiro[i] != i+1):
                totalDePecasForaDoLugar = totalDePecasForaDoLugar + 1

        return totalDePecasForaDoLugar


    #Funcao Heuristica original
    def funcaoHeuristicaDistanciaAteObjetivo(self,listaRepresentandoTabuleiro):
        totalDeMovimentosLivresNecessarios = 0
        for i in range(len(listaRepresentandoTabuleiro)):
            if(listaRepresentandoTabuleiro[i] != 0 ):
                linhaAtual = i/3
                colunaAtual = i%3
                linhaCorreta = (listaRepresentandoTabuleiro[i]-1)/3
                colunaCorreta = (listaRepresentandoTabuleiro[i]-1)%3
                totalDeMovimentosLivresNecessarios += abs(linhaAtual - linhaCorreta) + abs(colunaAtual - colunaCorreta)

        return totalDeMovimentosLivresNecessarios


    def gerarDescendentesParaNo(self, no):
        #Recebe uma lista de tuplas com o formato (movimento, estadoGerado)
        listaDeTuplas = no.estadoTabuleiro.gerarListaDePossibilidades(movimentoAnterior = no.movimentoGerador)

        for (movimentoGerador, tabuleiro) in listaDeTuplas:
            #if(not self.estadoJaPassouPelaFronteira(estadoGerado)):
            estadoGerado = EstadoTabuleiro(tabuleiro, self.funcaoHeuristicaEscolhida)
            novoNo = No(no, movimentoGerador, estadoGerado)
            no.adicionarDescendente(novoNo)



