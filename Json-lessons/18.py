import json
with open("talabalar.json",encoding="utf-8") as ptr:
      t=json.load(ptr)
print("+" + "-"*20 + "+" + "-"*20 + "+" + "-"*47 + "+")
print(f"| {'Ism':^18} | {'Yosh':^18} | {'Universitet':^45} |")
print("+" + "-"*20 + "+" + "-"*20 + "+" + "-"*47 + "+")
for i in t:
        if i["talaba"]==True:
            print(f"| {i["ism"]:^18} | {i["yosh"]:^18} | {i["ta'lim"]["universitet"]:^45} |")
print("+" + "-"*20 + "+" + "-"*20 + "+" + "-"*47 + "+")