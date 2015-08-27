from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Desenho import *
import sys

def main():
	
    app = QApplication(sys.argv)
    
    listaNumeros = [1,2,3,4,5,6,7,0,8]
    
    a = Desenho(listaPecas=listaNumeros)
    
    a.show()
        
    #listaMovimentos = ['w','w','a','a','a','d','s']
    #a.getListaMovimentos(listaMovimentos)
    
    return app.exec_()
	
if __name__ == "__main__":
	main()
	