def grades(baholar:dict)->float:
    count=0
    summ=0
    for i in baholar.values():
        summ+=i
        count+=1
    print(f"o'rtacha baho:{summ/count}")
n=int(input("nechta fan kiritasan:"))
t={}
for k in range(n):
    a=input("fan:")
    b=int(input("baho:"))
    t[a]=b
natija=grades(t)
