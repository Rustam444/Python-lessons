import json
with open("tickets.json",encoding="utf-8") as ptr:
    data=json.load(ptr)
    dct={}
    count=0
    for i in data:
        count+=i["seats"]
        if i["from"]=="Tashkent":
            print(i,"\n")
        dct[i["flight"]]=i["price"]
    print("eng qimmat reys:",max(dct,key=dct.get))
    print("eng arzon reys:",min(dct,key=dct.get))
    print("umumiy o'rindiq: ",count)  
    
