import insertproblem
import insertuser
import removeuser
import bottle
import json
from authenticate import authenticateUser
import HELPERadd


@bottle.route('/')
def htmlfile():
    return bottle.static_file('index.html',root='.')

@bottle.route('/index.js')
def jsfile():
    return bottle.static_file('index.js',root='.')

@bottle.route('/ajax.js')
def ajaxfile():
    return bottle.static_file('ajax.js',root='.')

@bottle.post('/receiver')
def receiver():
    jsonBlob = bottle.request.body.read().decode()
    userCred = json.loads(jsonBlob)
    username = userCred['username']
    password = userCred['password']
    login = authenticateUser(username, password)
    print(login)
    HELPERadd.addUser_addQuestion(login["LEETCODE_SESSION"], login["csrftoken"])
    loginJson = json.dumps(username)
    return loginJson

def main():
    print ("Hello world")
    #name = "testname"
    #insertuser.insertuser(name)

if __name__ == "__main__":
    main()

bottle.run(host='0.0.0.0',port=8080,debug=True)