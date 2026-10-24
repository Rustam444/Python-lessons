x=input("matn kiriting:")#user matn kiritadi probel bn
t=x.split(" ")#matnni probel bo'yicha list qiladi
dct={}
for i in t:#list dan har bir so'zni olyapmiz 
    c=t.count(i)#har bir so'zni lstda necha marta qatnashganini sanayapmiz
    dct[i]=c# lst dan olinayotgan har bir so'zni key qilib unga c bn sanagan countimizni beryapmiz
print(dct)