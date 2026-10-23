lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
lst1=[]
for i in lst:#lst ni icidan har bir elementni oldik
    l=list(i)
    l.remove(l[-1])#har bir elemntni oxirini o'chirdik 
    l.append(100)#va oxiriga 100 ni qo'shdik
    lst1.append(tuple(l))
print(lst1)