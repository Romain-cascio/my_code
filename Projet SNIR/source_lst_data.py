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

        file = open("ip_bdd.rtf", "r")
        ligne = file.readlines()
        ligne = str(ligne)
        ligne = ligne.split()
        ligne = ligne[-1]
        Host = ligne.replace("}", '').replace("'", '').replace("]", '')

        db = mc.connect(host = Host, database = 'quincaillerie', user = 'Inventaire', password = 'Inventaire/789')
        cursor = db.cursor()

        cursor.execute("SELECT nom_piece FROM piece")
        for ligne in cursor.fetchall():
            lst_nom_piece.append(str(ligne))

        cursor.execute("SELECT quantite_piece FROM piece")
        for ligne in cursor.fetchall():
            lst_quantité_piece.append(str(ligne))

        cursor.execute("SELECT prix_piece FROM piece")
        for ligne in cursor.fetchall():
            lst_prix_piece.append(str(ligne))

        cursor.execute("SELECT poids_piece FROM piece")
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