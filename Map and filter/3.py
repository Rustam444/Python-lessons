natija=map(lambda x: x[0], filter(lambda x: True in x ,[("Burger", False), ("Salad", True), ("Soup", True), ("Steak", False)] ))
print(list(natija))