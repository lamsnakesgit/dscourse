#find the least number out of 3
a = int(input())
b = int(input())
c = int(input())#break this case.  1 2 3 min1 a>b>c 1 4 2 is false
min = a;
if a > b:
    min = b
if c < min:#c < b: - false
    min = c
print(min)
