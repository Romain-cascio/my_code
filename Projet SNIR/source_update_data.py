#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import string
import re
import mysql.connector as mc

def Update_to_base(UpdateName, UpdateQuantite, UpdatePrix, UpdatePoids, n):
    x = 0
    lst_id = []

    file = open("ip_bdd.rtf", "r")
    ligne = file.readlines()
    ligne = str(ligne)
    ligne = ligne.split()
    ligne = ligne[-1]
    Host = ligne.replace("}", '').replace("'", '').replace("]", '')

    db = mc.connect(host = Host, database = 'quincaillerie', user = 'Inventaire', password = 'Inventaire/789')
    cursor = db.cursor()

    cursor.execute("SELECT id FROM piece")
    for ligne in cursor.fetchall():
            lst_id.append(str(ligne))

    while (x < len(lst_id)):
            lst_id[x] = re.sub("[',()]", '', lst_id[x])
            x = x + 1
    x = 0

    cursor.execute("UPDATE info_piece SET nom_piece = %s, quantité = %s, prix = %s, poids = %s WHERE id = %s", (UpdateName, UpdateQuantite, UpdatePrix, UpdatePoids, lst_id[n]))
    db.commit()
    db.close()