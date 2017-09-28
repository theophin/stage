import csv ,os

def Lisible(param1,type):   
  if(type==1) :
    fichier = param1+".csv"
  else : 
    fichier=param1

    with open (fichier, encoding='utf8',errors= 'replace') as csv_file :
      with open("out",'w') as file:
        for line in csv_file :
              fields= line.split(',') 
              fields='.'.join(fields)
              ret =fields.split(';')
              file.write(','.join(ret))
              
    os.remove(fichier)
    os.rename("out",fichier)

def CalculeFreq(param1,param2) :
    return (1/(param2-param1))

def  essai(nom):
	
	if ("toto"in nom):
		print("nice")
	