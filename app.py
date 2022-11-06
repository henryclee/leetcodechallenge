from flask import Flask, render_template, url_for, request, redirect
import authenticate

app = Flask(__name__)

arr = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            authenticate.authenticate(username, password)
            arr = authenticate.authenticate(username, password)
            return redirect('/')
        except:
            return "There was an issue"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)