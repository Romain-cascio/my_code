#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import string
import re
import serial
import time #librairie gestion du temps

def recup_scan_usb():
    scan_port = serial.Serial("/dev/ttys003", 9600, timeout=1)

    while (True):
        if(str(data) == "b''"):
            varBreak = varBreak + 1
            if(varBreak == 4):
                break
        scan_port.write("P\r\n".encode())
        data = scan_port.readline()
        code_produit = str(data)
        time.sleep(2)
    
    return code_produit

if __name__ == "__main__":
    recup_scan_usb()