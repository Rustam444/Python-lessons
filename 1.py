import json
<<<<<<< HEAD
with open("malumotlar.json") as ptr:
    t=json.load(ptr)
    print(len(t["mahsulotlar"]),"- ta mahsulot bor")
    l=[i["nomi"] for i in t["mahsulotlar"]]
    print(l)
    print()
    print(max(t["mahsulotlar"], key=lambda x: x["narx"]))
    print(min(t["mahsulotlar"], key=lambda x: x["narx"]))
    print()
    dct={}
    for i in t["mahsulotlar"]:
        dct[i["nomi"]]=i["narx"]
    print(dct)


    
=======
with open("o'quv_markaz.json") as ptr:
    data=json.load(ptr)
    for markaz in data["branches"]:
        print(markaz["name"])
    print()
    for markaz in data["branches"]:  
        for techer in markaz["teachers"]:
            if techer["subject"]=="Python":
                print(f"ism:{techer["name"]} {markaz["name"]} experience:{techer["experience"]}-yil")
    print()
    for markaz in data["branches"]:
        print(f"{markaz["name"]}->{len(markaz["students"])}-talaba")
    print()
    price=0
    ism="Ali"
    for markaz in data["branches"]:
        for students in markaz["students"]:
            if students["payment"]>price:
                price=students["payment"]
                markaz["name"]
    print(f"{markaz["name"]}->{students["name"]}->{price}")
    print()
    for markaz in data["branches"]:
        jami=0
        for i in markaz["students"]:
           jami+=i["payment"]
        print(f"umumiy tushum={markaz["name"]}->{jami}")
    print()
    for markaz in data["branches"]:
        for i in markaz["teachers"]:
            if i["experience"]>5:
                print(f"experience 5 yildan katta teachers:{i["name"]}")
    print()
    for markaz in data["branches"]:
        flag=0
        for k in markaz["teachers"]:
            if  k["subject"]!="Python":
                flag+=1
        if flag==0:
            print("faqat Python kursi bor->",markaz["name"])
>>>>>>> 9cc13e8a9422ff9da7c37782ff07fa860f1960e5
