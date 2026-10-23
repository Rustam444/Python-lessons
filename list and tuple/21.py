lst=[(3,10),(1,20), (2,30)]
#key ni tuple larni birinchi elementi bo'yicha saraladik
#lambda x: ni ichiga ikkita shart ham berish mumkin
lst.sort(key=lambda x: x[0])
print(lst)