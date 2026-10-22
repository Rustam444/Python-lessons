while True:
    c=input("haroratni selsiyda kirit(yoki to'xtashni xohlasang 'exist' deb kirit):")
    if c.lower()=='exist':
        print("sikl to'xtadi")
        break
    t=int(c)
    f=t*(9/5)+32
    if f<=32:
        print(f"{t}-gradus --> {f}-muzlash")
    elif 32<f<85:
        print(f"{t}-gradus --> {f}-yaxshi kun")
    else:
        print(f"{t}-gradus --> {f}-issiq")
