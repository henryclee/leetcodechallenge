import mysql.connector

def removeuser(username: str):

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
    for userids in cursor:
        user = cursor[0]

    cursor.execute("DELETE FROM usertable WHERE leetcodeName = %s",[username])

    cursor.execute("DELETE FROM solved WHERE userid = %s",[user])

    cnx.commit()
    cursor.close()
    cnx.close()

