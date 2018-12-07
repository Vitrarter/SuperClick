import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from designe import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_main.clicked.connect(self.main_click)
        self.count = 0

    def main_click(self):
        self.count += 1
        self.lcd_main.display(self.count)


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
