import json
with open("menu.json",encoding="utf-8") as ptr:
    data=json.load(ptr)
    for i in data:
        if i["category"]=="Pizza":
            print(i,"\n")
    dct={}
    for k in data:
        dct[k["name"]]=k["price"]
    print(f"eng qimmat taom: {max(dct, key=dct.get)}")
    print(f"eng arzon taom: {min(dct, key=dct.get)}")

