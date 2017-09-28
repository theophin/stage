
from os import listdir
from os.path import isfile,join
import fonctions
import dat
import cfg


def dossier():
    folder="../../"+ input("Nom du dossier : ")
    print("Assurez vous que tous les fichiers soient des .csv")
    try:
    

        files = [f for f in listdir(folder) if isfile(join(folder,f))]

        rep = input("Format décimale: . séparateur: , ? ")
               
        user = input("identifiant : ")
        log = input("logiciel utilisé : ")
        index =input("présence d'un index ? ")
        titre=input("présence d'une première ligne avec les titres ? " )
                
        freq=input("fréquence des réseaux : ")
        NbrSim = input("Nombre de simulation dans les fichiers : ")
        unite = input("Unité des valeurs ?")
        
        SignauxA=input("Nombre de signaux analogiques : ")
        SignauxD= input("Nombre de signaux digitaux : ")
        NbrSignaux= int(SignauxA) + int(SignauxD)

        for i in files:
                fichier=folder+"/"+i

                if("non" in rep):  #Permet de convertir le fichier pour quil soit lisible par le programme 
                    fonctions.Lisible(fichier,2)

                dat.dat(fichier,titre,index,NbrSim,NbrSignaux,2)
                cfg.cfg(fichier,user,log,index,titre,freq,NbrSim,unite,SignauxA,SignauxD,2)
        print("Tous les fichiers du dossier sont convertis")
    except FileNotFoundError:
        print("Le dossier est introuvable ou un fichier n'est pas dans le bon format")
       
      
