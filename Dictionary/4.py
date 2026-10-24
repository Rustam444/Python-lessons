dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {9:90, 7:70}
dict1.update(dict2)
dict1.update(dict3)
t=dict1 |dict2 | dict3
print(t)