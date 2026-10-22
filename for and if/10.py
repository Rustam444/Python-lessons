import random
n=int(input("nechta son ichida random qilmoqchisiz:"))
y=int(input("son kirit:"))
for i in range(3):
    x=random.randint(1,n)
    print(x)
    if y==x:
        print("you're winner")
    else:
        print("you're looser '")