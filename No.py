__author__ = 'Matheus'
from EstadoTabuleiro import *


class No:

    #Inicializador
    #noPai: No; movimentoGerador: char; estadoTabuleiro: list
    def __init__(self, noPai, movimentoGerador, estadoTabuleiro):
        self.noPai = noPai
        self.movimentoGerador = movimentoGerador
        self.estadoTabuleiro = estadoTabuleiro
        self.nosDescendentes = []

        if noPai is None:
            self.nivel = 0
        else:
            self.nivel = noPai.nivel + 1


        self.numeroDeOrdem = self.estadoTabuleiro.valorHeuristico + self.nivel


    #Adiciona noDescendentes a lista de descendentes
    def adicionarDescendente(self, noDescendente):
        self.nosDescendentes.append(noDescendente)
        noDescendente.pai = self

    def __cmp__(self, other):
        return cmp(self.numeroDeOrdem, other.numeroDeOrdem)
