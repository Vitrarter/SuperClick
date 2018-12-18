import sys
from PyQt5 import QtWidgets
from test import Ui_MainWindow
from sketh import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit, QWidget, \
    QVBoxLayout


class Login(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.check)
        self.buttonBox.rejected.connect(self.reject)

    def check(self):
        if str(self.lineEdit.text()) != '':
            self.accept()
            self.username = str(self.lineEdit.text())
        else:
            pass


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.setupUi(self)
        self.button_main.clicked.connect(self.main_click)
        self.count = 0
        self.factor = 1
        self.i = 1
        self.last = 0
        self.all = 0
        self.level = 1
        self.super_mem = 0
        self.max_level = 200
        self.max_level_1 = 50
        self.max_level_2 = 200
        self.max_level_3 = 500
        self.max_level_4 = 3000
        self.max_level_5 = 6000
        self.max_level_6 = 10000
        self.max_level_7 = 40000
        self.max_level_8 = 40000
        self.g_last_1 = 0
        self.g_last_2 = 0
        self.pushButton_1.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_9)
        self.pushButton_9.clicked.connect(self.run_8)
        self.pushButton_10.clicked.connect(self.run_10)
        self.pushButton_11.clicked.connect(self.run_11)
        self.pushButton_12.clicked.connect(self.run_12)
        self.pushButton_13.clicked.connect(self.run_13)
        self.pushButton_14.clicked.connect(self.run_14)
        self.pushButton_15.clicked.connect(self.run_15)
        self.lcd_main_2.display(self.i)
        self.g_1 = 0
        self.g_2 = 0
        self.g_3 = 0
        self.g_4 = 0
        self.g_5 = 0
        self.g_6 = 0
        self.g_8 = 0
        self.trig = 0
        self.trig_2 = 0
        self.trig_3 = 0
        self.trig_4 = 0
        self.trig_5 = 0

    def main_click(self):
        self.count += 1 * self.factor
        self.all += 1 * self.factor
        if (self.all >= (50 * (self.level + 1) * (self.level + 1))) and (self.count >= self.last):
            self.all -= 50 * (self.level + 1) * (self.level + 1)
            self.lcd_main_2.display(self.level + 1)
            self.last = self.count
            self.level += 1
            self.max_level = 50 * (self.level + 1) * (self.level + 1)
            self.progressBar_level.setMaximum(self.max_level)
            if self.super_mem == 1:
                self.count += 10 * self.level * self.level
                self.factor -= 0.1
        if self.count == 30:
            self.lineEdit_2.setText('Начало положено! Продолжайте кликать и улучшайте вашу группу!')
        if self.level == 3 and self.trig == 0 and self.g_1 + self.g_2 >= 4:
            self.factor = self.factor / 1.2
            self.trig += 1
            self.lineEdit_2.setText('Этой Группой становится сложно управлять...')
        if self.level == 6 and self.trig_2 == 0 and self.g_1 >= 5:
            self.factor = self.factor / 1.2
            self.trig_2 += 1
            self.lineEdit_2.setText('Приходится увеличивать зарплаты сотрудникам...')
        if self.level == 10 and self.trig_3 == 0 and self.g_4 + self.g_1 <= 10:
            self.factor = self.factor / 1.2
            self.trig_3 += 1
            self.lineEdit_2.setText('Недостаточно админов...')
        if self.level == 10 and self.trig_3 == 0 and self.g_3 <= 5:
            self.factor = self.factor / 1.1
            self.trig_3 += 1
            self.lineEdit_2.setText('Группа выглядит слишком плохо...')
        if self.level == 3 and self.trig_5 and self.g_1 < 5:
            self.factor -= 1
            self.trig_5 += 1
            self.lineEdit_2.setText('Недостаточно админов...')
        self.i = 1
        self.lcd_main.display(self.count)
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)
        self.progressBar_level.setValue(self.all)

    def setUsername(self, username):
        self.username = username
        self.lineEdit_3.setText(self.username)

    def run(self):
        if self.count >= self.max_level_1 and self.g_1 <= 8:
            self.factor = self.factor * 1.1
            self.count -= self.max_level_1
            self.max_level_1 += 25
            self.lcd_main.display(self.count)
            self.g_1 += 1
            self.progressBar_1.setMaximum(self.max_level_1)
        if self.g_1 > 8:
            self.pushButton_1.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

    def run_2(self):
        if self.count >= self.max_level_2 and self.g_2 <= 8:
            self.factor = self.factor * 1.2
            self.count -= self.max_level_2
            self.lcd_main.display(self.count)
            self.g_2 += 1
            self.max_level_2 += 50
            self.progressBar_2.setMaximum(self.max_level_2)
        if self.g_2 > 8:
            self.pushButton_2.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

    def run_3(self):
        if self.count >= self.max_level_3 and self.g_3 <= 6:
            if self.g_1 <= 4:
                self.lineEdit_2.setText('Администраторы не проследили за работой. Улучшение не удалось.')
            else:
                self.factor = self.factor * 1.2
            self.count -= self.max_level_3
            self.lcd_main.display(self.count)
            self.g_3 += 1
            self.max_level_3 += 100
            self.progressBar_3.setMaximum(self.max_level_3)
        if self.g_3 > 6:
            self.pushButton_3.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

    def run_4(self):
        if self.count >= self.max_level_4 and self.g_4 <= 7:
            self.factor = self.factor * 1.3
            self.count -= self.max_level_4
            self.lcd_main.display(self.count)
            self.g_4 += 1
            self.max_level_4 += 300
            self.progressBar_4.setMaximum(self.max_level_4)
        if self.g_4 > 7:
            self.pushButton_4.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

    def run_5(self):
        if self.count >= self.max_level_5 and self.g_5 <= 4:
            self.factor = self.factor * 1.3
            self.count -= self.max_level_5
            self.lcd_main.display(self.count)
            self.g_5 += 1
            self.max_level_5 += 500
            self.progressBar_5.setMaximum(self.max_level_5)
        if self.g_5 > 4:
            self.pushButton_5.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

    def run_6(self):
        if self.count >= self.max_level_6 and self.g_6 <= 3:
            self.factor = self.factor * 1.4
            self.count -= self.max_level_6
            self.lcd_main.display(self.count)
            self.g_6 += 3
            self.max_level_6 += 3000
            self.progressBar_6.setMaximum(self.max_level_6)
        if self.g_6 > 3:
            self.pushButton_6.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

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
            self.progressBar_8.setValue(self.count)

    def run_8(self):
        if self.count >= self.max_level_8 and self.g_8 <= 2:
            self.factor = self.factor * 1.5
            self.count -= self.max_level_8
            self.lcd_main.display(self.count)
            self.g_8 += 1
            self.max_level_8 += 5000
            self.progressBar_8.setMaximum(self.max_level_2)
        if self.g_8 > 2:
            self.pushButton_9.setText("Продано")
        self.progressBar_1.setValue(self.count)
        self.progressBar_2.setValue(self.count)
        self.progressBar_3.setValue(self.count)
        self.progressBar_4.setValue(self.count)
        self.progressBar_5.setValue(self.count)
        self.progressBar_6.setValue(self.count)
        self.progressBar_7.setValue(self.count)
        self.progressBar_8.setValue(self.count)

    def run_9(self):
        self.lcd_main_3.display(self.factor)

    def run_10(self):
        if self.g_last_1 == 0:
            self.pushButton_11.setText("-")
            self.pushButton_12.setText("-")
            self.count += 300
            self.super_mem += 1
            self.factor -= 0.2
            self.lcd_main.display(self.count)
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)
            self.progressBar_8.setValue(self.count)

    def run_11(self):
        if self.g_last_1 == 0 and self.count >= 100:
            self.pushButton_10.setText("-")
            self.pushButton_12.setText("-")
            self.count -= 100
            self.factor += 0.5
            self.lcd_main.display(self.count)
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)
            self.progressBar_8.setValue(self.count)

    def run_12(self):
        if self.g_last_1 == 0:
            self.pushButton_11.setText("-")
            self.pushButton_10.setText("-")
            self.factor = 0.1
            self.lcd_main.display(self.count)
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)
            self.progressBar_8.setValue(self.count)

    def run_13(self):
        if self.g_last_2 == 0:
            self.pushButton_14.setText("-")
            self.pushButton_15.setText("-")
            self.count += 300
            self.factor = 0.4
            self.lcd_main.display(self.count)
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)
            self.progressBar_8.setValue(self.count)

    def run_14(self):
        if self.g_last_2 == 0 and self.count >= 100:
            self.pushButton_13.setText("-")
            self.pushButton_15.setText("-")
            self.super_mem -= 1
            self.count -= 100
            self.factor = 0.8
            self.lcd_main.display(self.count)
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)
            self.progressBar_8.setValue(self.count)

    def run_15(self):
        if self.g_last_1 == 0:
            self.pushButton_13.setText("-")
            self.pushButton_14.setText("-")
            self.count += 100
            self.factor = 0.6
            self.lcd_main.display(self.count)
            self.progressBar_1.setValue(self.count)
            self.progressBar_2.setValue(self.count)
            self.progressBar_3.setValue(self.count)
            self.progressBar_4.setValue(self.count)
            self.progressBar_5.setValue(self.count)
            self.progressBar_6.setValue(self.count)
            self.progressBar_7.setValue(self.count)
            self.progressBar_8.setValue(self.count)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    if not login.exec_():
        sys.exit(-1)
    main = Example()
    main.setUsername(login.lineEdit.text())
    main.show()
    sys.exit(app.exec_())
