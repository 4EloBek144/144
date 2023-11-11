import random
import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QMainWindow
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 382)
        self.pb = QtWidgets.QPushButton(Form)
        self.pb.setGeometry(QtCore.QRect(130, 110, 221, 121))
        self.pb.setObjectName("pb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb.setText(_translate("Form", "Кнопка???"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(random.randrange(0, 256), \
                           random.randrange(0, 256), random.randrange(0, 256)))
        qp.drawEllipse(30, 30, self.ra, self.ra)
        self.ra = random.randrange(30, 500)
        qp.setBrush(QColor(random.randrange(0, 256), \
                           random.randrange(0, 256), random.randrange(0, 256)))
        qp.drawEllipse(200, 300, self.ra, self.ra)
        self.ra = random.randrange(30, 500)
        qp.setBrush(QColor(random.randrange(0, 256), \
                           random.randrange(0, 256), random.randrange(0, 256)))
        qp.drawEllipse(100, 50, self.ra, self.ra)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
