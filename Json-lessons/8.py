import json
with open("iteams.json") as ptr:
    t=[i["phone"] for i in json.load(ptr)["contacts"]] # bu yerda for ni qisqa ko'rinishidan foydalandik 
    print(t)