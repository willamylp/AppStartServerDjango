import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog

from Ui_MainWin import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.btnBuscarApp.clicked.connect(self.btnSearchApp)
        self.ui.btnBuscarVenv.clicked.connect(self.btnSearchVenv)

    def show(self):
        self.main_win.show()

    def btnSearchApp(self):
        self.dir_name = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))

        if self.dir_name:
            self.btn_file.setText(self.dir_name)
        #file = QFileDialog.getExistingDirectory(self, "Selecionar Diretório")

    def btnSearchVenv(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

