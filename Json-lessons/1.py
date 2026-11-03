import json # json improt qilib olyapmiz, note that json fayl ochganimizda uni .json deb ochamiz, (students.json)
with open("students.json") as prt: # json ochgin uni har doim kengaytma bn yozish kk " " ichiga txt da ham shunday edi
    for shaxs in json.load(prt): # json.load(prt)-- faylni o'qib ol degani
        if "Matematika" in shaxs["subjects"]:
            print(shaxs)
