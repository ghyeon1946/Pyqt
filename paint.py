import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QPushButton, QFileDialog, QColorDialog, QGridLayout, QGraphicsScene, QComboBox, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect
from copy import deepcopy

class Canvas(QLabel):
    def __init__(self, parent, size):
        super().__init__(parent=parent)

        self.count = 10

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

        self.backgroundcolor = QColor(255, 255, 255)
        self.backbtn = QPushButton('배경색', self)
        self.backbtn.resize(60, 50)
        self.backbtn.move(790, 20)
        self.backbtn.clicked.connect(self.ColorLine)

        self.scene = QGraphicsScene() 
        
        self.begin = QPoint()
        self.end = QPoint()

        self.label1 = QLabel(self)
        self.label1.move(60, 60)

        # 그림판 초기화
        self.clear_canvas()
        self.initBtn()

    # 그림 그릴 곳을 하얀색으로 칠하기
    def clear_canvas(self):
        painter = QPainter(self.pixmap())
        painter.setBrush(QColor(self.backgroundcolor))
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
        btnTriangle.clicked.connect(self.changeMouseMoveEvent6)

        btnCircle = QPushButton('원', self)   # 버튼 텍스트
        btnCircle.resize(50, 50)
        btnCircle.move(200, 20)   # 버튼 위치
        btnCircle.clicked.connect(self.changeMouseMoveEvent3)

        btnFile = QPushButton('불러오기', self)
        btnFile.resize(70, 50)
        btnFile.move(260, 20)
        btnFile.clicked.connect(self.ButtonClickedFile)

        btnLine = QPushButton('직선', self)
        btnLine.resize(50, 50)
        btnLine.move(540, 20)
        btnLine.clicked.connect(self.changeMouseMoveEvent4)

        self.Erasercolor = QColor(255, 255, 255)
        btnErase = QPushButton('지우개', self)
        btnErase.resize(50, 50)
        btnErase.move(600, 20)
        btnErase.clicked.connect(self.changeMouseMoveEvent5)

        self.label = QLabel('선 두께', self)
        self.label.resize(50, 50)
        self.label.move(660, 20)

        self.cb = QComboBox(self)
        self.cb.addItem('1')
        self.cb.addItem('2')
        self.cb.addItem('3')
        self.cb.addItem('4')
        self.cb.addItem('5')
        self.cb.addItem('6')
        self.cb.addItem('7')
        self.cb.addItem('8')
        self.cb.addItem('9')
        self.cb.addItem('10')
        self.cb.move(720, 35)

        btnSave = QPushButton('저장', self)
        btnSave.resize(50, 50)
        btnSave.move(860, 20)
        btnSave.clicked.connect(self.ButtonClickedsave)

        btnBrush2 = QPushButton('도형 비우기', self)
        btnBrush2.resize(90, 50)
        btnBrush2.move(920, 20)
        btnBrush2.clicked.connect(self.ButtonClickedBrush)

    def ButtonClickedBrush(self):
        self.brushcolor = self.backgroundcolor

    def ButtonClickedErase(self, e):
        self.pencolor = self.Erasercolor
        painter = QPainter(self.pixmap())
        painter.setPen(QPen(QColor(self.Erasercolor), 15))
        painter.drawLine(self.begin, e.pos())
        self.begin = e.pos()
        painter.end()

        # QLabel을 업데이트 해주는 함수
        self.repaint()

    def ColorLine(self):       
        # 색상 대화상자 생성      
        color = QColorDialog.getColor()
        sender = self.sender()
 
        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if sender == self.penbtn and color.isValid():           
            self.pencolor = color

        elif sender == self.brushbtn:
            self.brushcolor = color

        elif sender == self.backbtn:
            t_pixmap = self.pixmap()
            t_pixmap = t_pixmap.copy(0, 0, t_pixmap.width(), t_pixmap.height())
            t_pixmap.fill(color)
            self.backgroundcolor = color
            self.Erasercolor = color
            self.setPixmap(t_pixmap)

    def ButtonClickedCircle(self, e):
        self.count = 1
        t_pixmap = self.pixmap()
        t_pixmap = t_pixmap.copy(0, 0, t_pixmap.width(), t_pixmap.height())
        Circle = QPainter(self.pixmap())
        Circle.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
        Circle.setBrush(QColor(self.brushcolor))
        Circle.drawEllipse(QRect(self.begin, e.pos()))
        Circle.end()
        self.repaint()
        self.setPixmap(t_pixmap)

    def ButtonClickedSquare(self, e):
        self.count = 0
        t_pixmap = self.pixmap()
        t_pixmap = t_pixmap.copy(0, 0, t_pixmap.width(), t_pixmap.height())
        Square = QPainter(self.pixmap())
        Square.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
        Square.setBrush(QColor(self.brushcolor))
        Square.drawRect(QRect(self.begin, e.pos()))
        Square.end()
        self.repaint()
        self.setPixmap(t_pixmap)

    def ButtonClickedTriangle(self, e):
        t_pixmap = self.pixmap()
        t_pixmap = t_pixmap.copy(0, 0, t_pixmap.width(), t_pixmap.height())
        Triangle = QPainter(self.pixmap())
        Triangle.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
        Triangle.setBrush(QColor(self.brushcolor))

        points = QPolygon([
            QPoint(10,10),
            QPoint(10,100),
            QPoint(100,10)
        ])
 
        Triangle.drawPolygon(points)

    def ButtonClickedLine(self, e):
        self.count = 2
        t_pixmap = self.pixmap()
        t_pixmap = t_pixmap.copy(0, 0, t_pixmap.width(), t_pixmap.height())
        Square = QPainter(self.pixmap())
        Square.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
        Square.setBrush(QColor(self.brushcolor))
        Square.drawLine(self.begin, e.pos())
        Square.end()
        self.repaint()
        self.setPixmap(t_pixmap)

    def mousePressEvent(self, e):
        self.begin = e.pos()
        self.update()

    def mouseReleaseEvent(self, e):
        if self.count == 0:
            Square = QPainter(self.pixmap())
            Square.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
            Square.setBrush(QColor(self.brushcolor))
            Square.drawRect(QRect(self.begin, e.pos()))
            Square.end()
            self.repaint()
        
        elif self.count == 1:
            Square = QPainter(self.pixmap())
            Square.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
            Square.setBrush(QColor(self.brushcolor))
            Square.drawEllipse(QRect(self.begin, e.pos()))
            Square.end()
            self.repaint()

        elif self.count == 2:
            Square = QPainter(self.pixmap())
            Square.setPen(QPen(QColor(self.pencolor),self.cb.currentIndex()))
            Square.setBrush(QColor(self.brushcolor))
            Square.drawLine(self.begin, e.pos())
            Square.end()
            self.repaint()


    def ButtonClickedFile(self):
        fname = QFileDialog.getOpenFileName(self)

        if fname[0]:
            # QPixmap 객체
            pixmap = QPixmap(fname[0])

            self.label1.setPixmap(pixmap)  # 이미지 세팅
            self.label1.resize(pixmap.width(), pixmap.height())

            # 이미지의 크기에 맞게 Resize
            self.resize(pixmap.width(), pixmap.height())

            self.show()
        
    def ButtonClickedsave(self):
        buttonReply = QMessageBox.question(self, '저장', "저장하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if buttonReply == QMessageBox.Yes:
            self.pixmap().save("save.jpg")
        else:
            pass

    def changeMouseMoveEvent(self):
        self.mouseMoveEvent = self.mouseMoveEventPen

    def changeMouseMoveEvent2(self):
        self.mouseMoveEvent = self.ButtonClickedSquare

    def changeMouseMoveEvent3(self):
        self.mouseMoveEvent = self.ButtonClickedCircle

    def changeMouseMoveEvent4(self):
        self.mouseMoveEvent = self.ButtonClickedLine

    def changeMouseMoveEvent5(self):
        self.mouseMoveEvent = self.ButtonClickedErase

    def changeMouseMoveEvent6(self):
        self.mouseMoveEvent = self.ButtonClickedTriangle

    def mouseMoveEvent(self, e):
        pass

    def mouseMoveEventPen(self, e):        
        painter = QPainter(self.pixmap())
        painter.setPen(QPen(QColor(self.pencolor), self.cb.currentIndex()))
        painter.drawLine(self.begin, e.pos())
        self.begin = e.pos()
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