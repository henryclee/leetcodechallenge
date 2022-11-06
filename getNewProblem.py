import mysql.connector
import random

def getNewProblem(users, level: int):

    config = {
        'user': 'hackathon',
        'password': 'hack',
        'host': '127.0.0.1',
        'database': 'codingchallenge',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    completedSet = (())
    questionsSet = (())

    cursor = cnx.cursor()

    for user in users:
        cursor.execute("SELECT userid FROM usertable WHERE leetcodeName = %s",[user])
        userid = 0

        for id in cursor:
            userid = id[0]
        cursor.execute("SELECT problemid FROM solved WHERE userid = %s",[userid])

        problem = 0

        for p in cursor:
            problem = p[0]
            completedSet.add(problem)

    if level == 1:
        cursor.execute("SELECT problemid FROM probleminfo WHERE easy = 1")
    elif level == 2:
        cursor.execute("SELECT problemid FROM probleminfo WHERE medium = 1")
    else:
        cursor.execute("SELECT problemid FROM probleminfo WHERE hard = 1")

    for p in cursor:
        problem = p[0]
        questionsSet.add(problem)

    notCompleted = questionsSet - completedSet

    rndIndex = random.randrange(0,len(notCompleted))
    rndProblemID = list(notCompleted)[rndIndex]

    cursor.execute("SELECT problem_name FROM probleminfo WHERE problemid = %s",[rndProblemID])

    answer = ""

    for name in cursor:
        answer = name[0]

    return answer
    




    



    cnx.commit()
    cursor.close()
    cnx.close()