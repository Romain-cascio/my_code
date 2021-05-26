#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.resize(600, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(250, 550, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rename_label)

        ###################################################################

        self.label_nom_X = QLabel(self)
        self.label_nom_X.setObjectName("label")
        self.layout.addWidget(self.label_nom_X)
        self.label_nom_X.setText("NOM : ")

    def rename_label(self):
        self.label_nom1 = QLabel("test")
        self.label_nom1.setObjectName("label")
        self.layout.addWidget(self.label_nom1)
        self.label_nom1.setText("hello")

        # # create objects
        # label = QLabel(self.tr("Enter command and press Return"))
        # self.le = QLineEdit()
        # self.te = QTextEdit()

        # # layout
        # layout = QVBoxLayout(self)
        # # layout.addWidget(label)
        # layout.addWidget(self.le)
        # layout.addWidget(self.te)
        # self.setLayout(layout)

    #     # create connection
    #     self.connect(self.le, SIGNAL("returnPressed(void)"),
    #                  self.run_command)

    # def run_command(self):
    #     cmd = str(self.le.text())
    #     stdouterr = os.popen4(cmd)[1].read()
    #     self.te.setText(stdouterr)

if __name__ == "__main__":
    main()