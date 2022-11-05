import mysql.connector

def insertuser(username: str):



    config = {
        'user': 'hackathon',
        'password': 'hack',
        'host': '127.0.0.1',
        'database': 'codingchallenge',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    cursor.execute("INSERT INTO usertable (leetcodeName) VALUES (%s)",[username])

    cnx.commit()
    cursor.close()
    cnx.close()
