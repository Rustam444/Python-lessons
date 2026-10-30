def narxlar(prices:list)-> list:

    new_prices=[]
    for i in prices:
        if i >0:
            i=i*0.85
            new_prices.append(i)
        else: prices.remove(i)
    print(sorted(new_prices, reverse=True))

n=int(input(">>>"))
prices=[]
for k in range(n):
    l=int(input("sonlar:"))
    prices.append(l)
narxlar(prices)
