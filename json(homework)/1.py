import json
with open("orders.json",encoding="utf-8") as ptr:
    dct={}
    for i in json.load(ptr):
        print()
        natija=0
        for k in i["items"]:
            natija+=k["price"]
        print(f"{i["customer_name"]}: {natija}\n")
        dct[i["customer_name"]]=natija
    print(f"Eng katta summali buyurtma bergan: {max(dct, key=dct.get)} ")
