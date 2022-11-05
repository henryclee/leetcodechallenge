import leetcode
import insertuser 
import insertproblem

# Get the next two values from your browser cookies
leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNzE3MzU2NiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjM3ZDlmM2U3ZWUyNmU4ZmNlZWMwNjRjMGQ4MzYyYzMwYzMzYjQ5MDQiLCJpZCI6NzE3MzU2NiwiZW1haWwiOiJtb3JnYW5saWFuZ2xpQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoibW9ydHlrdDUiLCJ1c2VyX3NsdWciOiJtb3J0eWt0NSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9hdmF0YXJzL2F2YXRhcl8xNjY2NTMyNDYzLnBuZyIsInJlZnJlc2hlZF9hdCI6MTY2NzY2OTM3NywiaXAiOiIyNjIwOmNjOjgwMDA6MWM4MjoyY2EzOjQ4ZjM6Njg5MzpkYzYiLCJpZGVudGl0eSI6ImFjZmY1MmExNjUyOTAxYWU3ZTQ0NmZiNDFiOTE4OWI3Iiwic2Vzc2lvbl9pZCI6Mjk4MjI0ODF9.ypvvER9XtpDnlrMR9Vt3WsdmCif3ATMqzqcEfi9x51o"
csrf_token = "r2KvEKKyiOBAr5BH5ZxWWyskRmMKQoG8r63kbQg1jULM0eIRfMC3bP5u9ddWa6HJ"

# Experimental: Or CSRF token can be obtained automatically
import leetcode.auth
csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)

configuration = leetcode.Configuration()

configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

graphql_request = leetcode.GraphqlQuery(
    query="""
      {
        user {
          username
          isCurrentUserPremium
        }
      }
    """,
    variables=leetcode.GraphqlQueryVariables(),
)

dict = api_instance.graphql_post(body=graphql_request).to_dict()

print(dict)

username = dict["data"]["user"]["username"]
print (username)

insertuser.insertuser(username)

api_response=api_instance.api_problems_topic_get(topic="algorithms")
solved_questions=[]
for questions in api_response.stat_status_pairs:

  insertproblem.insertproblem(username,questions)
  print(questions.to_dict()["stat"]["question__title"])
  if questions.status=="ac":
      solved_questions.append(questions.stat.question__title)

print("Total number of solved questions ",len(solved_questions))


