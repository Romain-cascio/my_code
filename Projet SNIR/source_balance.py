#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from os import replace
import sys
import string
import re
import serial #librairie serie
import time #librairie gestion du temps

def recup_port_USB():
# création de l'objet type serial (port usb)
        poids = 0
        varBreak = 0
        
        balance_port = serial.Serial("/dev/cu.usbserial-FT3LHFLY", 9600, timeout=1)

        while True:
                balance_port.write("P\r\n".encode())
                data = balance_port.readline()
                vartmp = str(data)
                time.sleep(2)

                if(str(data) == "b''"):
                        varBreak = varBreak + 1
                        if(varBreak == 4):
                                break
                else:
                        if(str(data) == vartmp):
                                varBreak = varBreak + 1
                                if(varBreak == 4):
                                        break
                        poids = str(data).replace("\\", '').replace("b", '').replace("r", '').replace("n", '').replace("k", '').replace("g", '').replace("'", '').replace(" ", '')
                        print("poids = "+str(poids))

        return poids