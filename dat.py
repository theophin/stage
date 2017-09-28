import os.path, time
import csv, string
import fonctions
from codecs import open

def dat(nom,titre,index,simu,NbrSignaux,type):

  if(type==2) :
        nom=os.path.splitext(nom)[0]
    
  fichier = nom+".csv"
  
    
  n=0
  a=2
  while n<int(simu):
    with open (fichier, 'r',  encoding='utf8',errors= 'replace') as csvfile : #ouvre le fichier contenant les simulations
      data = nom+str(n)+'.dat'
      reader = csv.reader(csvfile)
       
          
      with open(data, 'w', encoding='utf8') as dfile : #ouverture ou creation du .dat
                    
           wd = csv.writer(dfile, quoting=csv.QUOTE_NONE,escapechar=' ') #creation  de loutil decriture de pour le .dat

           if("oui"in titre) :
               header = next(reader) #recupere la première ligne du fichier contenant les noms des signaux 
           
                    
           if("oui" in index ):
                for row in reader :
                  wd.writerow(row[0:2]+row[a:a+NbrSignaux]) #Ecrit toujours les 2 premieres colonnes puis les colonnes des signaux concernes


           else :
                k=1
                for row in reader :
                    wd.writerow([k]+[row[0]]+row[a-1:a+NbrSignaux-1])
                k+=1
                                                        

    a+=NbrSignaux
    
    n+=1
  
