from bottle import route, run, template, static_file, post, request
import getLeaders
import getNewProblem
import json
from authenticate import authenticateUser
import HELPERadd


@route("/")
def sendIndex ():
  return static_file("index2.html",root = ".")

@route("/ajax.js")
def sendAjax ():
  return static_file("ajax.js",root=".")

@route("/index2.js")
def sendIndexTest ():
  return static_file("index2.js",root=".")

@route("/leaderboard")
def sendLeaderBoard():
  retVal = [{"x":[],"y":[],"type":"bar"}]
  leaders = getLeaders.getLeaders()

  #print (leaders)

  for i in range(1, len(leaders)):
    retVal[0]["x"].append(leaders[i][0])
    retVal[0]["y"].append(leaders[i][1])

  #print (retVal)

  return (json.dumps(retVal))

@post('/receiver')
def receiver():
    jsonBlob = request.body.read().decode()
    userCred = json.loads(jsonBlob)
    username = userCred['username']
    password = userCred['password']
    login = authenticateUser(username, password)
    print(login)
    HELPERadd.addUser_addQuestion(login["LEETCODE_SESSION"], login["csrftoken"])
    loginJson = json.dumps(username)
    return loginJson  

run(host='localhost', port=8080)