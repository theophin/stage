import fichier
import dossier

n=1
print("Ne prennez pas en compte l'emplacement du .exe mais celui du dossier build")
while (n==1):
		
	hans = input("Voulez-vous traiter un dossier ou un fichier ? ")
	if("dossier" in hans.lower()):
		dossier.dossier()
	elif("fichier"in hans.lower()):
		fichier.fichier()
	else:
		print("Ecrivez fichier ou dossier")

	choix = input("Avez-vous fini ? ")
	if("oui" in choix.lower()):
		n=2
	
