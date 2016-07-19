from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # deliberate error
    return "the answer is: " + 42  # error shows up in the browser

if __name__ == "__main__":
    print "serving on localhost, port 5000"
    app.debug = True
    app.run()
    