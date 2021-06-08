#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import string
import mysql.connector as mc
from PyQt5 import QtCore, QtWidgets
from source_balance import recup_port_USB
from source_lst_data import listing_données
from source_update_data import Update_to_base
from source_scan import recup_scan_usb

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

class Ui_InventaireWindow(object):
    # def __init__(self):
    #     super().__init__()
    #     #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    #     self.contenu_interface_balance(self)
    #     self.show()

    def contenu_interface_balance(self, inventairewindow):
        inventairewindow.setObjectName(_fromUtf8("MainWindow"))
        inventairewindow.resize(800, 600)

        self.verticalLayoutWidget = QtWidgets.QWidget(inventairewindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 560))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))

        self.Layout_Label = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Layout_Label.setObjectName(_fromUtf8("Layout_Label"))

        self.verticalLayoutWidget2 = QtWidgets.QWidget(inventairewindow)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(170, 20, 160, 560))
        self.verticalLayoutWidget2.setObjectName(_fromUtf8("verticalLayoutWidget2"))

        self.Layout_Label2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.Layout_Label2.setObjectName(_fromUtf8("Layout_Label"))

        self.horizontalLayoutWidget_but = QtWidgets.QWidget(inventairewindow)
        #self.horizontalLayoutWidget_but.setGeometry(QtCore.QRect(500, 500, 250, 35))
        self.horizontalLayoutWidget_but.setObjectName("horizontalLayoutWidget_but")

        self.horizontalLayoutWidget_lst = QtWidgets.QWidget(inventairewindow)
        #self.horizontalLayoutWidget_lst.setGeometry(QtCore.QRect(350, 80, 250, 40))
        self.horizontalLayoutWidget_lst.setObjectName("horizontalLayoutWidget_lst")

        self.Layout_Label2.setSpacing(48)

#################boutons balance et Update données##################################

        self.BalanceBut = QtWidgets.QPushButton(self.horizontalLayoutWidget_but)
        self.BalanceBut.setGeometry(QtCore.QRect(500, 500, 113, 32))
        self.BalanceBut.setObjectName("BalanceBut")
        self.BalanceBut.setText("Balance")
        self.BalanceBut.clicked.connect(self.donne_balance)

        self.UpdateDataBut = QtWidgets.QPushButton(self.horizontalLayoutWidget_but)
        self.UpdateDataBut.setGeometry(QtCore.QRect(650, 500, 113, 32))
        self.UpdateDataBut.setObjectName("UpdateDataBut")
        self.UpdateDataBut.setText("Update")
        self.UpdateDataBut.clicked.connect(self.Update_data)

        self.ScanBut = QtWidgets.QPushButton(self.horizontalLayoutWidget_but)
        self.ScanBut.setGeometry(QtCore.QRect(350, 500, 113, 32))
        self.ScanBut.setObjectName("ScanBut")
        self.ScanBut.setText("Scan")
        self.ScanBut.clicked.connect(self.donne_scan)


#################boutons balance et Update données##################################



        self.label_X_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_X_name.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_name)
        self.label_X_name.setText("NOM : ")

        self.label_X_Quantité = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_X_Quantité.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_Quantité)
        self.label_X_Quantité.setText("QUANTITÉ : ")

        self.label_X_prix = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_X_prix.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_prix)
        self.label_X_prix.setText("PRIX : ")

        self.label_X_poids = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_X_poids.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_poids)
        self.label_X_poids.setText("POIDS : ")

        self.Valeur1 = QtWidgets.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur1.setObjectName(_fromUtf8("Valeur1"))
        self.Layout_Label2.addWidget(self.Valeur1)

        self.Valeur2 = QtWidgets.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur2.setObjectName(_fromUtf8("Valeur2"))
        self.Layout_Label2.addWidget(self.Valeur2)

        self.Valeur3 = QtWidgets.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur3.setObjectName(_fromUtf8("Valeur3"))
        self.Layout_Label2.addWidget(self.Valeur3)

        self.Valeur4 = QtWidgets.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur4.setObjectName(_fromUtf8("Valeur4"))
        self.Layout_Label2.addWidget(self.Valeur4)

        #################PARTIE LISTE DEROULANTE########################################################
        
        self.combo1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_lst)
        self.combo1.setGeometry(QtCore.QRect(350, 79, 200, 30))
        lst_nom_piece, lst_quantité_piece, lst_prix_piece, lst_poids_piece = listing_données()

        for ligne in lst_nom_piece:
            self.combo1.addItem(str(ligne))

        #################PARTIE LISTE DEROULANTE########################################################
        self.Checkstatu = QtWidgets.QCheckBox(self.horizontalLayoutWidget_lst)
        self.Checkstatu.setGeometry(QtCore.QRect(600, 79, 30, 30))
        self.Checkstatu.setChecked(False)
        self.combo1.setEnabled(False)
        #self.onClicked()
        self.Checkstatu.toggled.connect(self.onClicked)

        self.labelcheck = QtWidgets.QLabel(self.horizontalLayoutWidget_lst)
        self.labelcheck.setGeometry(QtCore.QRect(635, 79, 150, 30))
        self.labelcheck.setText("Activer / Désactiver")

        self.combo1.currentIndexChanged.connect(self.display_combo_txt)
       
#################fonction récupération et affichage de la base de donnée##################################
    def display_combo_txt(self):
        ######global ici##############
        global n
        n = 0
        y = 0

        lst_nom_piece, lst_quantité_piece, lst_prix_piece, lst_poids_piece = listing_données()
        
        txt_selected = self.combo1.currentText()
        self.Valeur1.setText(txt_selected)

        while (y < len(lst_nom_piece)):
            if(txt_selected == lst_nom_piece[y]):
                n = y
            y = y + 1
        
        self.Valeur2.setText(lst_quantité_piece[n])
        self.Valeur3.setText(lst_prix_piece[n])
        self.Valeur4.setText(lst_poids_piece[n])
#################fonction récupération et affichage de la base de donnée##################################


    def onClicked(self):
        print("passe ici")
        if(self.Checkstatu.isChecked()):
            print("OUI")
            self.display_combo_txt()
            self.combo1.setEnabled(True)
        else:
            print("NON")
            self.combo1.setEnabled(False)

    def Update_data(self):
        #########global ici##############
        global n

        UpdateName = self.Valeur1.text()
        UpdateQuantite = self.Valeur2.text()
        UpdatePrix = self.Valeur3.text()
        UpdatePoids = self.Valeur4.text()

        #Update_to_base(UpdateName, UpdateQuantite, UpdatePrix, UpdatePoids, n)
    
        return UpdateName

    def donne_balance(self):
        poids_balance = recup_port_USB()
        self.Valeur2.setText(str(poids_balance))

    def donne_scan(self):
        code_produit = recup_scan_usb()
        self.Valeur1.setText(code_produit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inventairewindow = QtWidgets.QDialog()
    ui = Ui_InventaireWindow()
    ui.contenu_interface_balance(inventairewindow)
    inventairewindow.show()
    sys.exit(app.exec_())