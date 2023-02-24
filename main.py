#Задание 1
a=str('Транспорт')
print(a)
b=str(a[2])
print(b)
c=str(a[-2])
print(c)
d=(a[0:5])
print(d)
e=(a[0:7])
print(e)
f=(a[1::2])
print(f)
h=(a[::2])
print(h)
j=(a[::-1])
print(j)
k=(a[-1::-2])
print(k)
l=(len(a))
print(l)

#Задание 2
full_str = input('Введите текст: ')
small_str = input('Введите  текст: ')
if small_str.upper() in full_str.upper():
    print('Да')
else:
    print('Нет')


