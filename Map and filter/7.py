natija1=list(map(str,[15000, 23000, 5000, 125000] )) # map yordamida list ni str ga o'tkazyapmiz

natija=map(lambda x: x[:-3]+','+x[-3:], natija1) # lambda bn kesma qilib orasiga " , " qo'shdik
# natija=map(lambda x: x.replace("0", ",",1)+"0", natija1) # bu usul esa replace() orqali
print(list(natija))