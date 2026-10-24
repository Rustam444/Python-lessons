store = {
"olma": 5000,
"banan": 7000}
x=input("mahsulot nomi:")
while x in store:
    x=input("bu mahsulot do'konda bor, boshqasini tekshir:")
else:
    narx=int(input("narxini kirit:"))
    store[x]=narx
    print(store)