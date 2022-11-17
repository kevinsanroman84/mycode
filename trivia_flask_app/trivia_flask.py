#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("triva_page.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/answer", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm") == "Zone Improvement Project": # if nm was assigned via the POST
            return redirect(url_for("correct")) # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            return redirect(url_for("start"))

@app.route("/correct", methods = ["POST", "GET"])
def correct():
    return render_template("correct.html")
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

