import json
with open("iteams.json") as ptr:
    t=[i["name"] for i in json.load(ptr)["users"] if len(i["social"])>=2]
    print(t)
        