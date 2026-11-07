import json
def employees(file: list, min_salary:int)->list:
    lst=[]
    for i in file:
        if i["is_active"] and i["salary"]>=min_salary:
            lst.append(i)
    return lst       
with open("workers.json") as ptr:
    t=json.load(ptr)
    natija=employees(t,int(input("min maoshni kirit:")))
print(natija)