n=int(input("nechta foydalanuvchi qo'shmoqchisiz;"))
for i in range(n):
    print(f"{i+1}-chi mijoz")
    yosh=int(input("yoshingizni kirit:"))
    yil=int(input("necha yil obuna bo'lgansiz:"))
    print("Asosiy narx=15$")
    narx=0
    narx1=0
    if yosh>=50:
        print("yosh bo'yicha chegirma=20%")
        narx=15*0.2
    if yil>=3 and yil<5:
        print("obuna davomiyligi bo'yicha=10%")
        narx1=15*0.1
    elif yil>=5:
        print("obuna davomiyligi bo'yicha=15%")
        narx1=15*0.15
    print(f"yakuniy narx= ${15-narx-narx1}")