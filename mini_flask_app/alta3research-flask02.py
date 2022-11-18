#!/usr/bin/env python3
import requests

URL= "http://0.0.0.0:2224/rogue_info"
# call api for data and parse into python
resp= requests.get(URL).json()



print(resp["name"])
print(resp["proficiency_choices"][0]["desc"])
print("Saving throws: " + resp["saving_throws"][0]["name"] + ", " + resp["saving_throws"][1]["name"])
print("Starting equipment: " + resp["starting_equipment"][0]["equipment"]["name"] + ", " + resp["starting_equipment"][0]["equipment"]["name"] + ", " + resp["starting_equipment"][0]["equipment"]["name"] + ", ")
