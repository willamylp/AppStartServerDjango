import os, socket, sys, time,subprocess, webbrowser
from os import system as system_call 
from platform import system as system_name
from ssl import SOCK_STREAM
from PyQt5.QtWidgets import QApplication, QFileDialog, QLineEdit, QMainWindow
from Ui_MainWin import Ui_MainWindow
class MainWindow:
    def __init__(self):
        self.url = 'http://wi2l.com.br'
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ipAtual = str(socket.gethostbyname(socket.gethostname()))
        self.ui.serverName.setText(self.ipAtual)
        self.ui.port.setValue(80)
        
        self.ui.btnBuscarApp.clicked.connect(self.searchApp)
        self.ui.btnBuscarVenv.clicked.connect(self.searchVenv)
        self.ui.btnTestar.clicked.connect(self.testServer)
        #self.ui.linkWI2L.clicked.connect(self.openLink(self.url))
        self.ui.startServer.clicked.connect(self.startServer)

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
    
    def testConnectPort(self, host, port):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.settimeout(0.3)
        self.conexao = self.cliente.connect_ex((host, port))
        return self.conexao

    def testConnectServer(self, host):
        return system_call("ping {}".format(host)) == 0

    def testServer(self):
        #START - Test ServerName
        self.ui.labelStatusServer.setText(
            '<b style=" font-size:10pt; color:#000055;">Testando ServerName</b>')
        time.sleep(0.3)
        for i in range(50):
            self.ui.progressTestBar.setValue(i+1)
            time.sleep(0.02)
        
        self.testServerName = self.testConnectServer(self.ui.serverName.text())
        #END - Test ServerName
        '''--------------------------------------'''
        #START - Test Port
        self.ui.labelStatusServer.setText(
            '<b style=" font-size:10pt; color:#000055;">Testando Porta</b>')
        for i in range(50, 100):
            self.ui.progressTestBar.setValue(i+1)
            time.sleep(0.01)
        self.testPort = self.testConnectPort(
            self.ui.serverName.text(), self.ui.port.value())
        #END - Test Port

        self.ui.separador.setText(
            '<center><b style=" font-size:11pt;">|</b></center>')
        
        if(self.testPort != 0):
            self.ui.labelStatusPorta.setText(
                '<center><b style="font-size:10pt; color:#005500;">Porta Ok!</b></center>')
        else:
            self.ui.labelStatusPorta.setText(
                '<center><b style="font-size:10pt; color:#550000;">Porta Indisponível!</b></center>')
        if(self.testServerName):
            self.ui.labelStatusServer.setText(
                '<center><b style="font-size:10pt; color:#005500;">Server Ok!</b></center>')
        else:
            self.ui.labelStatusServer.setText(
                '<center><b style="font-size:10pt; color:#550000;">Server Indisponível!</b></center>')

    def startServer(self):
        self.cmdOpenDirVenvActivate = 'cd {}/Scripts & activate'.format(self.ui.dictVenv.text())
        self.cmdOpenDirApp = 'cd {}'.format(self.ui.dictApp.text())

        self.cmdStartServer = '{} & {} & python manage.py runserver {}:{}'.format(
            self.cmdOpenDirVenvActivate,
            self.cmdOpenDirApp,
            self.ui.serverName.text(),
            self.ui.port.value()
        )
        os.system(self.cmdStartServer)
        time.sleep(2)
        #self.url = '{}:{}'.format(
        #    self.ui.serverName.text(), self.ui.port.value())
        #self.openLink(self.url)

    def openLink(self, url):
        if sys.platform == 'darwin':  # Em caso de ser OS X
            subprocess.Popen(['open', url])
        else:
            webbrowser.open_new_tab(url)

def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
