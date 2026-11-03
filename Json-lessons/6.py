import json
with open("iteams.json") as ptr:
    for mahsulot in json.load(ptr):
        if mahsulot["is_available"]==False and mahsulot["price"]<1000:
            print(mahsulot["material"])