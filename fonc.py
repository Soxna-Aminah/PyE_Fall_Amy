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
    l2=["A","B","C","D"]
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
    dictnote=dict(zip(listmat,nlistnote))
    return dictnote
    ###########################################
def Afficherinf(file):
    for i in file:
        n=i["Numero"]
        pren=i["Prénom"]
        nom=i["Nom"]
        datenaiss=i["Date de naissance"]
        notess=i["Note"]
        print("Numero: ",n," Prénom: ",pren,"  Nom: ",nom," Date de Naissance",datenaiss)
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
            matiere.append(j)
    matiere=set(matiere)
    return matiere
##########################################################
def Affich5premier(Notes):
    for i in Notes:
        moy=Notes[i]["moygen"]