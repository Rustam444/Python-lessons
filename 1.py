import json
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


    
