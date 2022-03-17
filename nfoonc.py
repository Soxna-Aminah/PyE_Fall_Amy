import mysql.connector
def connexionexe(r):
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
r="select *from Classe"
n=connexionexe(r)
print(n)