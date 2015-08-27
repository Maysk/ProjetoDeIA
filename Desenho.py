from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Tema import *
import os
import random
import time
        
class Desenho(QWidget):
    def __init__(self, tamanho = 600, borda = 10,  bordaMenu = 20, listaPecas = [], tema = None, redErrado=0,greenErrado=102,blueErrado=200, redCerto=74,greenCerto=178,blueCerto=79,parent=None):
        QWidget.__init__(self, parent)
        
        #Configuracoes Gerais:
        self.tamanho = tamanho
        self.borda = borda
        if(os.name == 'nt'): #se for Windows
            self.bordaMenu = bordaMenu
        else: #se for Linux ou outro
            self.bordaMenu = 0
        self.bordaRodape = (self.tamanho/40) + 10
        self.corErrado = QColor(redErrado,greenErrado,blueErrado)
        self.corCerto = QColor(redCerto,greenCerto,blueCerto)
        # setGeometry(x_pos, y_pos, width, height)    
        self.setGeometry(100, 100, self.tamanho+(2*self.borda), self.tamanho+(2*self.borda)+self.bordaMenu+self.bordaRodape)
        self.setWindowTitle('Joguinho Weeeeeeeeee')

        #Menus:
        self.myQMenuBar = QMenuBar(self)
        menuOpcoes = self.myQMenuBar.addMenu('Opcoes')
        
        #Menu gerar novo:
        acaoNovo = QAction('&Novo Jogo',self)
        acaoNovo.setShortcut('F2')
        acaoNovo.triggered.connect(self.acaoNovoJogo)         
        menuOpcoes.addAction(acaoNovo)
        
        #Menu selecionar tema(imagem):
        acaoTema = QAction('&Inserir Tema',self)
        acaoTema.setShortcut('Insert')
        acaoTema.triggered.connect(self.acaoTemaEvent)
        menuOpcoes.addAction(acaoTema)

        #Menu solucionar com magia negra:
        acaoSoluc = QAction('&Solucionar',self)
        acaoSoluc.setShortcut('End')
        acaoSoluc.triggered.connect(self.acaoSolucionar)
        menuOpcoes.addAction(acaoSoluc)
        
        #Menu fechar
        acaoSair = QAction(QIcon('exit.png'),'&Sair',self)
        acaoSair.setShortcut('Esc')
        acaoSair.triggered.connect(qApp.quit)
        menuOpcoes.addAction(acaoSair)

        #criacao dos objetos do desenho:
        self.tab = Tabuleiro(self.tamanho, self.borda, self.bordaMenu, self.bordaRodape)        
        self.listaPecas = listaPecas
        if not self.listaPecas:
            [self.listaPecas,self.espacoVazio] = self.gerarPecasAleatoriamente()
        else:
            [self.listaPecas,self.espacoVazio] = self.gerarPecasDeLista(listaPecas)
            
        if tema is not None:
            self.setImagemDasPecas(DialogoTema.dividirTema(tema, self.tamanho))
    
    #EVENTO PRINCIPAL DE PINTURA
    def paintEvent(self, event):
        
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        #background branco:
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        
        paint.setPen(Qt.black)
        #Desenhar Tabuleiro        
        self.tab.drawTabuleiro(paint)
        
        #Desenhar pecas:
        paint.setPen(QColor(Qt.white))
        for peca in self.listaPecas:
            peca.drawPeca(paint)
        
        #Fechar pintor
        paint.end()
	
    def acaoTemaEvent(self):
        selecionado = DialogoTema.getTemaSelecionado()
        print 'Tema selecionado:',selecionado 
        self.setImagemDasPecas(DialogoTema.dividirTema(selecionado, self.tamanho))
                
    def acaoNovoJogo(self):
        self.tab.qtdMovimentos = 0
        [self.listaPecas,self.espacoVazio] = self.gerarPecasAleatoriamente()
        QApplication.processEvents()        
        self.update()
        
    def acaoSolucionar(self):
        QMessageBox.about(self, 'Lamento :(', 'Esta funcionalidade nao esta implementada\n\n Ainda :D')
        
    def setImagemDasPecas(self, listaImagens):       
        for peca in self.listaPecas:
            peca.imagem = listaImagens[peca.getNumero().toInt()[0]-1]
                    
    def gerarPecasAleatoriamente(self):
        listaPecas = []
        listaNumerosAleatorios = range(0,9)
        random.shuffle(listaNumerosAleatorios)
        for i in range(0,8):
            listaPecas.append(Peca(i+1, listaNumerosAleatorios[i], self.tamanho, self.borda,self.bordaMenu,self.corErrado,self.corCerto))
        espacoVazio = listaNumerosAleatorios[8]
        return [listaPecas,espacoVazio]
    
    def gerarPecasDeLista(self,listaNumeros):
        listaPecas = []
        for i in range(0,len(listaNumeros)):
            if listaNumeros[i] != 0:
                listaPecas.append(Peca(listaNumeros[i], i, self.tamanho, self.borda, self.bordaMenu, self.corErrado, self.corCerto))
            else:
                espacoVazio = i
        return [listaPecas,espacoVazio]
        
    
    def showListaPecas(self):
        for peca in self.listaPecas:
            print 'Peca de numero: ',peca.getNumero(),'esta na posicao',peca.getPosicao()
        print 'Posicao do espaco vazio: ',self.espacoVazio
            
    def trocarPecaPorEspacoVazio(self,peca):
        auxTroca = peca.getPosicao()
        peca.setPosicao(self.espacoVazio)
        self.espacoVazio = auxTroca
        
    def buscarPecaMovel(self,pecaMovel):
        
        for peca in self.listaPecas:
                if(peca.getPosicao() == pecaMovel):
                    self.trocarPecaPorEspacoVazio(peca)                    
        self.tab.incrementarQtdMovimentos()        
        
    
    def moverLogica(self,botao):
        movimentoValido = False
        posicaoFinal = -1
        if(botao == Qt.Key_W or botao == Qt.Key_Up):#mover pra cima
            pecaMovel = self.espacoVazio + 3            
            if(pecaMovel<=8): #movimento valido
                print 'Mover para cima' 
                movimentoValido = True
                posicaoFinal = pecaMovel-3                 
                self.buscarPecaMovel(pecaMovel)                
                        
        elif(botao == Qt.Key_S or botao == Qt.Key_Down):#mover pra baixo
            pecaMovel = self.espacoVazio - 3
            if(pecaMovel>=0):
                print 'Mover para baixo'
                movimentoValido = True
                posicaoFinal = pecaMovel+3
                self.buscarPecaMovel(pecaMovel)
                
        elif(botao == Qt.Key_A or botao == Qt.Key_Left):#mover pra esquerda
            pecaMovel = self.espacoVazio + 1
            if(pecaMovel%3 != 0):
                print 'Mover para esquerda'
                movimentoValido = True
                posicaoFinal = pecaMovel-1
                self.buscarPecaMovel(pecaMovel)                
                
        elif(botao == Qt.Key_D or botao == Qt.Key_Right):#mover pra direita
            pecaMovel = self.espacoVazio - 1
            if(pecaMovel%3 != 2):
                print 'Mover para direita'
                movimentoValido = True
                posicaoFinal = pecaMovel+1
                self.buscarPecaMovel(pecaMovel)
                
        else: #botao invalidO   
            print 'Botao invalido'
        if movimentoValido:
            return [pecaMovel,posicaoFinal]
        return [-1,-1]
    
    def interpolacaoCor(self, cor1, cor2, frames = 25):
        listaCores = []
        if (cor1==None or cor2==None):
            return listaCores
        
        passoR = (cor2.red() - cor1.red())/float(frames)
        passoG = (cor2.green() - cor1.green())/float(frames)
        passoB = (cor2.blue() - cor1.blue())/float(frames)
        
        for i in range(0,frames+1):
            listaCores.append([cor1.red()+(i*passoR),cor1.green()+(i*passoG),cor1.blue()+(i*passoB)])
            
        return listaCores
        
        
    def interpolacaoTranslacao(self, posicaoInicial, posicaoFinal, frames = 12):
        listaCoordenadas = []
        
        if(posicaoInicial / 3 == 0):
            x1 = self.borda + (posicaoInicial * self.tamanho/3)
            y1 = self.borda            
        if(posicaoInicial / 3 == 1):
            x1 = self.borda + (posicaoInicial-3) * self.tamanho/3
            y1 = self.borda + self.tamanho/3
        if(posicaoInicial / 3 == 2):
            x1 = self.borda + (posicaoInicial-6) * self.tamanho/3
            y1 = self.borda + 2*self.tamanho/3
            
        if(posicaoFinal / 3 == 0):
            x2 = self.borda + posicaoFinal * self.tamanho/3
            y2 = self.borda            
        if(posicaoFinal / 3 == 1):
            x2 = self.borda + (posicaoFinal-3) * self.tamanho/3
            y2 = self.borda + self.tamanho/3
        if(posicaoFinal / 3 == 2):
            x2 = self.borda + (posicaoFinal-6) * self.tamanho/3
            y2 = self.borda + 2*self.tamanho/3  
        passoX = (x2-x1)/float(frames)
        passoY = (y2-y1)/float(frames)
        
        for i in range(0,frames+1):
            listaCoordenadas.append([x1 + (i*passoX),y1 + (i*passoY)])
        
        return listaCoordenadas    
        
    def moverInterface(self, posicaoInicial, posicaoFinal,delayMovimento = 0.001, delayCor = 0.001):
        
        for peca in self.listaPecas:
            if(peca.getPosicao() == posicaoFinal):
                #se for a peca que vai mover:
                pass
                listaCoordenadas = self.interpolacaoTranslacao(posicaoInicial, posicaoFinal)
                for coordenada in listaCoordenadas:
                    peca.xOrigem = coordenada[0]
                    peca.yOrigem = coordenada[1]
                    peca.xOrigemTexto = peca.xOrigem + self.tamanho/6 - self.tamanho/60
                    peca.yOrigemTexto = peca.yOrigem + self.tamanho/6 + self.tamanho/60
                    QApplication.processEvents()
                    time.sleep(delayMovimento)
                    self.update()
                if(peca.imagem is None):
                    if((posicaoInicial+1) != peca.getNumero().toInt()[0] and (posicaoFinal+1) == peca.getNumero().toInt()[0]): #se estava errado e foi pra certo
                        cor1 = self.corErrado
                        cor2 = self.corCerto
                    elif((posicaoInicial+1) == peca.getNumero().toInt()[0] and (posicaoFinal+1) != peca.getNumero().toInt()[0]): # se estava certo e foi pra errado
                        cor1 = self.corCerto
                        cor2 = self.corErrado
                    else:
                        cor1 = None
                        cor2 = None
                        pass
                    listaCores = self.interpolacaoCor(cor1, cor2)
                    for cor in listaCores:
                        peca.cor = QColor(int(cor[0]),int(cor[1]),int(cor[2]))
                        QApplication.processEvents()
                        time.sleep(delayCor)
                        self.update()
            
            
        
        pass
    
    def mover(self, botao):
        [posicaoInicial,posicaoFinal] = self.moverLogica(botao)    
        if(posicaoInicial != -1 and posicaoFinal != -1):     
            self.setDisabled(True)  
            self.moverInterface(posicaoInicial,posicaoFinal)        
            self.setDisabled(False)
            self.checarFimDoJogo()
            
    def checarFimDoJogo(self):
        posicaoErrada = False
        for peca in self.listaPecas:
            if(peca.getNumero().toInt()[0] != peca.getPosicao()+1):
                posicaoErrada = True
        if(not posicaoErrada): #terminou o jogo
            QMessageBox.about(self, 'Yaaaay :D', 'Parabens!!!\n\n Voce terminou o jogo com %s movimentos!!!' %self.tab.qtdMovimentos)
            
    
    def parseListaMovimentosParaKey(self, lista):
        listaKeys = []
        for movimento in lista:
            if(movimento == 'w'):
                listaKeys.append(Qt.Key_W)
            elif(movimento == 's'):
                listaKeys.append(Qt.Key_S)
            elif(movimento == 'a'):
                listaKeys.append(Qt.Key_A)
            elif(movimento == 'd'):
                listaKeys.append(Qt.Key_D)
        return listaKeys
    
    def getListaMovimentos(self,listaMov):
        listaKeys = self.parseListaMovimentosParaKey(listaMov)
        for movimento in listaKeys:
            QApplication.processEvents()
            time.sleep(0.2)
            self.mover(movimento)
    
    def keyPressEvent(self, event):
        self.mover(event.key())


