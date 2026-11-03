import json # har doim json ni yuklab olish kk 
with open("iteams.json") as ptr:
    for mahsulot in json.load(ptr):
        if 500<=mahsulot["price"]<=1000 and mahsulot["is_available"]==True:
            print(f"id={mahsulot["id"]} material={mahsulot["material"]}")