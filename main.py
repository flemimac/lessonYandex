import sys
import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Main")
        
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []
        
    def add_circle(self):
        diameter = random.randint(20, 150)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter) in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()

    sys.exit(app.exec())