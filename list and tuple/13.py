lst =[(),(),('',),(),('a', 'b'),(),('a', 'b','c'), (),('d',)]
lst1=lst.copy()
for i in lst1:
    if i==():
        lst.remove(i)
print(lst)