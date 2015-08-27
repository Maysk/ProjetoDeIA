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
        print len(self.listaImagens)
        for imagem in self.listaImagens:
            label = Item(imagem, self)
            pixmap = QPixmap(QString(imagem))
            print pixmap
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

