import json


with open("blacklist.json") as json_file:
    data = json.load(json_file)
    for p in data["addresses"]:
        print p["url"]