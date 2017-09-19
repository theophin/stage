import csv ,os

def Lisible(param1):   
    fichier = param1+".csv"
    with open (fichier, encoding='utf8',errors= 'replace') as csv_file :
      with open(param1+"1.csv",'w') as file:
        for line in csv_file :
              fields= line.split(',') 
              fields='.'.join(fields)
              ret =fields.split(';')
              file.write(','.join(ret))
              
    os.remove(fichier)
    os.rename(param1+"1.csv",fichier)

def CalculeFreq(param1,param2) :
    return (1/(param2-param1))