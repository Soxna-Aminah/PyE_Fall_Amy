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
################################################
def supabrevmoi(m):
    m=m.lower()
    if m in "janvier":
        return"01"
    elif m in ["fevrier","février","fév","fev,févr,fevr"]:
        return"02"
    elif m in "mars":
        return"03"
    elif m in "avril":
        return"04"
    elif m in "mai":
        return"05"
    elif m in "juin":
        return "06"
    elif m in "juillet":
        return"07"
    elif m in "août":
         return"08"
    elif m in "septembre":
        return"09"
    elif m in "octobre":
        return"10"
    elif m in "novembre":        
        return"11"
    elif m in "decembre":
        return "12"
#######################################
from datetime import date
def datevalide(j,m,a):
    try:
        naiss=date(a,m,j)
        return True
    except ValueError:
        return False
########################################
import re
def transformdate(date):
    nx=[]
    x=re.split("[-/. _;:, .-]",date)
    t=len(x)
    i=0
    while i<t:
        if x[i]!="":
            nx.append(x[i])
        i+=1
    if len(nx)==3:
        j=nx[0]
        m=nx[1]
        a=nx[2]
        if m.isalpha():
            m=supabrevmoi(m)
            if m==None:
                return None
            else:
                m=int(m)
        elif m.isnumeric():
            m=int(m)
        else:
            return None
        j=int(j)
        if len(a)==2:
            a=int(a)
            if a>=22:
                a+=1900
            else:
                a+=2000
        else:
            a=int(a)
        if datevalide(j,m,a):
            j=str(j)
            m=str(m)
            a=str(a)
            ndate=j+"/"+m+"/"+a
            return ndate
        else:
            return None  
    else:
        return None
   
    #####################################################
def Prenomvalid(prenom):
        cpt=0
        for i in prenom:
            if i.isalpha():
                cpt+=1
        if prenom[0].isalpha() and cpt>=3:
            return True
        else:
            return False
#############################################
def nomvalid(nom):
    cpt=0
    for i in nom:
        if i.isalpha():
            cpt+=1
    if nom[0].isalpha() and cpt>=2:
        return True
    else:
        return False
############################################
def Numvalide(num):
    if len(num)==7 and num.isupper() and  num.isalnum():
        return True
    else:
        return False
###########################################
def classe(chaine):
    if "3" in chaine:
        if "A" in chaine:
            return "3iéme A"
        elif "B" in chaine:
            return "3iéme B"
        else:
            return None
    elif "4" in chaine:
        if "A" in chaine:
            return "4iéme A"
        elif "B" in chaine:
            return "4iéme B"
        else:
            return None
    elif "5" in chaine:
        if "A" in chaine:
            return "5iéme A"
        elif "B" in chaine:
            return "5iéme B"
        else:
            return None
    elif "6" in chaine:
        if "A" in chaine:
            return "6iéme A"
        elif "B" in chaine:
            return "6iéme B"
        else:
            return None
    else:
        return None
    ##################################
def calculmoyen(devoir):
        x=len(devoir)
        i=0
        s=0
        while i<x: 
            try:
                devoir[i]=float(devoir[i])
            except:
                return False
            
            if verifnotevalid(devoir[i])==True:
                s+=devoir[i]
                i+=1
            else:
                return False
        moyenne=s/x
        moyenne=round(moyenne,2)
        return moyenne
############################################
def calculmoygen(moydev,examen):
    examen=float(examen)
    if verifnotevalid(examen)==True:
        moygen=(moydev+ 2*examen)/3
        moygen=round(moygen,2)
        return moygen
    else:
        return False
##############################################
def verifnotevalid(note):
    if note>=0 and note<=20:
        return True
    else:
        return False
#############################################
def Note(note):
    dictnote={}
    listnot=[]
    listmat=[]
    notes=["devoir","examen","moydev","moygen"]
    dnote={}
    nlistnote=[]
    note=note.strip()
    note=note.replace(",",".")
    mat=re.split("[#]",note)
    x=len(mat)
    i=0
    while i<x:
        mat[i]=mat[i].replace("]","")
        mat[i]=mat[i].split("[")
        if len(mat[i])==2:
            listmat.append(mat[i][0])
            listnot.append(mat[i][1])
        else:
            return False
        i+=1
    x=len(listnot)
    i=0
    while i<x:
        listnot[i]=listnot[i].split(":")
        if len(listnot[i])==2:
            listnot[i][0]=listnot[i][0].split(";")
            moydev =calculmoyen(listnot[i][0])
            moygen=calculmoygen(moydev,listnot[i][1])
            if moydev!=False and moygen!=False:
                listnot[i].append(moydev)
                listnot[i].append(moygen)
                dnote=dict(zip(notes,listnot[i]))
                nlistnote.append(dnote)
            else:return False
        else:
            return False
        i+=1
    dictnote=dict(zip(listmat,nlistnote))
    return dictnote
    ###########################################
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
    if Prenomvalid(row["Prénom"])==False or not(Numvalide(row["Numero"])) or not(nomvalid(row["Nom"])) or row["Date de naissance"]==None or row["Classe"]==None or row["Note"]==False:
        if Prenomvalid(row["Prénom"])==False:
            invalidite["Prenom"]=True
        if Numvalide(row["Numero"])==False:
            invalidite["Numero"]=True
        if nomvalid(row["Nom"])==False:
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
###########################################################
def AfficherInvalide():
    for i in myfileinvalide:
        print(i)
###########################################################
def Affichervalide():
    for i in myfilevalide:
        print(i)
########################################################
def Affichinfnum(Numero):
    for i in myfilevalide:
        if i["Numero"]==Numero:
            print(i)
        else:
            for j in myfileinvalide:
                if j["Numero"]==Numero:
                    print(j)
        
########################################################
def determinematiere():
    matiere=[]
    for i in myfilevalide:
        for j in i["Note"]:
            matiere.append(j)
    matiere=set(matiere)
    return matiere
##########################################################
rep=True
ans=True
while rep:
    print("""
            1.Afficher les informations (Valide ou invalide)
            2.Afficher une information (par son numéro)
            3.Afficher les cinq premiers
            4.Modifier une information invalide ensuite le transférer dans la structure où se
trouve les informations valides
            5.Quitter
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
                Affichervalide()
            elif ans=="b":
                AfficherInvalide()
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
    elif rep=="4":
        print("Modification d'une information invalide")
    elif rep=="5":
        rep=None
    else:
        print("Choix indisponible")