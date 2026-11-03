import json
with open("iteams.json") as ptr:
    for i in json.load(ptr)["students"]:
        t=sum(i["grades"])/(len(i["grades"]))
        print(f"{i["name"]}: {t:.2f}")