import typing
import pathlib
from PyQt5.QtWidgets import QMainWindow,  QTableWidgetItem, QMessageBox, QPushButton
from PyQt5 import QtCore, uic
from controllers.student_form import StudentForm

from models.student_model import StudentModel
from models.db_conector import DatabaseConnection

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        mod_path = pathlib.Path(__file__).parent.parent
        uic.loadUi(mod_path / "views/main_window.ui",self)
        self._studentForm = StudentForm()
        self.__student_db = StudentModel()
        self.load_students()
        
        
        self.newStudentAction.triggered.connect(lambda: self.create_student())
        self._studentForm.student_saved.connect(self.load_students)
        
    
    def load_students(self):
        students_list = self.__student_db.get_students()
        self.studentsTable.setRowCount(len(students_list))
        for i, student in enumerate(students_list):
            id, first_name, last_name, email = student
            self.studentsTable.setItem(i, 0, QTableWidgetItem(str(id)))
            self.studentsTable.setItem(i, 1, QTableWidgetItem(first_name))
            self.studentsTable.setItem(i, 2, QTableWidgetItem(last_name))
            self.studentsTable.setItem(i, 3, QTableWidgetItem(email))
            self.studentsTable.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.studentsTable.item(i, 1).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.studentsTable.item(i, 2).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.studentsTable.item(i, 3).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

            # Botón de Edición
            edit_button = QPushButton("Editar")
            edit_button.clicked.connect(self.edit_student)
            edit_button.setProperty("row", i)
            self.studentsTable.setCellWidget(i, 4, edit_button)
            
            # Botón de Eliminación
            delete_button = QPushButton("Eliminar")
            delete_button.clicked.connect(self.delete_student)
            delete_button.setProperty("row", i)
            self.studentsTable.setCellWidget(i, 5, delete_button)
           
    def edit_student(self):
        sender = self.sender()
        row = sender.property("row")
        student_id = self.studentsTable.item(row, 0).text()
        self._studentForm.load_student_data(student_id)
        self._studentForm.show()
    
    def create_student(self):
        self._studentForm.reset_form()
        self._studentForm.show()
    
    def delete_student(self):
        sender = self.sender()
        row = sender.property("row")
        
        msg = f"¿Está seguro que desea borrar el estudiante {self.studentsTable.item(row, 1).text()}"\
              f"{self.studentsTable.item(row, 2).text()}?"
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(msg)
        msgBox.setWindowTitle("Eliminar estudiante")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            student_id = self.studentsTable.item(row,0).text()
            print(student_id)
            self.__student_db.delete_student(str(student_id))
            self.load_students()
            msgBox2 = QMessageBox()
            msgBox2.setIcon(QMessageBox.Information)
            msgBox2.setText("La operación se ha realizado con éxito")
            msgBox2.setWindowTitle("Eliminar estudiante")
            msgBox2.exec_()
            
                
    
    def closeEvent(self, ev):
        db = DatabaseConnection()
        db.close()
        return super().closeEvent(ev)