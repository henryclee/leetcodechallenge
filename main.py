import insertproblem
import insertuser
import removeuser
import bottle
import json

username = ''
password = ''

@bottle.route('/')
def htmlfile():
    return bottle.static_file('index.html',root='')

@bottle.route('/index.js')
def jsfile():
    return bottle.static_file('index.js',root='')

@bottle.route('/ajax.js')
def ajaxfile():
    return bottle.static_file('ajax.js',root='')

@bottle.post('/receiver')
def receiver():
    jsonBlob = bottle.request.body.read().decode()
    input = json.loads(jsonBlob)
    username = input['username']
    password = input['password']
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