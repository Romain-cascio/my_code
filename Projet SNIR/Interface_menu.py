#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from Login_Inventaire import Ui_LoginInvWindow
from Login_Preparation import Ui_LoginPrepWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MenuWindow(object):
    
    def openLoginInventaire(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_LoginInvWindow()
        self.ui.setupUi(self.window)
        self.window.exec()

    def openLoginPreparation(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_LoginPrepWindow()
        self.ui.setupUi(self.window)
        self.window.exec()
        
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName(_fromUtf8("MenuWindow"))
        MenuWindow.resize(800, 600)
        MenuWindow.setStyleSheet(_fromUtf8("background-color: rgb(85, 87, 83);"))

        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 120, 321, 431))
        self.pushButton.setStyleSheet(_fromUtf8("font-size:20pt;\n" "color: rgb(238, 238, 236);\n" "background-color: rgb(0,0,255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.openLoginInventaire)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 120, 321, 431))
        self.pushButton_2.setStyleSheet(_fromUtf8("font-size:20pt;\n" "color: rgb(238, 238, 236);\n" "background-color: rgb(255, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.openLoginPreparation)
        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 671, 41))
        self.label.setStyleSheet(_fromUtf8("font-size:20pt;\n" "color: rgb(238, 238, 236);"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(_translate("MenuWindow", "MenuWindow", None))
        self.pushButton.setText(_translate("MenuWindow", "INVENTAIRE", None))
        self.pushButton_2.setText(_translate("MenuWindow", "PREPARATION", None))
        self.label.setText(_translate("MenuWindow", "Bienvenue, choisissez une application :", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QDialog()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())