#Задача «Сколько совпадает чисел»
#Условие
#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
a = int(input())
b = int(input())
c = int(input())
e = 0
if a == b:
    e += 1
if b == c:
    e += 1
if a == c:
    e += 1
if e > 0 and e < 3:
    print(e + 1)
elif e == 3:
    print(3)
else:
    print(0)
