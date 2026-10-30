def top_user(data:list[tuple[str, int]]) ->str: # funksiya yaratdik

    dct={} # o'yinchilarni nomini bir marta ishlatish uchun dct dan foydalandik
    for i in data: # data dagi har bir list larni aylantiryapmiz
        if i[0] not in dct: # lstnig 0 chi elementi dct larning key lari orasiga bo'lmasa 
            dct[i[0]]=i[1] # dct ga uni qiymati bn qo'shib qo'y
        else:
            dct[i[0]]+=i[1] # aks holda uni qiymatiga yangi qiymatni qo'shda natijani yana tenglab qo'y
    print(max(dct, key=dct.get),"- ning achkosi eng katta") # dct ning ichidan key bo'yicha eng katta qeymatga egasini topish

data=[
        ("user1", 50),
        ("user2", 60),
        ("user1", 10),
        ("user3", 30)
    ]
top_user(data)