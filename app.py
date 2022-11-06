from flask import Flask, render_template, url_for, request, redirect
import authenticate

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cookies = authenticate(username, password)
        return redirect('/')
        """
        try:
            authenticate(username, password)
            print(authenticate(username, password))
            return redirect('/')
        except:
            return "There was an issue"
        """
    else:
        return render_template('index.html', cookies=cookies)

if __name__ == "__main__":
    app.run(debug=True)