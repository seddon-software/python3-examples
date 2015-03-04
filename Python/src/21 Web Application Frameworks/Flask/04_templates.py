from flask import Flask
from flask import render_template

# This example uses 'Jinja2' templates 

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    print "serving on localhost, port 5000"
    app.debug = True
    app.run()
    