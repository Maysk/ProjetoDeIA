__author__ = 'Matheus'

class No:
    def __init__(self, noPai, movimentoGerador, estadoTabuleiro):
        self.noPai = noPai
        self.movimentoGerador = movimentoGerador
        self.estadoTabuleiro = estadoTabuleiro
        self.nosDescendentes = []


    def adicionarDescendente(self, noDescendente):
        self.nosDescendentes.append(noDescendente)

