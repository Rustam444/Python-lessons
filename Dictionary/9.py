grades = {
    "Ali": 85,
    "Vali": 78,
    "Hasan": 90
    }
ism=input("ismingizni kiriting:")
baho=int(input("bahoni kirit:"))
while 0>baho or baho>100:   
    baho=int(input("baho xato boshqa kirit>>>"))
if ism in grades:
    grades[ism]=baho
    print(grades)
else:
    print("bunday talaba topilmadi")
    
