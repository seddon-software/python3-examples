from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

loginTable = { 
               'tom' : 'mot',
               'sue' : 'eus',
               'jim' : 'mij'
              }

def is_valid_login(username, password):
    if username == '': 
        return False
    else:
        return loginTable[username] == password

def log_the_user_in(name):
    return render_template('successful_login.html', name=name)

def dont_log_the_user_in(name):
    return render_template('unsuccessful_login.html', name=name)


@app.route('/')
def try_to_login(name=None):
    return render_template('try_to_login.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if is_valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            # the code below is executed if the request method
            # was GET or the credentials were invalid
            return dont_log_the_user_in(request.form['username'])


if __name__ == "__main__":
    print "serving on localhost, port 5000"
    app.debug = True
    app.run()
