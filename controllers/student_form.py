import typing
import pathlib
from PyQt5.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from PyQt5 import QtCore, uic
from PyQt5.QtCore import pyqtSignal
from models.student_db import StudentDb


class StudentForm(QWidget):
    student_saved = pyqtSignal()    
    def __init__(self) -> None:
        super().__init__()
        self.__student_db = StudentDb()
        self.student_id = None 
        mod_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / "views/student_form.ui",self)
        self.saveButton.clicked.connect(lambda: self.save_student())
        self.cancelButton.clicked.connect(lambda: self.close())
        
    def save_student(self):
        if self.student_id:
            self.__student_db.update_student(
                self.student_id,
                self.firstNameTextField.text(),
                self.lastNameTextField.text(),
                self.emailTextField.text()
            )
        else:    
            self.__student_db.create_student(
                self.firstNameTextField.text(),
                self.lastNameTextField.text(),
                self.emailTextField.text()
            )
        self.student_saved.emit()
        self.close()
    
    def load_student_data(self, student_id):
        self.student_id = student_id
        student_data = self.__student_db.get_student_by_id(student_id)
        if student_data:
            self.firstNameTextField.setText(student_data[1])
            self.lastNameTextField.setText(student_data[2])
            self.emailTextField.setText(student_data[3])
            
    def reset_form(self):
        self.firstNameTextField.setText("")
        self.lastNameTextField.setText("")
        self.emailTextField.setText("")
        self.student_id = None 