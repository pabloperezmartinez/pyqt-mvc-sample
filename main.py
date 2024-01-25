import sys
from PyQt5.QtWidgets import QApplication
from controllers.main_window import MainWindow

app = QApplication(sys.argv)
gestor = MainWindow()
gestor.show()
sys.exit(app.exec_())