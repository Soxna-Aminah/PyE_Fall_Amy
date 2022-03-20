import mysql.connector
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
def connexionexe(r,p):
    connectpar={
        "host":"localhost",
        "user":"Aminah",
        "password":'Ami@h1998',
        "database":"projetpythonsql"
    }
    with mysql.connector.connect(**connectpar) as db:
                with db.cursor() as c:
                    c.execute(r,p)
                db.commit()
def connexionexeplus(r,p):
    connectpar={
        "host":"localhost",
        "user":"Aminah",
        "password":'Ami@h1998',
        "database":"projetpythonsql"
    }
    with mysql.connector.connect(**connectpar) as db:
                with db.cursor() as c:
                    c.executemany(r,p)
                db.commit()
def verifclass(var,r):
    l=connexionbaserecup(r)
    i=0
    while i<len(l):
        if l[i][1]==var:
            return l[i][0]
        i+=1
def insertClassEl(classe):
    r1="select *from Classe"
    if(verifclass(classe,r1)==None):
        nclasse=(classe,)
        r2="insert into Classe(nom_class) values(%s)"
        connexionexe(r2,nclasse)
        nl=verifclass(classe,r1)
    else:
        nl=verifclass(classe)
    return nl
 #fonction insertion matiere
def insertmat(file):
    mat=[]
    r3="insert into Matiere(nom_matiere) values(%s)"
    n=determinematiere(file)
    print(n)
    for i in n:
         mat.append((i,))
    connexionexeplus(r3,mat)
def imporsql(file):
    n=file[0]
    r1="insert into Eleve(numero,nom,prenom,datenaiss,id_classe) values(%s,%s,%s,%s,%s)"
    r3="select *from Matiere"
    classe=n["Classe"]
    num=n["Numero"]
    pren=n["Prénom"]
    nom=n["Nom"]
    note=n["Note"]
    datenais=n["Date de naissance"]
    clas=insertClassEl(classe)
    print(clas)
    tupel=(num,nom,pren,datenais,clas)
    for j in note:
        n=verifclass(j,r3)

    #insertmat(file)
    connexionexe(r1,tupel)


     