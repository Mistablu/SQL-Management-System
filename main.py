from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, \
     QVBoxLayout, QComboBox
from PyQt6.QtGui import QAction
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id","Name","Course","Mobile No."))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)


    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM STUDENTS")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialogue = InsertDialogue()
        dialogue.exec()

class InsertDialogue(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        #add studentname widget
        student_name = QLineEdit()
        student_name.setPlaceholderText("Name")
        layout.addWidget(student_name)

        #add combo box widget
        course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        course_name.addItems(courses)
        layout.addWidget(course_name)

        #add mobile number widget
        mobileNo = QLineEdit()
        mobileNo.setPlaceholderText("Mobile No.")
        layout.addWidget(mobileNo)
        
        #add "register" button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)

        self.setLayout(layout)

    def add_student(self):
        pass


app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
age_calculator.load_data()
sys.exit(app.exec())
