#from __builtin__ import None
__author__ = 'Matheus'


class EstadoTabuleiro:
    def __init__(self, listaRepresentandoTabuleiro):
        self.listaRepresentandoTabuleiro = listaRepresentandoTabuleiro
        self.totalDeMovimentosLivresNecessarios = self.funcaoHeuristica()

    def isPecasNasPosicoesCorretas(self):
        pecasNasPosicoesCorretas = True

        for i in range(len(self.listaRepresentandoTabuleiro)-1):
            if(self.listaRepresentandoTabuleiro[i] != i+1):
                pecasNasPosicoesCorretas = False

        return pecasNasPosicoesCorretas

    def gerarIdentificador(self):
        idResultante = ''
        for i in self.listaRepresentandoTabuleiro:
            idResultante += str(i)
        return idResultante

    def gerarListaDePossibilidades(self, movimentoAnterior): #considerar as movimentacoes posiveis.
        '''retorno: lista de tuplas no formato (movimentoGerador, estadoGerado)'''
        retorno = []
        listaMovimentos = ['u','d','r','l']
        if movimentoAnterior == 'u':
            listaMovimentos.remove('d')
        elif movimentoAnterior == 'd':
            listaMovimentos.remove('u')
        elif movimentoAnterior == 'r':
            listaMovimentos.remove('l')
        elif movimentoAnterior == 'l':
            listaMovimentos.remove('r')
            
        for movimento in listaMovimentos:
            tabMovimentado = self.executarMovimento(movimento)
            if tabMovimentado is not None:
                retorno.append([movimento,EstadoTabuleiro(tabMovimentado)])
                
        return retorno
                                   
    def executarMovimento(self, movimento):    
        indiceEspacoVazio = self.listaRepresentandoTabuleiro.index(0)
        
        if movimento == 'u':
            indicePecaMovel = indiceEspacoVazio+3
            if indicePecaMovel>8: #movimento invalido
                return None
        elif movimento == 'd':
            indicePecaMovel = indiceEspacoVazio-3
            if indicePecaMovel<0:
                return None
        elif movimento == 'l':
            indicePecaMovel = indiceEspacoVazio+1
            if indicePecaMovel%3==0:
                return None
        elif movimento == 'r':
            indicePecaMovel = indiceEspacoVazio-1
            if indicePecaMovel%3==2:
                return None
        
        return self.trocarPecas(indicePecaMovel,indiceEspacoVazio)    
        
    def trocarPecas(self,indicePeca1,indicePeca2):
        '''a entrada sao os indices, nao os numeros das pecas'''
        tabuleiro = self.listaRepresentandoTabuleiro[:]
                
        auxTroca = tabuleiro[indicePeca1]
        tabuleiro[indicePeca1] = tabuleiro[indicePeca2]
        tabuleiro[indicePeca2] = auxTroca
        
        return tabuleiro
    
    def mostrarEstadoTabuleiro(self):
        for i in range(0,len(self.listaRepresentandoTabuleiro)):
            if i%3==2:
                print self.listaRepresentandoTabuleiro[i]
            else:
                print self.listaRepresentandoTabuleiro[i],
            

    def funcaoHeuristica(self):
        totalDeMovimentosLivresNecessarios = 0
        for i in range(len(self.listaRepresentandoTabuleiro)):
            if(self.listaRepresentandoTabuleiro[i] != 0 ):
                linhaAtual = i/3
                colunaAtual = i%3
                linhaCorreta = (self.listaRepresentandoTabuleiro[i]-1)/3
                colunaCorreta = (self.listaRepresentandoTabuleiro[i]-1)%3
                totalDeMovimentosLivresNecessarios += abs(linhaAtual - linhaCorreta) + abs(colunaAtual - colunaCorreta)

        return totalDeMovimentosLivresNecessarios
    
    @staticmethod
    def isSolucionavel(lista, mostrarNumInversoes = False):
        numInversoes = 0
        for i in range(0,len(lista)-1):
            for j in range(i,len(lista)):
                if((lista[i] != 0) and (lista[j] != 0) and lista[i]>lista[j]):
                    numInversoes = numInversoes + 1 
        if mostrarNumInversoes:
            print 'Numero de Inversoes: ',numInversoes
        #checa se e par
        if numInversoes%2 == 0:
            return True
        else:
            return False