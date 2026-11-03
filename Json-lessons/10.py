import json # json kutubxonasini chaqirib oldik
with open("iteams.json") as prt:
    base=json.load(prt)["categories"] # va categories bo'liniga kirib
    print(max(base, key=lambda x: base[x]))
    