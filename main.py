from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, King!</p>"
# print (__name__)
#if __name__ == '__name__':
app.run(host='0.0.0.0', debug=True)