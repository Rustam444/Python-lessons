lst = [1, 2, 33, 5, 6, 7, 7]
x=int(input("son kirit:"))
for i in range(len(lst)):
    for k in range(i, len(lst)):
        if lst[i]+lst[k]==x:
            print(f"{i},{k}")