import string
print('''Kamida 8 ta belgidan iborat parol kiriting
Unda kamida bitta katta harf bo'lishi kerak
Unda kamida bitta raqam bo'lishi kerak
Unda kamida bitta maxsus belgi(masalan: @, #, $) bo'lishi kerak''')
parol=input("parol kiriting:")
while True:
    if len(parol)<8:
        print("parol 8 tadan kam")
        parol=input("boshqa parol kiriting:")
    elif not any(belgi.isupper() for belgi in parol):
        print("Kamida bitta katta harf bo'lishi kerak")
        parol=input("parol kiriting:")
    elif not any(belgi.isdigit() for belgi in parol):
        print("parolda kamida bitta son bo'lishi kerak")
        parol=input("parol kiriting:")
    elif not any(belgi in string.punctuation for belgi in parol):
        print("Unda kamida bitta maxsus belgi kerak")
        parol=input("parol kiriting:")
    else:
        print("Parol kuchli!")
        break


    
