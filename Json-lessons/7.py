import json
with open("iteams.json") as prt:
    print(max((json.load(prt)["people"]), key=lambda x: x["age"]))
        
        