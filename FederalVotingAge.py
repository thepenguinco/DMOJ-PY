import sys
x = int(input())
for i in range (x):
    year, month, day = map(int, input().split())
    if 2007 - year > 18:
        print("Yes")
    elif 2007 - year < 18:
        print("No")
    elif month <= 2 and day <= 27:
        print("Yes")
    else:
        print("No")