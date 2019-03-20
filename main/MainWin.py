import os
import sys
import time
import subprocess
import webbrowser
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
        self.ui.btnTestar.clicked.connect(self.testServer)
        self.ui.linkWI2L.clicked.connect(self.openLink)

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
        
    #def testServer(self):
    def testServer(self):
        self.ui.serverName.setText('localhost')
        self.ui.port.setValue(8000)

        self.ui.labelStatus.setText(
            '<b style=" font-size:11pt; font-weight:600; color:#000055;">Testando...</b>')
        for i in range(100):
            self.ui.progressTestBar.setValue(i+1)
            time.sleep(0.02)
        self.ui.labelStatus.setText(
            '<b style="font-size:11pt; font-weight:600; color:#005500;">Disponível para uso!</b>')
    
        def openLink(self):
        url = 'http://wi2l.com.br'
        if sys.platform == 'darwin':  # Em caso de ser OS X
            subprocess.Popen(['open', url])
        else:
            webbrowser.open_new_tab(url)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
