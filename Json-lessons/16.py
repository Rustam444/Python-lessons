import json
with open("iteams.json") as ptr:
    dct={}
    for i in json.load(ptr)["sales"]:
        if i["month"] not in dct:
            dct[i["month"]]=i["amount"]
        else:
             dct[i["month"]]+=i["amount"]
    print(dct)