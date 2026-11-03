import json
with open("iteams.json","w") as ptr: # birinchi o'qitib oldik dump bn
    lst=[
        {"toshkent": 5000,
         "shahrisabz":10000,
         "buhoro":2000}
    ]
    json.dump(lst,ptr, indent=3)
with open("iteams.json") as ptr: # keyin load bn o'qitib max shaharni topayapmiz
    for shahar in json.load(ptr):
        print(max(shahar, key=shahar.get))