#!/usr/bin/env python3
"""
DEMO: Mini-project showcasing knowladge of Flask library
and API set-up

API endpoints:

    /home - home landing page
"""
import requests
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import jsonify
from flask import url_for

app= Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "GET":
        # return template for home landing page
        return render_template("index.html")

@app.route("/search/", methods = ["POST", "GET"])
def search( ):
    allowed_classes = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
    # check if it was a post method
    if request.method == "POST":
        dnd_class = request.form.get("search_term") # indicated by a button click
        # check for valid search term
        if dnd_class in allowed_classes:
            url = "https://www.dnd5eapi.co/api/classes/" + dnd_class
            # call api for info on dnd class
            class_info = requests.get(url).json()
            # render data into variable for template
            name = class_info["name"]
            hit_die = class_info["hit_die"]
            proficiency_choices = class_info["proficiency_choices"][0]["desc"]
            starting_equipment = []
            for equipment in class_info["starting_equipment"]:
                starting_equipment.append(equipment["equipment"]["name"])

            return render_template("results.html", name=name, hit_die=hit_die, proficiency_choices=proficiency_choices, starting_equipment=starting_equipment)

        else:
            return redirect(url_for("index"))



@app.route("/rogue_info", methods = ["GET"])
def get_rogue_info():
    # call dnd api for info
    dnd_url = "https://www.dnd5eapi.co/api/classes/rogue"
    resp = requests.get(dnd_url)
    info = resp.json()
    return info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
