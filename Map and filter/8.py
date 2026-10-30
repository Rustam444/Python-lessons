natija=map(lambda x: x[0], filter(lambda x: "IT" in str(x).upper(),[("Ali", "IT"), ("Vali", "HR"), ("Aziza", "IT"), ("Nodir", "Finance")]))
# birinchi map() ni yozdik biz kerakli narsani chiqarib olish uchun
# map() ni ichida filter() yozyapmiz verguldan keyin, u bizga IT so'zi bor so'zlarni olib beradi
# map endi x[0] ni chiqarib beradi
print(list(natija))