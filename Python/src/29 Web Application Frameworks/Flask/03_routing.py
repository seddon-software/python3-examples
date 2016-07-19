from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Index Page"

@app.route('/route1')
def page1():
    return 'Route 1'

@app.route('/route2')
def page2():
    return 'Route 2'

@app.route('/user/<day>')
def day(day):
    return 'User {0}'.format(day)

@app.route('/sum/<int:x>/<int:y>')
def summation(x, y):
    return str(x + y)

if __name__ == "__main__":
    print "serving on localhost, port 5000"
    app.debug = True
    app.run()
    