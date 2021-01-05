import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QPushButton, QFileDialog, QColorDialog, QGridLayout, QGraphicsScene, QComboBox, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect
from copy import deepcopy

# 그림은 QLabel에 QPixmap을 넣어서 만든다.
# QPixmap은 그냥 그림이라고 생각
class Canvas(QLabel):
    # Canvas 클래스를 생성할때 size를 받아서
    def __init__(self, size):
        super().__init__()

        self.init_UI()
    
    def init_UI(self):
        self.backbtn = QPushButton('디렉터리 선택', self)
        self.backbtn.resize(110, 50)
        self.backbtn.move(20, 630)
        self.backbtn.clicked.connect(self.ButtonClickedFile)

        self.prebtn = QPushButton('<', self)
        self.prebtn.resize(110, 50)
        self.prebtn.move(730, 630)
        #self.prebtn.clicked.connect(self.ImagePage(0))

        self.nextbtn = QPushButton('>', self)
        self.nextbtn.resize(110, 50)
        self.nextbtn.move(850, 630)
        #self.nextbtn.clicked.connect(self.ImagePage(1))

        self.label1 = QLabel('안녕',self)
        self.label1.move(150, 645)

    def ImagePage(self, n):
        if n == 0:
            pass
        elif n == 1:
            pass

    def ButtonClickedFile(self):
        fname = QFileDialog.getOpenFileName(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #가로 1280 세로 720 윈도우 생성
        self.Canvas = Canvas((1000, 720))
        self.setFixedSize(1000, 720)
        
        MainWidget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.Canvas)
        MainWidget.setLayout(layout)
        
        self.setCentralWidget(MainWidget)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    app.exec_()