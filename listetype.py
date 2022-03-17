import random
import mysql.connector
liste=["depot","retrait"]
i=0
nl=[]
while i<100:
    r=(random.choice(liste),)
    nl.append(r)
    i+=1

connectpar={
     "host":"localhost",
    "user":"Aminah",
    "password":'Ami@h1998',
    "database":"DB_LemGUI"}
req="insert into TYPE(type) values (%s)"
with mysql.connector.connect(**connectpar) as db:
        with db.cursor() as c:
            c.executemany(nl)