import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QPushButton, QFileDialog, QColorDialog, QGridLayout, QGraphicsScene
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import QPoint, QRect

class Canvas(QLabel):
    def __init__(self, parent, size):
        super().__init__(parent=parent)

        self.size = size
        self.setPixmap(QPixmap(*size))
        self.setFixedSize(*size)

        self.pencolor = QColor(0,0,0)

        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton('테두리 색상', self)
        self.penbtn.resize(90, 50)
        self.penbtn.move(340, 20)    
        self.penbtn.clicked.connect(self.ColorLine)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton('도형 채우기', self)
        self.brushbtn.resize(90, 50)
        self.brushbtn.move(440, 20)
        self.brushbtn.clicked.connect(self.ColorLine)

        self.brushcolor = QColor(255,255,255)

        self.scene = QGraphicsScene() 
        
        self.begin = QPoint()
        self.end = QPoint()

        # 그림판 초기화
        self.clear_canvas()
        self.initBtn()

    # 그림 그릴 곳을 하얀색으로 칠하기
    def clear_canvas(self):
        painter = QPainter(self.pixmap())
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.drawRect(-100, -100, self.size[0]+100, self.size[1]+100)
        painter.end()
    
    def initBtn(self):
        btnPen = QPushButton('pen', self)   # 버튼 텍스트
        btnPen.resize(50, 50)
        btnPen.move(20, 20)   # 버튼 위치
        btnPen.clicked.connect(self.changeMouseMoveEvent)

        btnSquare = QPushButton('사각형', self)   # 버튼 텍스트
        btnSquare.resize(50, 50)
        btnSquare.move(80, 20)   # 버튼 위치
        btnSquare.clicked.connect(self.changeMouseMoveEvent2)

        btnTriangle = QPushButton('세모', self)   # 버튼 텍스트
        btnTriangle.resize(50, 50)
        btnTriangle.move(140, 20)   # 버튼 위치
        #btnTriangle.clicked.connect()

        btnCircle = QPushButton('원', self)   # 버튼 텍스트
        btnCircle.resize(50, 50)
        btnCircle.move(200, 20)   # 버튼 위치
        #btnCircle.clicked.connect()

        btnFile = QPushButton('불러오기', self)
        btnFile.resize(70, 50)
        btnFile.move(260, 20)
        btnFile.clicked.connect(self.ButtonClickedFile)

    def ColorLine(self):       
        # 색상 대화상자 생성      
        color = QColorDialog.getColor()
 
        sender = self.sender()
 
        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if sender == self.penbtn and color.isValid():           
            self.pencolor = color

        else:
            self.brushcolor = color


    def ButtonClickedSquare(self, e):
        Square = QPainter(self.pixmap())
        Square.setPen(QPen(QColor(self.pencolor)))
        Square.drawRect(QRect(self.begin, self.end))
        Square.end()
        self.repaint()

    def mousePressEvent(self, e):
        self.begin = e.pos()
        #self.end = e.pos()
        self.update()

    def mouseRelaseEvent(self, e):
        #self.begin = e.pos()
        self.end = e.pos()
        self.update()

    def ButtonClickedFile(self):
        fname = QFileDialog.getOpenFileName(self)

    def changeMouseMoveEvent(self):
        self.mouseMoveEvent = self.mouseMoveEventPen

    def changeMouseMoveEvent2(self):
        self.mouseMoveEvent = self.ButtonClickedSquare

    def mouseMoveEvent(self, e):
        pass

    def mouseMoveEventPen(self, e):        
        painter = QPainter(self.pixmap())
        painter.setPen(QPen(QColor(self.pencolor), 2))
        painter.drawPoint(e.x(), e.y())
        painter.end()

        # QLabel을 업데이트 해주는 함수
        self.repaint()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.canvas = Canvas(self, (1280, 720))
        self.setFixedSize(1280, 720)
        
        self.setCentralWidget(self.canvas)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    app.exec_()