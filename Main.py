from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Solucionador import *
from Desenho import *
import sys


def main():	
    app = QApplication(sys.argv)
    
    listaNumeros = [1,2,3,4,5,6,7,0,8]
    #lista1 = [1,8,2,0,4,3,7,6,5]

    lista1=[7,2,4,5,0,6,8,3,1]
    #s = Solucionador(lista1)


    a = Desenho(listaPecas=lista1)
    
    
    a.show()
        
    #listaMovimentos = ['w','w','a','a','a','d','s']
    #a.getListaMovimentos(listaMovimentos)
    
    return app.exec_()

if __name__ == "__main__":
    main()
