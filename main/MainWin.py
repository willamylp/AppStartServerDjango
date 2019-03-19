import os
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QLineEdit
from Ui_MainWin import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.appDir = ''
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.btnBuscarApp.clicked.connect(self.searchApp)
        self.ui.btnBuscarVenv.clicked.connect(self.searchVenv)

    def show(self):
        self.main_win.show()

    def searchApp(self):
        self.appDir = str(QFileDialog.getExistingDirectory(
            None, 'Selecionar Pasta da Aplicação', os.getenv('HOME')))
        self.ui.dictApp.setText(self.appDir)

    def searchVenv(self):
        self.venvDir = str(QFileDialog.getExistingDirectory(
            None, 'Selecionar Pasta da Virtualenv', os.getenv('HOME')))
        self.ui.dictVenv.setText(self.venvDir)
        


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
