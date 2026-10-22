n=int(input("son kiriting:"))
count=0
ifoda=""
for i in range(1,n):
    t=(i)**(i)
    count=count+t
    if i==1:
        ifoda+=f"{i}^{i}"
    if i>1:
        ifoda+=f"+{i}^{i}"
print(f"{ifoda}={count}")
