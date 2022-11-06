import insertproblem
import insertuser
import removeuser
import bottle
import json
import authenticate
import bottle
from bottle import response

@bottle.route('/')
def htmlfile():
    return bottle.static_file('index.html',root='')

@bottle.route('/index.js')
def jsfile():
    return bottle.static_file('index.js',root='')

@bottle.post('/receiver')
def receiver():
    jsonBlob = bottle.request.body.read().decode()
    input = json.loads(jsonBlob)
    authenticate.authenticate(input['username'],input['password'])
    temp = {"hello":"world"}
    retval = json.dumps(temp)
    return retval

def main():
    print ("Hello world")

    name = "testname"
    insertuser.insertuser(name)

if __name__ == "__main__":
    main()

bottle.run(host='0.0.0.0',port=8080,debug=True)