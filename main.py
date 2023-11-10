import random
import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog
from PyQt5 import uic


class RandomO(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pb.clicked.connect(self.push)

    def push(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def draw(self, qp):
        self.ra = random.randrange(30, 500)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(30, 30, self.ra, self.ra)
        self.ra = random.randrange(30, 500)
        qp.drawEllipse(200, 300, self.ra, self.ra)
        self.ra = random.randrange(30, 500)
        qp.drawEllipse(100, 50, self.ra, self.ra)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomO()
    ex.show()
    sys.exit(app.exec())
