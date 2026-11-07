def iteams(mahsulot:list)->list:
    lst=[]
    for i in mahsulot:
      if i not in lst:
         lst.append(i)
    return lst
t=["olma", "banan", "olma", "anor", "banan"]
natija=iteams(t)
print(natija)