#coding utf8

import os.path, time
import csv, string
import fonctions
from codecs import open
import dat
import cfg


def fichier():


    nom="../../"+ input("Nom du fichier : ")

    rep = input("Format décimale: . séparateur: , ? ")
    if("non" in rep):  #Permet de convertir le fichier pour quil soit lisible par le programme 
        fonctions.Lisible(nom,1)



    try:
        user = input("identifiant : ")
        log = input("logiciel utilisé : ")
        index =input("présence d'un index ? ")
        titre=input("présence d'une première ligne avec les titres ? " )

        freq=input("fréquence du réseau : ")
        NbrSim = input("Nombre de simulation dans ce fichier : ")
        unite = input("Unité des valeurs ?")
       
        SignauxA=input("Nombre de signaux analogiques : ")
        SignauxD=input("Nombre de signaux digitaux : ")
        NbrSignaux= int(SignauxA) + int(SignauxD)
        
        dat.dat(nom,titre,index,NbrSim,NbrSignaux,1)
        cfg.cfg(nom,user,log,index,titre,freq,NbrSim,unite,SignauxA,SignauxD,1)    



        print("Fichier converti")
        #Signale la fin de la convertion


    except FileNotFoundError :

        print("Pas de fichier trouvé à ce nom ")
