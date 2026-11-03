import json
with open("iteams.json") as ptr:
    base=json.load(ptr)["departments"]
    for i in base:
        print(f"{i}:{len(base[i])}")