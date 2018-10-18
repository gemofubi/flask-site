from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("site shown.")
    return 'Hello, World!'

@app.route('/world/')
def world():
    return "the world site"

print("Main file.")
