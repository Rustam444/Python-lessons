import json
with open("iteams.json") as ptr:
    n=input("material nomini kirit:")
    new= []
    for mahsulot in json.load(ptr):
        if mahsulot['material'] == n and mahsulot["is_available"]:
            new.append(mahsulot)
    print(sorted(new, key=lambda x: x['price']))