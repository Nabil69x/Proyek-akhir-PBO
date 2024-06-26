import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, 
                             QPushButton, QLabel, QLineEdit)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')

        # Create the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)

        # Create the buttons
        self.buttons = {}
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]
        for i, text in enumerate(buttons):
            button = QPushButton(text)
            button.clicked.connect(lambda checked, text=text: self.button_clicked(text))
            self.buttons[text] = button

        # Create the grid layout
        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)
        for i in range(1, 5):
            for j in range(4):
                grid.addWidget(self.buttons[buttons[(i-1)*4+j]], i, j)

        # Set the layout
        self.setLayout(grid)

    def button_clicked(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception as e:
                self.display.setText('Error')
        elif text == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())