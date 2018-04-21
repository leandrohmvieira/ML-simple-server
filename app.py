
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get")
def get_response():
    return True

@app.route("/post")
def post_response():
    return True

if __name__ == "__main__":
    app.run()
