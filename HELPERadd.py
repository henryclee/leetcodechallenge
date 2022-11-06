import leetcode
# import insertuser 
# import insertproblem

def addUser_addQuestion(session, token):

#   # Get the next two values from your browser cookies

  leetcode_session = session
  csrf_token = token

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

  # insertuser.insertuser(username)

  api_response=api_instance.api_problems_topic_get(topic="algorithms")
  solved_questions=[]
  counter = 0

  for questions in api_response.stat_status_pairs:

    if questions.status=="ac":
    
      solved_questions.append(questions.stat.question__title)
      # insertproblem.insertproblem(username,questions)
      print(questions.to_dict()["stat"]["question__title"])
      counter+=1

  print()
  print("Total number of solved questions ",len(solved_questions), "expected: ", counter)
  print()


