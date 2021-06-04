#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import string
import re
import mysql.connector as mc

def listing_données():

        x = 0
        
        lst_nom_piece = []
        lst_quantité_piece = []
        lst_prix_piece = []
        lst_poids_piece = []

        db = mc.connect(host = 'localhost', database = 'quincaillerie', user = 'inventoriste', password = 'root') 
        cursor = db.cursor()

        cursor.execute("SELECT nom_piece FROM info_piece")
        for ligne in cursor.fetchall():
            lst_nom_piece.append(str(ligne))

        cursor.execute("SELECT quantité FROM info_piece")
        for ligne in cursor.fetchall():
            lst_quantité_piece.append(str(ligne))

        cursor.execute("SELECT prix FROM info_piece")
        for ligne in cursor.fetchall():
            lst_prix_piece.append(str(ligne))

        cursor.execute("SELECT poids FROM info_piece")
        for ligne in cursor.fetchall():
            lst_poids_piece.append(str(ligne))

        while (x < len(lst_nom_piece)):
            lst_nom_piece[x] = re.sub("[',()]", '', lst_nom_piece[x])
            x = x + 1
        x = 0

        while (x < len(lst_quantité_piece)):
            lst_quantité_piece[x] = re.sub("[',()]", '', lst_quantité_piece[x])
            x = x + 1
        x = 0

        while (x < len(lst_prix_piece)):
            lst_prix_piece[x] = re.sub("[',()]", '', lst_prix_piece[x])
            x = x + 1
        x = 0

        while (x < len(lst_poids_piece)):
            lst_poids_piece[x] = re.sub("[',()]", '', lst_poids_piece[x])
            x = x + 1

        return lst_nom_piece, lst_quantité_piece, lst_prix_piece, lst_poids_piece

if __name__ == "__main__":
    listing_données()