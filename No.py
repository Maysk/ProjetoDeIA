__author__ = 'Matheus'

class No:
    def __init__(self, noPai, movimentoGerador, estadoTabuleiro):
        self.noPai = noPai
        self.movimentoGerador = movimentoGerador
        self.estadoTabuleiro = estadoTabuleiro
        self.nosDescendentes = []
        if noPai is None:
            self.nivel = 0
        else:
            self.nivel = noPai.nivel + 1
        self.numeroDeOrdem = estadoTabuleiro.funcaoHeuristica() + self.nivel


    def adicionarDescendente(self, noDescendente):
        self.nosDescendentes.append(noDescendente)
        noDescendente.pai = self

    def __cmp__(self, other):
        return cmp(self.numeroDeOrdem, other.numeroDeOrdem)
