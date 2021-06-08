#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import ssl
import re
import mysql.connector as mc
from PyQt5 import QtCore, QtWidgets
from mysql.connector.errors import DatabaseError
from Inventaire import Ui_InventaireWindow

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

class Ui_LoginInvWindow(object):

    def openInventaire(self):
        try:
            file = open("ip_bdd.rtf", "r")
            ligne = file.readlines()
            ligne = str(ligne)
            ligne = ligne.split()
            ligne = ligne[-1]
            Host = ligne.replace("}", '').replace("'", '').replace("]", '')

            inventoriste = '1'
            User = self.User.text()
            Password = self.Password.text()

            connexion = mc.connect(host = Host, database = 'quincaillerie', user = 'User', password = 'Password')
            cursor = connexion.cursor()
            cursor.execute("SELECT COUNT(*) AS NB FROM users WHERE Login = '" +User+ "' AND Password = '" +Password+ "' AND inventoriste = " +inventoriste+ ";")
            count = cursor.fetchone()
            resultat = str(count).replace("(", '').replace(")", '').replace(",", '')
            connexion.close()


            if(resultat == '1'):
                print("passe ici")
                print(User)
                print(Password)
                connexion = mc.connect(host = '172.20.10.6', database = 'quincaillerie', user = 'Inventaire', password = 'Inventaire/789')
                print("toto")
                self.window = QtWidgets.QDialog()
                self.ui = Ui_InventaireWindow()
                self.ui.contenu_interface_balance(self.window)
                self.window.exec()

            #self.window = QtWidgets.QDialog()
            #self.ui = Ui_InventaireWindow()
            #self.ui.contenu_interface_balance(self.window)
            #self.window.exec()


            #self.ui.display_combo_txt()
            #self.ui.onClicked()
            #self.ui.Update_data()
            #self.ui.donne_balance()

        except mc.Error as err:
            QtWidgets.QMessageBox.about(self.label, "Connexion impossible ", str(err))


    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(800, 600)
        LoginWindow.setStyleSheet(_fromUtf8("background-color: rgb(85, 87, 83);"))

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 40, 101, 51))
        self.label.setStyleSheet(_fromUtf8("color: rgb(238, 238, 236);\n" "font-size: 20pt;"))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 81, 51))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(238, 238, 236);\n" "font-size: 20pt;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 320, 181, 51))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(238, 238, 236);\n" "font-size: 20pt;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.User = QtWidgets.QLineEdit(self.centralwidget)
        self.User.setGeometry(QtCore.QRect(340, 170, 421, 61))
        self.User.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 236);\n" "color: rgb(85, 87, 83);\n" "font-size:20pt;"))
        self.User.setObjectName(_fromUtf8("User"))

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setGeometry(QtCore.QRect(340, 310, 421, 61))
        self.Password.setStyleSheet(_fromUtf8("color: rgb(85, 87, 83);\n" "background-color: rgb(238, 238, 236);\n" "font-size:20pt;"))
        self.Password.setObjectName(_fromUtf8("Password")) 

        self.buttonConnexion = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConnexion.setGeometry(QtCore.QRect(590, 440, 171, 51))
        self.buttonConnexion.setStyleSheet(_fromUtf8("font-size: 20pt;\n" "color: rgb(85, 87, 83);\n" "background-color: rgb(238, 238, 236);"))
        self.buttonConnexion.setObjectName(_fromUtf8("buttonConnexion"))
        self.buttonConnexion.clicked.connect(self.openInventaire)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow", None))
        self.buttonConnexion.setText(_translate("LoginWindow", "Connexion", None))
        self.label.setText(_translate("LoginWindow", "LOGIN", None))
        self.label_2.setText(_translate("LoginWindow", "USER", None))
        self.label_3.setText(_translate("LoginWindow", "PASSWORD", None))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QDialog()
    ui = Ui_LoginInvWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())