dct={'a': 100, 'b':700, 'c': 200} # dict bu xuddi list ga o'xshagan funkdiya 
#lekin unda indeks o'rniga keys lar bo'ladi, biz uning values lariga keys lari 
#orqali murojat qilamiz
if 200 in dct.values():# here 200 bormi dct ning values larini ichida degani
    print("bor")# bo'sa bor degin
else:
    print("yo'q")