# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 110, 401, 51))
        self.groupBox.setObjectName("groupBox")
        self.dictApp = QtWidgets.QLineEdit(self.groupBox)
        self.dictApp.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.dictApp.setObjectName("dictApp")
        self.btnBuscarApp = QtWidgets.QPushButton(self.groupBox)
        self.btnBuscarApp.setGeometry(QtCore.QRect(320, 20, 71, 21))
        self.btnBuscarApp.setObjectName("btnBuscarApp")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 230, 401, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnTestar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnTestar.setGeometry(QtCore.QRect(320, 49, 71, 21))
        self.btnTestar.setObjectName("btnTestar")
        self.serverName = QtWidgets.QLineEdit(self.groupBox_2)
        self.serverName.setGeometry(QtCore.QRect(10, 49, 211, 21))
        self.serverName.setObjectName("serverName")
        self.labelServerName = QtWidgets.QLabel(self.groupBox_2)
        self.labelServerName.setGeometry(QtCore.QRect(10, 29, 211, 21))
        self.labelServerName.setObjectName("labelServerName")
        self.port = QtWidgets.QSpinBox(self.groupBox_2)
        self.port.setGeometry(QtCore.QRect(230, 49, 81, 21))
        self.port.setObjectName("port")
        self.labelPorta = QtWidgets.QLabel(self.groupBox_2)
        self.labelPorta.setGeometry(QtCore.QRect(230, 30, 101, 21))
        self.labelPorta.setObjectName("labelPorta")
        self.progressTestBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressTestBar.setGeometry(QtCore.QRect(10, 90, 381, 21))
        self.progressTestBar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.progressTestBar.setProperty("value", 0)
        self.progressTestBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressTestBar.setInvertedAppearance(False)
        self.progressTestBar.setObjectName("progressTestBar")
        self.status = QtWidgets.QLabel(self.groupBox_2)
        self.status.setGeometry(QtCore.QRect(10, 115, 71, 31))
        self.status.setObjectName("status")
        self.labelOk = QtWidgets.QLabel(self.groupBox_2)
        self.labelOk.setGeometry(QtCore.QRect(70, 120, 321, 21))
        self.labelOk.setObjectName("labelOk")
        self.labelErro = QtWidgets.QLabel(self.groupBox_2)
        self.labelErro.setGeometry(QtCore.QRect(70, 120, 321, 21))
        self.labelErro.setObjectName("labelErro")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 10, 401, 91))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 440, 401, 31))
        self.label.setObjectName("label")
        self.endServer = QtWidgets.QPushButton(self.centralwidget)
        self.endServer.setGeometry(QtCore.QRect(340, 400, 81, 23))
        self.endServer.setObjectName("endServer")
        self.startServer = QtWidgets.QPushButton(self.centralwidget)
        self.startServer.setGeometry(QtCore.QRect(252, 400, 82, 23))
        self.startServer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.startServer.setObjectName("startServer")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 170, 401, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.dictVenv = QtWidgets.QLineEdit(self.groupBox_3)
        self.dictVenv.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.dictVenv.setObjectName("dictVenv")
        self.btnBuscarVenv = QtWidgets.QPushButton(self.groupBox_3)
        self.btnBuscarVenv.setGeometry(QtCore.QRect(320, 20, 71, 21))
        self.btnBuscarVenv.setObjectName("btnBuscarVenv")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Start Server Django"))
        self.groupBox.setTitle(_translate("MainWindow", "DIRETÓRIO DA APLICAÇÃO"))
        self.btnBuscarApp.setText(_translate("MainWindow", "BUSCAR..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "INFORMAÇÕES DO SERVIDOR"))
        self.btnTestar.setText(_translate("MainWindow", "TESTAR"))
        self.labelServerName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">NOME DO SERVIDOR</span></p></body></html>"))
        self.labelPorta.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">PORTA</span></p></body></html>"))
        self.status.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Status:</span></p></body></html>"))
        self.labelOk.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#005500;\"></span></p></body></html>"))
        self.labelErro.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#aa0000;\"></span></p></body></html>"))
        self.logo.setText(_translate("MainWindow", "<html><head/><body>\n"
"<div align=\"center\"><img src=\"../images/Logo_StartServerDjango.png\"/></div>\n"
"</body></html>"))
        self.label.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<style>\n"
"a.link {\n"
"text-decoration: none;\n"
"transition: 0.3s\n"
"}\n"
"a.link:hover {\n"
"text-decoration: none;\n"
"font-weight: bold;\n"
"transition: 0.3s\n"
"}\n"
"</style>\n"
"<p>\n"
"<span style=\" font-size:10pt; font-weight:600;\">Desenvolvido por: </span>\n"
"<span style=\" font-size:10pt;\">\n"
"<a class=\"link\" href=\"wi2l.com.br\" target=\"_blank\">Willamy Domingos - WI2L</a>\n"
"</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.endServer.setText(_translate("MainWindow", "PARAR"))
        self.startServer.setText(_translate("MainWindow", "INICIAR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "DIRETÓRIO DA VirtualEnv (venv)"))
        self.btnBuscarVenv.setText(_translate("MainWindow", "BUSCAR..."))

