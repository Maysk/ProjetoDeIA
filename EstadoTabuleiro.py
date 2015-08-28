__author__ = 'Matheus'


class EstadoTabuleiro:
    def __init__(self, listaRepresentandoTabuleiro):
        self.lisRepresentandoTabuleiro = listaRepresentandoTabuleiro

    def isPecasNasPosicoesCorretas(self):
        pecasNasPosicoesCorretas = True

        for i in range(1,8,None):
            if(self.lisRepresentandoTabuleiro[i] == i):
                pecasNasPosicoesCorretas = False

        return pecasNasPosicoesCorretas




    def gerarListaDePossibilidades(self, movimentoAnterior): #considerar as movimentacoes posiveis.
        return None