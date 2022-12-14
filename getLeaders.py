import mysql.connector

def getLeaders():

    config = {
        'user': 'hackathon',
        'password': 'hack',
        'host': '127.0.0.1',
        'database': 'codingchallenge',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    cursor.execute("SELECT leetcodeName, number_solved FROM usertable ORDER BY number_solved DESC LIMIT 10")

    leaders = [(str,int)]

    for leader in cursor:
        leaders.append(leader)
    
    cnx.commit()
    cursor.close()
    cnx.close()

    return leaders