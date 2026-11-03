import json
with open("iteams.json") as ptr:
    dct={}
    for base in json.load(ptr)["orders"]:
        if base["customer"] not in dct:
            dct[base["customer"]]=base["amount"]
        else:
            dct[base["customer"]]+=base["amount"]
    print(dct)