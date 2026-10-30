def sozlar(words:list[str]):
    t=[i for i in words if i[-4:].lower()=="gram" ]
    return t
words =["telegram", "Instagram", "hello", "program", "diagram", "world"]
print(sozlar(words))
