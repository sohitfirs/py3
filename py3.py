# Задание 1

x = int(input('Введите целое число: '))
if (x < 0) & (x % 2 == 0):
    print('Отрицательное четное число')
elif x == 0:
    print('Нулевое число')
elif (x > 0) & (x % 2 == 0):
    print('Положительное четное число')
else:
    print('Число не является четным')

# Задание 2 

x = input('Введите слово из маленьких латинских букв: ')

y = 0
z = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for w in x:
    if w in 'aeiou':
        y += 1
        if w == 'a':
            a += 1
        elif w == 'e':
            e += 1
        elif w == 'i':
            i += 1
        elif w == 'o':
            o += 1
        elif w == 'u':
            u += 1
    elif w in 'bcdfghjklmnpqrstvwxyz':
        z += 1

print('Количество гласных букв:', y)
print('Количество согласных букв:', z)

if a == 0  or e == 0 or i == 0 or o == 0 or u == 0:

    print('False')
else: 
    print('Количество букв "a":', a)
    print('Количество букв "e":', e)
    print('Количество букв "i":', i)
    print('Количество букв "o":', o)
    print('Количество букв "u":', u)

# Задание 3

x = float(input('Минимальная сумма инвестиций: '))
a = float(input('У Майлка: '))
b = float(input('У Ивана: '))

if a >= x and b >= x:
    print(2)
elif a >= x:
    print('Mike')
elif b >= x:
    print('Ivan')
elif a+b >= x:
    print(1)
else:
    print(0)

input()