__author__ = 'Matheus'

#Melhoria: Talvez usar Heap
class GerenciadorDaFronteira:
    def __init__(self):
        self.fronteira = []

    def adicionarNoNaFronteira(self, no):
        self.fronteira.append(no)
        self.ordenarListaDeNosNaFronteira()

    #Retira o no com menor numeroDeOrdem
    def retirarNoDaFronteira(self):
        return self.fronteira.pop(0)

    def ordenarListaDeNosNaFronteira(self):
        self.fronteira.sort()

    def isVazia(self):
        if(self.fronteira == []):
            return True
        else:
            return False
