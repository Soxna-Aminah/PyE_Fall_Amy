from select import select
import mysql.connector
from datetime import datetime
from csv import*

from sqlalchemy import insert 
####Fonction pour abréger un mois#######
def supabrevmoi(m):
    r=None
    dictm={"ja":"01","f":"02","mars":"03","av":"04","mai":"05","juin":"06","juil":"07","ao":"08","sep":"09","oct":"10","nov":"11","dec":"12"
    }
    for key,value in dictm.items():
        if key in m:
            r=value
    return r
###########Fonction validité date############
from datetime import date
def datevalide(j,m,a):
    try:
        naiss=date(a,m,j)
        return True
    except ValueError:
        return False
###################Transformer la date ############################
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
            try:
                ndate=datetime.strptime(ndate, "%d/%m/%Y")
            except:
                return None


            return ndate
        else:
            return None  
    else:
        return None
   ########################### Fonction nom et prenom valide######
def Pre_nomvalid(var,n):
        cpt=0
        for i in var:
            if i.isalpha():
                cpt+=1
        if var[0].isalpha() and cpt>=n:
            return True
        else:
            return False
#####################################Fonction numero valide###################
def Numvalide(num):
    if len(num)==7 and num.isupper() and  num.isalnum():
        return True
    else:
        return False
##########################Fonction classe valide
def classe(chaine):
    l1=["3","4","5","6"]
    l2=["A","B"]
    nclass=None
    for i in l1:
        for j in l2:
            if i in chaine and j in chaine:
                nclass=i+"iéme"+j
    return nclass
############################Calcule de moyenne de devoir#######################
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
########################## Calcul de la moyenne general##################
def calculmoygen(moydev,examen):
    examen=float(examen)
    if verifnotevalid(examen)==True:
        moygen=(moydev+ 2*examen)/3
        moygen=round(moygen,2)
        return moygen
    else:
        return False
###################### Vérification note valide########################
def verifnotevalid(note):
    if note>=0 and note<=20:
        return True
    else:
        return False
def matiere(liste):
    li=[]
    for i in liste:
        i=i.strip()
        if i[0]=="F":
                i="Francais"
        elif i=="Science_Physique":
            i="PC"
        li.append(i)
    return li

########################Traitement des notes#####################
def Note(note):
    dictnote={}
    listnot=[]
    listmat=[]
    notes=["devoir","examen","moydev","moygen"]
    dnote={}
    nlistnote=[]
    note=str(note)
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
    listmat=matiere(listmat)
    dictnote=dict(zip(listmat,nlistnote))
    return dictnote
    ###########################################
def Afficherinf(file):
    for i in file:
        n=i["Numero"]
        pren=i["Prénom"]
        nom=i["Nom"]
        datenaiss=i["Date de naissance"]
        classe=i["Classe"]
        notess=i["Note"]
        print("Numero: ",n," Prénom: ",pren,"  Nom: ",nom," Date de Naissance: ",datenaiss," Classe: ",classe)
        print("Notes: ")
        #print(notess)
        for j in notess:
            dev=notess[j]["devoir"]
            exam=notess[j]["examen"]
            moydev=notess[j]["moydev"]
            moygen=notess[j]["moygen"]
            
            print(j," Devoir:",dev,"Examen: ",exam,"Moyenne de Devoir: ",moydev,"Moyenne général: ",moygen)
        print("----------------------------------------------------------------------------------------------")
##############################################
def Affichinfnum(Numero,file):
    for i in file:
        if i["Numero"]==Numero:
            print(i)
        else:
            for j in file:
                if j["Numero"]==Numero:
                    print(j)
        
########################################################
def determinematiere(file):
    matiere=[]
    for i in file:
        for j in i["Note"]:
            j=j.strip()
            if j[0]=="F":
                j="Francais"
            elif  j=="Science_Physique":
                j="PC"
            matiere.append(j)
    matiere=set(matiere)
    matiere=list(matiere)
    return matiere
##########################################################
def moygenerale(file):
    i=0
    m=len(file)
    listmoy=[]
    while i<m:
        l=0
        s=0
        for j in file[i]["Note"]:
           n=str(j)
           s+=file[i]["Note"][n]["moygen"]
           l+=1
        moy=s/l
        listmoy.append(moy)
        file[i]["Moyenne General"]=moy
        i+=1
    return file

##########################################
def en_fonction(row):
    return row["Moyenne General"]
#########################################
def Affich5premier(file):
    nfile=moygenerale(file)
    nfile.sort(key=en_fonction,reverse=True)
    for i in range(5):
        print(nfile[i])
