from flask import Flask, redirect

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello World!"


@app.route("/bye")
def bye_world():
    return "Bye World!"


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/hello"), 404, {"Refresh": "1; url=/hello"}
