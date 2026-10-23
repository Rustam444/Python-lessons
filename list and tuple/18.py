lst = [12, 'salom', 4.5, 'dunyo', True]
t=[i for i in lst if type(i)==str]     
print(sorted(t))