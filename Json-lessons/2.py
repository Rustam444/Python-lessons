import json
with open("iteams.json", "w") as ptr:
    lst=[
            {"name":input("nom:"),
            "price":int(input("narx:")),
            "number":int(input("soni:"))}
        ]
    json.dump(lst,ptr,indent=4)
with open("iteams.json") as ptr:
    natija=json.load(ptr)
    jami=0
    for mahsulot in natija:
        jami+=mahsulot['price'] *  mahsulot['number']
    print(jami)