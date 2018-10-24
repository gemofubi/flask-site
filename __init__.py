from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("site shown.")
    import datetime
    time_to_print= datetime.datetime.now()
    return render_template("main.html", time_to_print=time_to_print)

@app.route('/world/')
def world():
    return "the world site"

print("Main file.")

if __name__ == "__main__":
    app.run()
