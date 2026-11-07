def cleaning(text:str)->str:
    t=text.strip().title()
    return t
natija=cleaning(input("matn kiriting:"))
print(natija)