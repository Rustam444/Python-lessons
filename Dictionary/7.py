dct={'data1': 100,'data4' : -54,'data3': 247}
#dct dan biz items larni ajratib olsak, ajralgan itemslar 
#tuple ko'rinishda saqlanadi yani:('data1',100) qilib, so agar biz key= deb shart bermasak
#u avtomatskiy 1 chi turgan elamntga qarab sortlaydi,
natija=dict(sorted(dct.items(), key=lambda x: x[1]))
#bu kodda esa men key orqali 2 chi elment bo'yicha sortladim
print(natija)