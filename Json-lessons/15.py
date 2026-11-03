import json
with open("iteams.json") as ptr:
    t=max(json.load(ptr)["products"], key=lambda x: x["price"])
    print(f"{t["name"]}: {t["price"]}")
        