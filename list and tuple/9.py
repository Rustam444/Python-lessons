lst=[(9, 8, 9, 9), (4, 5, 4, 5, 4)]
for i in range(len(lst)):
    lst1=[]
    for x in lst[i]:
        lst1.append(lst[i].count(x))
    lst[i]=lst1
    lst[i]=tuple(lst[i])
print(lst)
        