import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit, QProgressBar
from sketh import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow, QProgressBar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_main.clicked.connect(self.main_click)
        self.count = 0
        self.factor = 1
        self.i = 1
        self.last = 0
        self.all = 0
        self.level = 1
        self.max_level = 200
        self.max_level_1 = 50
        self.max_level_2 = 200
        self.max_level_3 = 500
        self.max_level_4 = 3000
        self.max_level_5 = 6000
        self.max_level_6 = 10000
        self.max_level_7 = 40000
        self.pushButton_1.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_8)
        self.lcd_main_2.display(self.i)
        self.g_1 = 0
        self.g_2 = 0
        self.g_3 = 0
        self.g_4 = 0
        self.g_5 = 0
        self.g_6 = 0
        self.trig = 0
        self.trig_2 = 0
        self.trig_3 = 0
        self.trig_4 = 0


    def main_click(self):
        self.count += 1 * self.factor
        self.all += 1 * self.factor
        if (self.all >= (50 * (self.level+1) * (self.level+1))) and (self.count >= self.last):
            self.all -= 50 * (self.level+1) * (self.level+1)
            self.lcd_main_2.display(self.level + 1)
            self.last = self.count
            self.level += 1
            self.max_level = 50 * (self.level+1) * (self.level+1)
            self.progressBar_level.setMaximum(self.max_level)
        if self.count == 30:
            self.lineEdit_2.setText('Начало положено! Продолжайте кликать и улучшайте вашу группу!')
        if self.level == 3 and self.trig == 0 and self.g_1 + self.g_2 >= 4:
            self.factor = self.factor / 1.2
            self.trig +=1
            self.lineEdit_2.setText('Этой Группой становится сложно управлять...')
        if self.level == 6 and self.trig_2 == 0 and self.g_1 >= 5:
            self.factor = self.factor / 1.2
            self.trig_2 +=1
            self.lineEdit_2.setText('Приходится увеличивать зарплаты сотрудникам...')
        if self.level == 10 and self.trig_3 == 0 and self.g_4 + self.g_1 <= 10:
            self.factor = self.factor / 1.2
            self.trig +=1
            self.lineEdit_2.setText('Недостаточно админов...')
        if self.level == 10 and self.trig_3 == 0 and self.g_3 <= 5:
            self.factor = self.factor / 1.1
            self.trig +=1
            self.lineEdit_2.setText('Группа выглядит слишком плохо...')
        self.i = 1
        self.lcd_main.display(self.count)
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_level.setValue(self.all)

    def run(self):
        if self.count >= self.max_level_1 and self.g_1 <= 8:
            self.factor = self.factor * 1.1
            self.count -= self.max_level_1
            self.max_level_1 += 25
            self.lcd_main.display(self.count)
            self.g_1 += 1
            self.progressBar_1.setMaximum(self.max_level_1)
        if self.g_1 > 5:
            self.pushButton_1.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)

    def run_2(self):
        if self.count >= self.max_level_2 and self.g_2 <= 8:
            self.factor = self.factor * 1.2
            self.count -= self.max_level_2
            self.lcd_main.display(self.count)
            self.g_2 += 1
            self.max_level_2 += 50
            self.progressBar_2.setMaximum(self.max_level_3)
        if self.g_2 > 5:
            self.pushButton_2.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)

    def run_3(self):
        if self.count >= self.max_level_3 and self.g_3 <= 6:
            if self.g_1 <= 4:
                self.lineEdit_2.setText('Администраторы не проследили за работой. Улучшение не удалось.')
            else:
                self.factor = self.factor * 1.3
            self.count -= self.max_level_3
            self.lcd_main.display(self.count)
            self.g_3 += 1
            self.max_level_3 += 100
        if self.g_3 > 5:
            self.pushButton_3.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)

    def run_4(self):
        if self.count >= self.max_level_4 and self.g_4 <= 7:
            self.factor = self.factor * 1.4
            self.count -= self.max_level_4
            self.lcd_main.display(self.count)
            self.g_4 += 1
            self.max_level_4 += 300
        if self.g_4 > 5:
            self.pushButton_4.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)

    def run_5(self):
        if self.count >= self.max_level_5 and self.g_5 <= 4:
            self.factor = self.factor * 1.5
            self.count -= self.max_level_5
            self.lcd_main.display(self.count)
            self.g_5 += 1
            self.max_level_5 += 500
        if self.g_5 > 5:
            self.pushButton_5.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)

    def run_6(self):
        if self.count >= self.max_level_6 and self.g_6 <= 2:
            self.factor = self.factor * 1.5
            self.count -= self.max_level_6
            self.lcd_main.display(self.count)
            self.g_6 += 1
            self.max_level_6 += 1000
        if self.g_6 > 5:
            self.pushButton_5.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)

    def run_7(self):
        if self.count >= 40000:
            self.g_1 = 0
            self.g_2 = 0
            self.g_3 = 0
            self.g_4 = 0
            self.g_5 = 0
            self.g_6 = 0
            self.count = 0
            self.factor = 1.3
            self.i = 1
            self.last = 0
            self.all = 0
            self.level = 1
            self.max_level = 600
            self.trig_3 = 0
            self.trig_4 = 0
            self.progressBar_level.setMaximum(self.max_level)
            self.trig = 0
            self.trig_2 = 0
            self.max_level_1 = 50
            self.max_level_2 = 200
            self.max_level_3 = 500
            self.max_level_4 = 3000
            self.max_level_5 = 6000
            self.max_level_6 = 10000
            self.max_level_7 += 20000
            self.lineEdit_2.setText('Добро пожаловать в новую группу! Все результаты обнулены.')
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)

    def run_8(self):
        self.lcd_main_3.display(self.factor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