class Tabuleiro(object):
    
    def __init__(self,tamanho, borda, bordaMenu,bordaRodape, texto = 'Movimentos: '):
        self.tamanho = tamanho
        self.borda = borda
        self.bordaMenu = bordaMenu
        self.listaPecas = []
        self.texto = QString(texto)
        self.qtdMovimentos = 0

    def incrementarQtdMovimentos(self):
        self.qtdMovimentos = self.qtdMovimentos+1
        
    def drawTabuleiro(self,painter):
        painter.setBrush(Qt.gray)
        painter.setPen(Qt.black)
        #Desenhar o quadrado maior:
        painter.drawRect(self.borda,self.borda+self.bordaMenu,self.tamanho,self.tamanho)
        
        #desenhar o numero de movimentos:
        painter.setPen(Qt.black)
        painter.setFont(QFont("Arial",self.tamanho/40))
        
        painter.drawText(self.borda,self.bordaMenu+self.tamanho+self.borda*3.5,self.texto + QString().setNum(self.qtdMovimentos))
    
class Peca(object):
    def __init__(self,numero,posicao,tamanhoTabuleiro, bordaTabuleiro, bordaMenu, corErrado, corCerto):
        self.numero = QString()
        self.numero.setNum(numero)
        self.posicao = posicao
        self.tamanhoTabuleiro = tamanhoTabuleiro
        self.bordaTabuleiro = bordaTabuleiro
        self.bordaMenu = bordaMenu        
        self.imagem = None        
        self.largura = self.tamanhoTabuleiro/3
        self.altura = self.tamanhoTabuleiro/3        
        if(self.posicao / 3 == 0):
            self.xOrigem = self.bordaTabuleiro + self.posicao * self.tamanhoTabuleiro/3
            self.yOrigem = self.bordaTabuleiro            
        if(self.posicao / 3 == 1):
            self.xOrigem = self.bordaTabuleiro + (self.posicao-3) * self.tamanhoTabuleiro/3
            self.yOrigem = self.bordaTabuleiro + self.tamanhoTabuleiro/3
        if(self.posicao / 3 == 2):
            self.xOrigem = self.bordaTabuleiro + (self.posicao-6) * self.tamanhoTabuleiro/3
            self.yOrigem = self.bordaTabuleiro + 2*self.tamanhoTabuleiro/3            
        self.xOrigemTexto = self.xOrigem + self.tamanhoTabuleiro/6 - self.tamanhoTabuleiro/60
        self.yOrigemTexto = self.yOrigem + self.tamanhoTabuleiro/6 + self.tamanhoTabuleiro/60
        
        self.corErrado = corErrado
        self.corCerto = corCerto
        
        if(self.numero.toInt()[0] != self.posicao+1):
            self.cor = self.corErrado            
        else:
            self.cor = self.corCerto     
            

    def getPosicao(self):
        return self.posicao
    def setPosicao(self,novaPosicao):
        self.posicao = novaPosicao
    def getNumero(self):
        return self.numero
    def setNumero(self,novoNumero):
        self.numero.setNum(novoNumero)
    
    def drawPeca(self,painter):
        pass
        #Desenho da peca:
        if self.imagem is None:
            painter.setBrush(self.cor)            
            painter.drawRect(self.xOrigem,self.yOrigem+self.bordaMenu,self.largura,self.altura)
            painter.setFont(QFont("Arial",self.tamanhoTabuleiro/20))
            painter.drawText(self.xOrigemTexto,self.yOrigemTexto+self.bordaMenu,self.numero)
        else:
            painter.setPen(Qt.white)
            painter.drawPixmap(self.xOrigem,self.yOrigem+self.bordaMenu,self.imagem)
            painter.drawPolyline(QPoint(self.xOrigem,self.yOrigem+self.bordaMenu),QPoint(self.xOrigem + self.tamanhoTabuleiro/3,self.yOrigem+self.bordaMenu),QPoint(self.xOrigem + self.tamanhoTabuleiro/3,self.yOrigem + self.tamanhoTabuleiro/3 + self.bordaMenu),QPoint(self.xOrigem,self.yOrigem + self.tamanhoTabuleiro/3 + self.bordaMenu),)

