d1 = {"olma": 5000, "banan": 7000}
#men dict larni qo'shish uchun tayyor formulalardan foydalanmadim("| va d1.update(d2)")
d2 = {"shaftoli": 8000, "olcha": 10000}
result={}#yangi dict ochdim
for keys, value in d1.items():# d1 dan keys va values larni bir vaqtda bitta bitta olayapmiz
    result[keys]=value#bu yerda resultga keys va value ni qo'shayapmiz
    #note that dict da append() yo'q so "result[keys]=value" shunday qilib qo'shamiz
for key, val in d2.items():
    result[key]=val
print(result)