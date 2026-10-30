def sana(a: str)->str: # str qaytaryapti def 
    dct={ # dct yaratdik chunki oylarni aniqlash uchun
        "01":"Yanvar",
        "02":"Fevral",
        "03":"Mart",
        "04":"Aprel",
        "05":"May", 
        "06":"Iyun",
        "07":"Iyul",
        "08":"Avgust",
        "09":"Sentabr",
        "10":"Oktabr",
        "11":"Noyabr",
        "12":"Dekabr"    
    }
    for keys, values  in dct.items():
        if keys==a[3:5]: # agar keys lar a ni oyiga tebg bo'lsa
            print(a[:2]+' ' + values+' ' + a[-4:]+" "+"yil") # natijani chiqargin
sana(input("sanani kiriting: (13.03.2026)>>> "))