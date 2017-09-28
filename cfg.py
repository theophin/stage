
import os.path, time
import csv, string
import fonctions
from codecs import open


def cfg(nom,user,log,index,titre,freq,NbrSim,unite,SignauxA,SignauxD,type):
    if(type==2) :
        nom=os.path.splitext(nom)[0]
    
    fichier = nom+".csv"
    
    freqE=0 
    NbrSignaux= int(SignauxA) + int(SignauxD)
    n=0
    a=2
    while n<int(NbrSim):
        with open (fichier, 'r',  encoding='utf8',errors= 'replace') as csvfile : #ouvre le fichier contenant les simulations
          data = nom+str(n)+'.cfg'
          reader = csv.reader(csvfile)
           
              
          with open(data, 'w', encoding='utf8') as cfile : #ouverture ou creation du .cfg
                        
            wc = csv.writer(cfile, quoting=csv.QUOTE_NONE,escapechar=' ') #creation  de loutil decriture de pour le .cfg
            NbrP = 0
              
            if("oui"in titre) :

                header = next(reader) #recupere la première ligne du fichier contenant les noms des signaux 
            else:
                header = list(string.ascii_uppercase) #recupere lalphabet si la premiere ligne ne contient pas de titres

            if("oui" in index ): 

                k=0
                b=0
                for row in reader :
                    NbrP+=1  #Compte le nombre de valeur
                    if(k==1):
                        c=float(row[1])
                    if(b==2):
                        d=float(row[1])
                    k+=1
                    b+=1
            else :
                b=0
                f=0
                for row in reader :
                    NbrP+=1
                    if(b==1):
                        c=float(row[0])
                    if(f==2):
                        d=float(row[0])
                    f+=1
                    b+=1
            
            freqE=fonctions.CalculeFreq(c,d)
            wc.writerow([user]+[log]) #Ecrit la premiere ligne du .cfg avec lindentifiant et le logiciel utilise
            wc.writerow([NbrSignaux]+[SignauxA+'A']+[SignauxD+'D']) #Ecrit la deuxieme ligne avec le nombre total de signaux, le nombres de signaux analogiques et le nombre de signaux digitaux

            for i in range (1,NbrSignaux+1) :
                wc.writerow([i]+[header[i+a-1]]+['']+['']+[unite]+[1]+[0]+[0.0]+[-32767]+[32767])
            wc.writerow([freq]) #Ecrit la frequence du reseau
            wc.writerow('1')#Nombre de frequence de la simulation
            wc.writerow([freqE]+[NbrP]) #Ecrit la frequence dechantillonage et le nombre de point de la simulation
            wc.writerow([time.strftime("%d/%m/%y,%H:%M:%S",time.gmtime(os.path.getctime(fichier)))]) #Ecrit la date de creation du fichier .csv
            wc.writerow([time.strftime("%d/%m/%y,%H:%M:%S",time.gmtime(os.path.getctime(fichier)))])
            wc.writerow(['ASCII']) #Ecrit lencodage par defaut du fichier .cfg
                                                            

        a+=NbrSignaux
        
        n+=1
      


