from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

username = ''
password = ''

@app.route('/', methods = ['POST'])
def index():
    if request.methods == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    return render_template("index.html")

'''
@app.route('/receiver', methods = ['POST'])
def usercredentialsInfo():
    testdata = {"hello":40}
    testDataJson = json.dumps(testdata)
    return testDataJson

'''
if __name__ == "__main__":
    app.run(debug=True)
