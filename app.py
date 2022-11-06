from flask import Flask, render_template, url_for, request, redirect
import authenticate

app = Flask(__name__)

arr = {}

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/receiver', methods=['POST'])
def receiver():
    username = request.form['username']
    password = request.form['password']
    try:
        # arr = authenticate.authenticate(username, password)
        new = authenticate.authenticate(username, password)
        for key in new:
            arr[key] = new[key]
        print(arr)
    except:
        return "ERROR: There was an issue"
    return render_template('index.html', arr=arr)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)