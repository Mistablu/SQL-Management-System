from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        #creates widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Date of Birth DD/MM/YYYY:")
        self.date_birth_label_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        #adds widgets to a grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        birth_date = self.date_birth_label_edit.text()
        birth_year = datetime.strptime(birth_date, "%d/%m/%Y").date().year

        age = current_year - birth_year
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
