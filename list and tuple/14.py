lst = [('item1', '12.20'),('item2', '15.10'), ('item3', '24.5')]
#lstni sort qildik lambda bn x[1] chi elementni oldi va float qildik, int qilolmaymiz
#chunki kasr sonni int qila olmay xato beradi, oldidagi(-) ishora reverse=True vazifasini bajaradi
lst.sort(key=lambda x: -float(x[1]))
print(lst)