#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import math
from PyQt4 import QtCore, QtGui
from source_balance import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.contenu_interface()
        self.show()

    def contenu_interface(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(800, 600)

        # self.process = QtCore.QProcess(self)
        # # self.terminal = QtGui.QWidget(self)
        # self.layout = QtGui.QVBoxLayout(self)
        # self.layout.addWidget(self.layout)
        # self.process.start('xterm',['-into', str(self.terminal.winId())])

        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 560))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))

        self.Layout_Label = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.Layout_Label.setMargin(0)
        self.Layout_Label.setObjectName(_fromUtf8("Layout_Label"))

        self.verticalLayoutWidget2 = QtGui.QWidget(self)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(170, 20, 160, 560))
        self.verticalLayoutWidget2.setObjectName(_fromUtf8("verticalLayoutWidget2"))

        self.Layout_Label2 = QtGui.QVBoxLayout(self.verticalLayoutWidget2)
        self.Layout_Label2.setMargin(0)
        self.Layout_Label2.setObjectName(_fromUtf8("Layout_Label"))

        self.Layout_Label2.setSpacing(48)

        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(650, 500, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rename_label)

        self.label_X_name = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_X_name.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_name)
        self.label_X_name.setText("NOM : ")

        self.label_X_Quantité = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_X_Quantité.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_Quantité)
        self.label_X_Quantité.setText("QUANTITÉ : ")

        self.label_X_prix = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_X_prix.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_prix)
        self.label_X_prix.setText("PRIX : ")

        self.label_X_poids = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_X_poids.setObjectName("label")
        self.Layout_Label.addWidget(self.label_X_poids)
        self.label_X_poids.setText("POIDS : ")

        self.Valeur1 = QtGui.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur1.setObjectName(_fromUtf8("Valeur1"))
        self.Layout_Label2.addWidget(self.Valeur1)

        self.Valeur2 = QtGui.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur2.setObjectName(_fromUtf8("Valeur2"))
        self.Layout_Label2.addWidget(self.Valeur2)

        self.Valeur3 = QtGui.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur3.setObjectName(_fromUtf8("Valeur3"))
        self.Layout_Label2.addWidget(self.Valeur3)

        self.Valeur4 = QtGui.QLineEdit(self.verticalLayoutWidget2)
        self.Valeur4.setObjectName(_fromUtf8("Valeur4"))
        self.Layout_Label2.addWidget(self.Valeur4)

        #################PARTIE LISTE DEROULANTE########################################################

        self.combo1 = QtGui.QComboBox(self)
        self.combo1.setGeometry(QtCore.QRect(350, 79, 200, 30))
        self.combo1.addItem("Ttest1")
        self.combo1.addItem("Ttest2")

        #################PARTIE LISTE DEROULANTE########################################################

        self.Checkstatu = QtGui.QCheckBox(self)
        self.Checkstatu.setGeometry(QtCore.QRect(600, 79, 30, 30))
        self.Checkstatu.setChecked(True)
        self.Checkstatu.toggled.connect(self.onClicked)

        self.labelcheck = QtGui.QLabel(self)
        self.labelcheck.setGeometry(QtCore.QRect(635, 79, 150, 30))
        self.labelcheck.setText("Activer / Désactiver")

    def onClicked(self):
        if(self.Checkstatu.isChecked()):
            self.combo1.setEnabled(True)
        else:
            self.combo1.setEnabled(False)


    def rename_label(self):
        print ("test")
        recup_port_USB()
        #####################MODIF VALUE################################################################
        # test = 10
        # self.Valeur1.setText(str(test))#Attribue la valeur 0
        #####################MODIF VALUE################################################################


        # self.label = QtGui.QLabel(self.verticalLayoutWidget2)
        # self.label.setObjectName("label")
        # self.Layout_Label2.addWidget(self.label)
        # self.label.setText("hello")

        # self.label2 = QtGui.QLabel(self.verticalLayoutWidget2)
        # self.label2.setObjectName("label")
        # self.Layout_Label2.addWidget(self.label2)
        # self.label2.setText("hello2")

        # self.Layout_lineEdit = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        # self.Layout_lineEdit.setMargin(0)
        # self.Layout_lineEdit.setObjectName(_fromUtf8("Layout_lineEdit"))

        ###################CREATION DES CASES POUR LES VALEURS D'ENTREES#######################
        # self.Valeur1 = QtGui.QLineEdit(self.verticalLayoutWidget2)
        # self.Valeur1.setObjectName(_fromUtf8("Valeur1"))
        # self.Layout_Label2.addWidget(self.Valeur1)

        # self.Valeur2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        # self.Valeur2.setObjectName(_fromUtf8("Valeur2"))
        # self.Layout_lineEdit.addWidget(self.Valeur2)
        # self.Valeur2.setText("0")

        # self.Valeur3 = QtGui.QLineEdit(self.verticalLayoutWidget)
        # self.Valeur3.setObjectName(_fromUtf8("Valeur3"))
        # self.Layout_lineEdit.addWidget(self.Valeur3)
        # self.Valeur3.setText("0")

        # self.Valeur4 = QtGui.QLineEdit(self.verticalLayoutWidget)
        # self.Valeur4.setObjectName(_fromUtf8("Valeur4"))
        # self.Layout_lineEdit.addWidget(self.Valeur4)
        # self.Valeur4.setText("0")

        # self.Valeur5 = QtGui.QLineEdit(self.verticalLayoutWidget)
        # self.Valeur5.setObjectName(_fromUtf8("Valeur5"))
        # self.Layout_lineEdit.addWidget(self.Valeur5)
        # self.Valeur5.setText("0")

        # self.Valeur6 = QtGui.QLineEdit(self.verticalLayoutWidget)
        # self.Valeur6.setObjectName(_fromUtf8("Valeur6"))
        # self.Layout_lineEdit.addWidget(self.Valeur6)
        # self.Valeur6.setText("0")

        # self.Valeur7 = QtGui.QLineEdit(self.verticalLayoutWidget)
        # self.Valeur7.setObjectName(_fromUtf8("Valeur7"))
        # self.Layout_lineEdit.addWidget(self.Valeur7)
        # self.Valeur7.setText("0")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fen = Ui_MainWindow()
    sys.exit(app.exec_())