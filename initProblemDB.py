import leetcode
import mysql.connector

def main():
    print("Initializing")

    leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDk4NDcyOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmI3ZTk5MzlkYjcxMWZhYjY3ZDc0ZTgzNjZmODEzMWNhOGM2MjllNiIsImlkIjo0OTg0NzI4LCJlbWFpbCI6ImhlbnJ5Y2xlZTczQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiaGVucnljbGVlIiwidXNlcl9zbHVnIjoiaGVucnljbGVlIiwiYXZhdGFyIjoiaHR0cHM6Ly9zMy11cy13ZXN0LTEuYW1hem9uYXdzLmNvbS9zMy1sYy11cGxvYWQvYXNzZXRzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTY2NzY3NTkyMCwiaXAiOiIyNjIwOmNjOjgwMDA6MWM4MjplMDg5OjM1NWM6MTk4OTo3ZTIyIiwiaWRlbnRpdHkiOiJhY2ZmNTJhMTY1MjkwMWFlN2U0NDZmYjQxYjkxODliNyIsInNlc3Npb25faWQiOjI5NjIzOTk2LCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.EOrBoQSgg6OSYMF57Rt5lbwJEe943ApPTRxXE2ZvcIo"
    csrf_token = "35sQ0s3VbY3uwtQ6Q0yKCh2Duuya51H7iOl16ohmdMjcbkNw8vqSNNdSCxlkBQDx"

    configuration = leetcode.Configuration()

    configuration.api_key["x-csrftoken"] = csrf_token
    configuration.api_key["csrftoken"] = csrf_token
    configuration.api_key["LEETCODE_SESSION"] = leetcode_session
    configuration.api_key["Referer"] = "https://leetcode.com"
    configuration.debug = False

    api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))


    config = {
        'user': 'hackathon',
        'password': 'hack',
        'host': '127.0.0.1',
        'database': 'codingchallenge',
        'raise_on_warnings': True
    }

    api_response=api_instance.api_problems_topic_get(topic="algorithms")

    
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    for questions in api_response.stat_status_pairs:
        problemName = questions.stat.question__title
        #print (problemName)
        easyVal = 0
        medVal = 0
        hardVal = 0
        if (questions.difficulty.level == 1):
            easyVal = 1
        elif (questions.difficulty.level == 2):
            medVal = 1
        else:
            hardVal = 1
        cursor.execute("INSERT INTO probleminfo (problem_name, easy, medium, hard) VALUES (%s, %s, %s, %s)",[problemName, easyVal, medVal, hardVal])

    cnx.commit()
    cursor.close()
    




if __name__ == "__main__":
    main()