import json 
with open("iteams.json") as ptr: # json ni ochdik
    m=json.load(ptr)# uni o'qidik
    for r,i in m["courses"].items(): # r ga keys va i ga qiymatlarini berdik
        l=0
        count=0
        for base in i:
            l+=base["grade"]
            count+=1
        t=l/count
        print(f"{r}: {t}")
    