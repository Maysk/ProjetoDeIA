from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Desenho import *
import sys

def main():
	
    app = QApplication(sys.argv)
    
    #listaNumeros = [1,0,2,8,3,5,4,7,6]
    
    a = Desenho()
    
    a.show()
        
    #listaMovimentos = ['w','w','a','a','a','d','s']
    #a.getListaMovimentos(listaMovimentos)
    
    return app.exec_()
	
if __name__ == "__main__":
	main()

