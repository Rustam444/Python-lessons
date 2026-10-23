tpl=("ada", 212, False, 4567, "aziza")
for i in tpl:
    i=str(i)
    if i==i[::-1]:
        print(f"{i}--> palindrom")
    else:
        print(f"{i}--> palindrom emas")
