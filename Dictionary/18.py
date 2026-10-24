products = {
    "Laptop": 700,
    "Mouse": 25,
    "Phone": 35,
    "Camera": 500,
    "Keyboard": 45
}
cheap_products={}#yangi dict ochib oldim
for keys, values in products.items():#keys va values ni bir vaqtda chiqarib oldim chunki faqat bittasi bn yangi dict ga qo'shib bo'lmaydi
    if values<100:
        cheap_products[keys]=values #valuesi 100 dan kichgina bo'lgan productlarni yangi dict ga qo'shyapmiz 
print(cheap_products)