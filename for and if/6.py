n=int(input("nechta kompaniya kiritmoqchisiz:"))
for i in range(n):
    k=input(f"{i+1}-kompaniya nomini kirit:")
    x=int(input(f"{k}-kompaniya aksiyasini kiriting($):"))
    if x>=100:
        print(f"{k}-kompaniya Aksiysi qimmat")
    elif 50<=x<100:
        print(f"{k}-kompaniya Aksiyasi o'rtacha")
    else:
        print(f"{k}-kompaniya Aksiyasi arzon")
