gap = "salom aziz qalaysan"
gap=gap.split()#sort() bu  list uchun ishlata olamiz lejkin list ni ichida nima bo'lishini qizig'i yo'q 
gap.sort(key=len)
print(gap)