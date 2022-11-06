import insertproblem
import insertuser
import removeuser
import bottle
import json
import authenticate

def main():
    print ("Hello world")

    name = "testname"
    insertuser.insertuser(name)

if __name__ == "__main__":
    main()