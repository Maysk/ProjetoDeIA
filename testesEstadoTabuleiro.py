from EstadoTabuleiro import *


estado1 = [1,0,2,3,4,5,6,7,8]
estado2 = [1,2,3,0,4,5,6,7,8]
estado3 = [1,2,3,4,0,5,6,7,8]
estado4 = [1,2,3,4,5,6,7,8,0]



tab1 = EstadoTabuleiro(estado1)
tab2 = EstadoTabuleiro(estado2)
tab3 = EstadoTabuleiro(estado3)
tab4 = EstadoTabuleiro(estado4)

lista1 = tab1.gerarListaDePossibilidades(None)
lista2 = tab2.gerarListaDePossibilidades(None)
lista3 = tab3.gerarListaDePossibilidades('l')
lista4 = tab4.gerarListaDePossibilidades(None)
'''
for tupla in lista1:
    print 'Tabuleiro Inicial: '
    tab1.mostrarEstadoTabuleiro()
    print 'Movimento: ', tupla[0]
    tupla[1].mostrarEstadoTabuleiro()
    pass

print '---------------------'

for tupla in lista2:
    print 'Tabuleiro Inicial: '
    tab2.mostrarEstadoTabuleiro()
    print 'Movimento: ', tupla[0]
    tupla[1].mostrarEstadoTabuleiro()
    pass

print '---------------------'
for tupla in lista3:
    print 'Tabuleiro Inicial: '
    tab3.mostrarEstadoTabuleiro()
    print 'Movimento: ', tupla[0]
    tupla[1].mostrarEstadoTabuleiro()
    pass

print '---------------------'
for tupla in lista4:
    print 'Tabuleiro Inicial: '
    tab4.mostrarEstadoTabuleiro()
    print 'Movimento: ', tupla[0]
    print 'Heuristica: ', tupla[1].totalDeMovimentosLivresNecessarios
    tupla[1].mostrarEstadoTabuleiro()
    pass
'''

lista1 = [1,8,2,0,4,3,7,6,5]
lista2 = [8,1,2,0,4,3,7,6,5]
EstadoTabuleiro.isSolucionavel(lista1)
EstadoTabuleiro.isSolucionavel(lista2)