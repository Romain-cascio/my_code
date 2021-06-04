#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import serial #librairie serie
import time #librairie gestion du temps

def recup_port_USB():
# création de l'objet type serial (port usb)
        poids = 0

        balance_port = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

        while True:
                balance_port.write("P\r\n".encode())
                data = balance_port.readline()
                
                if (data != b''):
                        poids = int(data)
                        print(data.decode('utf-8'))
                        print("int poids : ")
                        print(poids)
                time.sleep(2)

        poids = re.sub("[',()]", '', poids)
        balance.close()

        return poids