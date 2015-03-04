from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    print "serving on localhost, port 5000"
    print "To get info on server type:   'sudo lsof -i:5000' in terminal"
    app.run()
    