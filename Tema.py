from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
import time

class DialogoTema(QDialog):
    def __init__(self,parent):
        super(QDialog,self).__init__(parent)
        self.setWindowTitle('Escolher Tema')
        self.imagemSelecionada = ''
        self.setLayout(QGridLayout(self))
        self.carregarImagens()

    def carregarImagens(self, diretorio = 'Temas/'):
        self.listaImagens = []
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        for imagem in os.listdir(diretorio):
            if imagem != 'Thumbs.db':
                self.listaImagens.append(diretorio+imagem)
        self.preencher()

    def preencher(self,imagensPorLinha = 4, larguraMaxima = 150):
        linha = 0
        coluna = 0
        for imagem in self.listaImagens:
            label = Item(imagem, self)
            pixmap = QPixmap(QString(imagem))
            pixmap = pixmap.scaled(larguraMaxima,50,Qt.KeepAspectRatioByExpanding)
            label.setPixmap(pixmap)
            self.layout().addWidget(label,linha,coluna)
            coluna = coluna + 1
            if coluna % imagensPorLinha == 0:
                linha = linha + 1
                coluna = 0

        botao = QPushButton('Pesquisar Tema')
        botao.setFixedSize(larguraMaxima,larguraMaxima)
        botao.clicked.connect(self.clicouBotao)
        self.layout().addWidget(botao,linha,coluna)

    def clicouBotao(self):

        [self.imagemSelecionada,result] = DialogoArquivo.getArquivoSelecionado()
        if result != 0:
            self.close()

    @staticmethod    
    def getTemaSelecionado(parent = None):
        dialog = DialogoTema(parent)
        result = dialog.exec_()
        return dialog.imagemSelecionada
    
    @staticmethod
    def dividirTema(tema, tamanhoTabuleiro, parent = None):
        listaImagens = []    
        imagem = QPixmap(tema).scaled(tamanhoTabuleiro,tamanhoTabuleiro)
        for i in range(0,8):
            if (i/3) == 0:
                x = i*(tamanhoTabuleiro/3.0)
                y = 0
            elif (i/3) == 1:
                x = (i-3)*(tamanhoTabuleiro/3.0)
                y = tamanhoTabuleiro/3.0
            elif (i/3) == 2:
                x = (i-6)*(tamanhoTabuleiro/3.0)
                y = 2*tamanhoTabuleiro/3.0
            listaImagens.append(imagem.copy(x,y,tamanhoTabuleiro/3.0,tamanhoTabuleiro/3.0))
        
        #a = VisualizadorDePixMap(listaImagens,titulo='')
        #a.show()
        #a.exec_()
        return listaImagens

class Item(QLabel):
    def __init__(self,imagem, dialogo):
        super(QLabel,self).__init__()
        self.dialogo = dialogo
        self.imagem = imagem

    def mousePressEvent(self, e):
        self.dialogo.imagemSelecionada = self.imagem
        self.dialogo.close()

class DialogoArquivo(QFileDialog):
    def __init__(self):
        super(QFileDialog,self).__init__()
        
    @staticmethod
    def getArquivoSelecionado(parent = None):
        dialog = DialogoArquivo()
        result = dialog.exec_()
        return [dialog.selectedFiles().takeFirst(),result]

class VisualizadorDePixMap(QWidget):
    def __init__(self, listaPixmap, titulo):
        super(QWidget,self).__init__()
        self.imagens = listaPixmap
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100,610,610)
        
    def paintEvent(self, event):
        
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        #background branco:
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        for i in range(0,len(self.imagens)):
            if (i==0):
                x = 0
                y = 0
            if (i==1):
                x = 200 
                y = 0
            if (i==2):
                x = 400
                y = 0
            if (i==3):
                x = 0
                y = 200
            if (i==4):
                x = 200
                y = 200
            if (i==5):
                x = 400 
                y = 200
            if (i==6):
                x = 0
                y = 400
            if (i==7):
                x = 200
                y = 400
            if (i==8):
                x = 400
                y = 400
            paint.drawPixmap(x,y,200,200,self.imagens[i])

            
            
        
        paint.end()
    pass
