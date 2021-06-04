#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

import sys
import string
import re
import mysql.connector as mc

def Update_to_base(UpdateName, UpdateQuantite, UpdatePrix, UpdatePoids, n):

    print(UpdateName)

    x = 0
    lst_id = []

    db = mc.connect(host = 'localhost', database = 'quincaillerie', user = 'inventoriste', password = 'root') 
    cursor = db.cursor()

    cursor.execute("SELECT id FROM info_piece")
    for ligne in cursor.fetchall():
            lst_id.append(str(ligne))

    while (x < len(lst_id)):
            lst_id[x] = re.sub("[',()]", '', lst_id[x])
            x = x + 1
    x = 0

    cursor.execute("UPDATE info_piece SET nom_piece = %s, quantité = %s, prix = %s, poids = %s WHERE id = %s", (UpdateName, UpdateQuantite, UpdatePrix, UpdatePoids, lst_id[n]))
    db.commit()
    db.close()


if __name__ == "__main__":
    Update_to_base()