#############
def connexionbaserecup(r):
    connectpar={
        "host":"localhost",
        "user":"Aminah",
        "password":'Ami@h1998',
        "database":"projetpythonsql"
    }
    with mysql.connector.connect(**connectpar) as db:
            with db.cursor() as c:
                c.execute(r)
                n=c.fetchall()
                return n
#remplir clé etrangére éléve
def classeleve(classe,r):
     connectpar={
     "host":"localhost",
    "user":"Aminah",
    "password":'Ami@h1998',
    "database":"projetpythonsql"}
     with mysql.connector.connect(**connectpar) as db:
        with db.cursor() as c:
            c.execute(r)
            n=c.fetchall()
            k=0
            while k<len(n):
                if n[k][1]==classe:
                    nclass=n[k][0]
                    return nclass
                k+=1
# #importer dans la base
#fonction insertion Classe
def inserClasse(file):
    i=0
    li=[]
    while i<len(file):
      n=file[i]["Classe"]
      n=(n,)
      li.append(n)
      i+=1
    li=set(li)
    li=list(li)
    return li
#fonction insertion Eleve
def insertEleve(file):
    r="select *from Classe"
    elv=[]
    i=0
    while i<len(file):
        n=file[i]["Classe"]
        num=file[i]["Numero"]
        pren=file[i]["Prénom"]
        nom=file[i]["Nom"]
        daten=file[i]["Date de naissance"]
        nc=classeleve(n,r)
        el=(num,nom,pren,daten,nc)
        elv.append(el)
        i+=1
    return elv
#fonction insertion matiere
def insertmat(file):
    mat=[]
    n=determinematiere(file)
    for i in n:
         mat.append((i,))
    return mat
def verifclass(var,r):
    l=connexionbaserecup(r)
    i=0
    while i<len(l):
        if l[i][1]==var:
            return l[i][0]
        i+=1
def insertnote(file):
    r2="select id_eleve,numero from Eleve"
    r3="select *from Matiere"
    i=0
    note=[]
    while i<len(file):
        notes=file[i]["Note"]
        num=file[i]["Numero"]
        id_el=verifclass(num,r2)
        for j in notes:
            mat=verifclass(j,r3)
            dev=notes[j]["devoir"]
            for k in dev:
                note.append(("devoir",k,mat,id_el))
            exam=float(notes[j]["examen"])
            note.append(("examen",exam,mat,id_el))
        i+=1
    return note
def moyenne(file):
    limoy=[]
    nfile=moygenerale(file)
    r2="select id_eleve,numero from Eleve"
    i=0
    while i<len(nfile):
        num=nfile[i]["Numero"]
        moygen=nfile[i]["Moyenne General"]
        id_el=verifclass(num,r2)
        n=(moygen,id_el)
        limoy.append(n)
        i+=1
    return limoy
def calculmoyenn(dev,exam):
     moydev=sum(dev)/len(dev)
     moyenn=(2*exam+moydev)/3
     moyenn=round(moyenn,2)
     return moyenn
def calculmoyelev(moy):
    moyenegen=sum(moy)/len(moy)
    moyenegen=round(moyenegen,2)
    return moyenegen

def creatriiger():
    r="""DELIMITER |
         create trigger after_update_Note before update
         on Note
         for each row
         BEGIN
         DECLARE note FLOAT
            BEGIN

         
         
             """
def imporsql(file):
    elv=insertEleve(file)
    li=inserClasse(file)
    mat=insertmat(file)
    note=insertnote(file)
    moy=moyenne(file)
    # exam=insertnote(file)[1]
    connectpar={
     "host":"localhost",
    "user":"Aminah",
    "password":'Ami@h1998',
    "database":"projetpythonsql"}
    r="insert into Classe(nom_class) values(%s)"
    r1="insert into Eleve(numero,nom,prenom,datenaiss,id_classe) values(%s,%s,%s,%s,%s)"
    r3="insert into Matiere(nom_matiere) values(%s)"
    r4="insert into Note(type_note,note,id_matiere,id_eleve) values(%s,%s,%s,%s)"
    r5="insert into Moyenne(moyenne,id_eleve) values(%s,%s)"
    with mysql.connector.connect(**connectpar) as db:
        with db.cursor() as c:
            pass
            #c.executemany(r,li)
            #c.executemany(r1,elv)
            #c.executemany(r3,mat)
            c.executemany(r4,note)
            # c.executemany(r5,moy)
        db.commit()

