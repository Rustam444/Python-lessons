import json
with open("weather.json",encoding="utf-8") as ptr:
    data=json.load(ptr)
    print(f"{data}\n")
    dct={}
    natija=0
    count=0
    for i in data:
        natija+=i["temperature"]
        count+=1
        dct[i["city"]]=i["temperature"]
    print(f"eng issiq shahar:{max(dct, key=dct.get)}")
    print(f"eng sovuq shahar:{min(dct, key=dct.get)}\n")
    print(f"O'rtacha harorat: {natija/count}")


