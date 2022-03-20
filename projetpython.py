from doctest import FAIL_FAST
from fonc import*
from collections import OrderedDict
#Suppression des valeurs manquantes
import csv
outfile = open("nfile",'w')
writer=csv.writer(outfile)
with open("file.csv",'r') as infile:
    reader = csv.reader(infile,delimiter=",")
    for row in reader:
        del(row[0])
        if any(field.strip() for field in row):
            writer.writerow(row)
outfile.close()
infile.close()
#########Traitement
from csv import DictReader
myfilevalide=[]
myfileinvalide=[]
invalidite={}
file=open("nfile",'r',encoding="utf8")
csv_reader=DictReader(file)
for row in  csv_reader:
    row["Date de naissance"] =transformdate(row["Date de naissance"])
    row["Classe"]=classe(row["Classe"])
    row["Note"]=Note(row["Note"])
    if Pre_nomvalid(row["Prénom"],3)==False or not(Numvalide(row["Numero"])) or not(Pre_nomvalid(row["Nom"],2)) or row["Date de naissance"]==None or row["Classe"]==None or row["Note"]==False:
        if Pre_nomvalid(row["Prénom"],3)==False:
            invalidite["Prenom"]=True
        if Numvalide(row["Numero"])==False:
            invalidite["Numero"]=True
        if Pre_nomvalid(row["Nom"],2)==False:
            invalidite["Nom"]=True
        if row["Date de naissance"]==None:
            invalidite["Date de naissance"]=True
        if row["Classe"]==None:
            invalidite["Classe"]=True
        if row["Note"]==False:
            invalidite["Note"]=True
        row["invalidite"]=invalidite
        myfileinvalide.append(row)
    else:
         myfilevalide.append(row)    
                       
file.close()            
rep=True
ans=True
while rep:
    print("""
            1.Afficher les informations (Valide ou invalide)
            2.Afficher une information (par son numéro)
            3.Afficher les cinq premiers
            4.Modifier une information invalide ensuite le transférer dans la structure où se
trouve les informations valides
            5.Importer dans la base sql
            6.Quitter
         """)
    rep=input("Faites votre choix: ")
    if rep=="1":
        print("Affichages des informations Valide ou invalide")
        while ans:
            print("""
                    a)Afficher les information valide
                    b)Afficher les information invalide
                    c)Quitter""")
            ans=input("Faites votre choix: ")
            if ans=="a":
                Afficherinf(myfilevalide)
            elif ans=="b":
                Afficherinf(myfileinvalide)
            elif ans=="c":
                ans=False
            else:
                print("Choix indisponible")
    elif rep=="2":
        print("Affichage d'une information par son numero")
        num=input("Saisir son numero: ")
        Affichinfnum(num)
    elif rep=="3":
        print("Afficher les cinq premiers")
        Affich5premier(myfilevalide)
    elif rep=="4":
        print("Modification d'une information invalide")
    elif rep=="5":
        print("Importer dans la base")
        imporsql(myfilevalide)
    elif rep=="6":
        rep=None
    else:
        print("Choix indisponible")

