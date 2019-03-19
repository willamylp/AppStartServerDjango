import os, sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog

from Ui_MainWin import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.appDir = self.ui.btnBuscarApp.clicked.connect(self.searchApp)
        self.venvDir = self.ui.btnBuscarVenv.clicked.connect(self.searchVenv)

    def show(self):
        self.main_win.show()

    def searchApp(self):
        self.appDir = str(QFileDialog.getExistingDirectory(
            None, 'Selecionar Pasta da Aplicação', os.getenv('HOME')))
        return self.appDir

    def searchVenv(self):
        self.venvDir = str(QFileDialog.getExistingDirectory(
            None, 'Selecionar Pasta da Virtualenv', os.getenv('HOME')))
        return self.venvDir

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

