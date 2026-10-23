lst = ['salom', 23, 'dunyo',5, 100, 'python']
strings=[i for i in lst if type(i) == str ]#biz qayta qayta yozishlarni bitta for sikliga kiritdik
numbers=[i for i in lst if type(i) == int ]
print(sorted(strings))
print(sorted(numbers, reverse=True))
