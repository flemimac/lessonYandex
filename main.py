import sys
import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)

        self.circle_drawer = CircleDrawer()
        self.setCentralWidget(self.circle_drawer)

        self.pushButton = QPushButton("нажми на меня", self)
        self.pushButton.setGeometry(360, 370, 100, 30)
        self.pushButton.clicked.connect(self.circle_drawer.add_circle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()

    sys.exit(app.exec())