import sys
x = int(input())
for i in range (x):
    y = int(input())
    print("{0:08b}".format(bin(y)[4:]))