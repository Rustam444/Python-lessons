dct={1: 10, 2: 20, 3:30, 4: 55, 5: 25}
dct1=dct.copy()#dct dan copy oldik, chunki dct dan value o'chganda xatolik yoki xato qiymat beradi 
for keys, value in dct.copy().items():# keys va values larni dct ni copysi bo'yicha oldik
    if value==max(dct1.values()) or value==min(dct1.values()):
#if da agar copy olmaganda min qiymat chiqib ketgan dct ni yana qolgan elementlaridan min topib o'chiraveradi
        dct.pop(keys)
print(dct)