import mysql.connector

def insertproblem(name: str, problem: str):

    print ("name:" + name)
    print ("problem:" + problem)

    config = {
        'user': 'hackathon',
        'password': 'hack',
        'host': '127.0.0.1',
        'database': 'codingchallenge',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    cursor.execute("SELECT userid FROM usertable WHERE leetcodeName = %s",[name])

    user = 0

    for id in cursor:
        user = id[0]

    cursor.execute("SELECT problemid FROM probleminfo WHERE problem_name = %s",[problem])

    problem = 0

    for p in cursor:
        problem = p[0]

    print (str(user) + " " + str(problem))

    cursor.execute("INSERT INTO solved (userid, problemid) VALUES (%s,%s)",[user,problem])

    cnx.commit()
    cursor.close()
    cnx.close()