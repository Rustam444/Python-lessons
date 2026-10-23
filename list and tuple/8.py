lst=[(1, 2, 1), (3, 3,3,4), (5,6,5)]
for i in range(len(lst)):
    lst1=[]
    for k in lst[i]:
        t=lst[i].count(k)
        lst1.append(t)
    lst[i]=lst1.copy()
    lst[i]=tuple(lst[i])
print(lst)