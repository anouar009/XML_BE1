#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:00 2017
BE 1 - XML
@author: Groupe 13
"""

import csv    
from collections import defaultdict          


#PARTIE LECTURE DE LA BASE
#_________________________

f = open("ponctualite-mensuelle-transilien.csv", encoding="ISO-8859-1")
csv_f = csv.reader(f, delimiter=";")   
data = []

for row in csv_f: 
   data.append(row)
f.close()


i=1
lst_rer=[]
lst_trans=[]
dico_rer=defaultdict(list)
dico_trans=defaultdict(list)


while i<len(data):
    if data[i][2]=="RER":
        
        if data[i][0] in lst_rer:
            dico_rer[str(data[i][0])].append(data[i])
        else:
            lst_rer.append(data[i][0])
            dico_rer[str(data[i][0])].append(data[i])
            
    else:
        if data[i][0] in lst_trans:
            dico_trans[str(data[i][0])].append(data[i])
        else:
            lst_trans.append(data[i][0])
            dico_trans[str(data[i][0])].append(data[i])
    if i==len(data):
        break
    else:
        i+=1
        
        

#PARTIE TRAITEMENT DE L'INFORMATION
#__________________________________
        
        
        
xml=open("ponctualite-mensuelle-transilien.xml", "a", encoding="ISO-8859-1")
xml.write("""<?xml version="1.0" encoding="ISO-8859-1"?>\n""")
xml.write("""<racine>
    <service serv="rer">""")
for k in lst_rer:
    xml.write("""
        <train id="%s">
            <ligne>%s</ligne>
            <nom_ligne>%s</nom_ligne>
            """ % (k, dico_rer[k][0][3],dico_rer[k][0][4]))
    for i in range(len(dico_rer[k])):
        xml.write("""
            <mesure>
                <date>%s</date>
                <taux>%s</taux>
                <ratio>%s</ratio>
            </mesure>
            """ % (dico_rer[k][i][1], dico_rer[k][i][5], dico_rer[k][i][6]))
        if i==len(dico_rer[k])-1:
            xml.write("""
        </train>
""")

xml.write("""    </service>

    <service serv="transilien">
    """)
for k in lst_trans:
    xml.write("""
        <train id="%s">
            <ligne>%s</ligne>
            <nom_ligne>%s</nom_ligne>
            """ % (k, dico_trans[k][0][3],dico_trans[k][0][4]))
    for i in range(len(dico_trans[k])):
        xml.write("""
            <mesure>
                <date>%s</date>
                <taux>%s</taux>
                <ratio>%s</ratio>
            </mesure>
            """ % (dico_trans[k][i][1], dico_trans[k][i][5], dico_trans[k][i][6]))
        if i==len(dico_trans[k])-1:
            xml.write("""
        </train>

        """)



xml.write("""    </service>
</racine>""")
xml.close()
        
