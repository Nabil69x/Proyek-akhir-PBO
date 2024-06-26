import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator_ui import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        # Connect buttons to their respective methods
        self.ui.pushButton.clicked.connect(lambda: self.append_number("7"))
        self.ui.pushButton_2.clicked.connect(lambda: self.append_number("8"))
        self.ui.pushButton_3.clicked.connect(lambda: self.append_number("9"))
        self.ui.pushButton_4.clicked.connect(lambda: self.operation("/"))
        self.ui.pushButton_5.clicked.connect(lambda: self.append_number("4"))
        self.ui.pushButton_7.clicked.connect(lambda: self.append_number("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.append_number("6"))
        self.ui.pushButton_8.clicked.connect(lambda: self.operation("*"))
        self.ui.pushButton_9.clicked.connect(lambda: self.append_number("1"))
        self.ui.pushButton_11.clicked.connect(lambda: self.append_number("2"))
        self.ui.pushButton_10.clicked.connect(lambda: self.append_number("3"))
        self.ui.pushButton_12.clicked.connect(lambda: self.operation("-"))
        self.ui.pushButton_13.clicked.connect(lambda: self.append_number("0"))
        self.ui.pushButton_14.clicked.connect(self.calculate_result)
        self.ui.pushButton_15.clicked.connect(self.clear_display)
        self.ui.pushButton_16.clicked.connect(lambda: self.operation("+"))

        self.current_operation = None
        self.first_number = None

    def append_number(self, number):
        print(f"Button {number} pressed")  # Debugging line
        current_text = self.ui.lineEdit.text()
        new_text = current_text + number
        self.ui.lineEdit.setText(new_text)

    def operation(self, op):
        self.first_number = float(self.ui.lineEdit.text())
        self.current_operation = op
        self.ui.lineEdit.clear()

    def calculate_result(self):
        second_number = float(self.ui.lineEdit.text())
        if self.current_operation == "+":
            result = self.first_number + second_number
        elif self.current_operation == "-":
            result = self.first_number - second_number
        elif self.current_operation == "*":
            result = self.first_number * second_number
        elif self.current_operation == "/":
            result = self.first_number / second_number
        self.ui.lineEdit.setText(str(result))

    def clear_display(self):
        self.ui.lineEdit.clear()
        self.current_operation = None
        self.first_number = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
