x = int(input("1-mahsulot narxini kirit (dollorda): "))
y = int(input("2-mahsulot narxini kirit (dollorda): "))
z = int(input("3-mahsulot narxini kirit (dollorda): "))

umumiy = x + y + z

if umumiy >= 500:
    print(f"20% chegirmada umumiy narx = {umumiy - umumiy * 0.2}")
elif umumiy >= 200:
    print(f"15% chegirmada umumiy narx = {umumiy - umumiy * 0.15}")
elif umumiy >= 100:
    print(f"10% chegirmada umumiy narx = {umumiy - umumiy * 0.1}")
else:
    print(f"Uzr, sizga chegirma yo'q = {umumiy}")