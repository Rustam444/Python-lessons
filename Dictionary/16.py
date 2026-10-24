orders = [
    {"customer": "Ali", "amount": 15000},
    
    {"customer": "Vali", "amount": 22000},
    
    {"customer": "Ali", "amount": 8000},

    {"customer": "Ali", "amount": 8000},

    {"customer": "Ali", "amount": 8000},
]
new_dict = {}
for i in orders:#har bir dict ni aylanib o't dedik
    if i['customer'] not in new_dict:# agar customer:Ali new_dict da bo'lmasa
        new_dict[i['customer']] = i['amount']# qo'shib qo'ygin
    else:
        new_dict[i['customer']]+=i["amount"]# bo'sa uning qiymatiga yangi Ali ni amountini qo'shgin
print(new_dict)