import mysql.connector
import removeuser

def insertuser(username: str, solved: int):

    config = {
        'user': 'hackathon',
        'password': 'hack',
        'host': '127.0.0.1',
        'database': 'codingchallenge',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    cursor.execute("SELECT userid FROM usertable WHERE leetcodeName = %s",[username])

    user = 0
    for id in cursor:
        user = cursor[0]
    if user == 0:
        removeuser(username)

    cursor.execute("INSERT INTO usertable (leetcodeName, number_solved) VALUES (%s)",[username, solved])

    cnx.commit()
    cursor.close()
    cnx.close()
