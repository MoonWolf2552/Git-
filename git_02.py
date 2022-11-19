import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('desing.ui', self)
        self.coords_ = (0, 0)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_(qp)
        qp.end()

    def draw_(self, qp):
        if self.do_paint:
            self.coords_ = randint(0, 560), randint(0, 380)
            qp.setBrush(QColor(255, 255, 0))
            r = randint(30, 200)
            x, y = self.coords_
            qp.drawEllipse(int(x - r / 2), int(y - r / 2), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
