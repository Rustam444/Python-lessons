import json
with open("iteams.json") as ptr:
    t=[i["name"] for i in json.load(ptr)["people"] if i["birth_year"]>1990]
    print(t)
