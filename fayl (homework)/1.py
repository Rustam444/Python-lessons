with open("moshina") as l:
    Max_brend={}
    for qator in l.read().split("\n"):
        t=qator.split(",")[-4]
        if t not in Max_brend:
            Max_brend[t]=1
        else:
            Max_brend[t]+=1
with open("moshina") as l:
    dct1={}
    for qator1 in l.read().split("\n"):
        m=qator1.split(",")
        if m[-4]==max(Max_brend, key=Max_brend.get):
            if m[-1] not in dct1:
                dct1[m[-1]]=1
            else:
                dct1[m[-1]]+=1
    
    print(f"Mashinalari eng ko'p bo'lgan brend---> {max(Max_brend, key=Max_brend.get)}")
    print(f"Ford brendi moshinalari eng ko'p davlat--->{max(dct1, key=dct1.get)}---{dct1[max(dct1, key=dct1.get)]} ta {max(Max_brend, key=Max_brend.get)} bor ")
    print(f"Ford brendi moshinalari eng kam davlat--->{min(dct1, key=dct1.get)}---{dct1[min(dct1, key=dct1.get)]} ta {max(Max_brend, key=Max_brend.get)} bor")
        
        
        
        
