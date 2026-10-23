lst=[(1,2), (3,4), (8,9) ]
lst3=[]
lst1=[]
lst2=[]
for i in lst:
    t=min(i)
    lst1.append(t)
for i in lst:
    k=max(i)
    lst2.append(k)
lst3.append(tuple(lst1))
lst3.append(tuple(lst2))
print(lst3)
