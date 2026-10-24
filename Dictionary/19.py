sales = [
    {"product": "Olma", "quantity": 5},
    {"product": "Banan", "quantity": 3},
    {"product": "Olma", "quantity": 2},
    {"product": "Uzum", "quantity": 4},
    {"product": "Banan", "quantity": 1}
]
new={}
for i in sales:
    if i["product"] not in new:
        new[i["product"]]=i["quantity"]
    else:
        new[i["product"]]+=i["quantity"]
print(new)
