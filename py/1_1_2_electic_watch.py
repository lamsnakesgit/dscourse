#Задача «Электронные часы»
#Условие
#Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках.
# n minutes gone since start of 24 hours. 0-23 0-59 n>60*24=1440
# code
nm = int(input())
# leftmin = 1440 - nm
# lefth = leftmin // 60
# mins = leftmin % 60
# print(leftmin, lefth, mins)
#print(lefth, mins) # this is the case if n is minutes left before 24h-day ends
lefth = (nm // 60) % 24
mins = nm % 60
print(lefth, mins)

