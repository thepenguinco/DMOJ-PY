import sys
s = 1
while (s != 100):
    x = int(input())
    if x == 0:
        print("You Quit!")
        sys.exit()
    if s + x <= 100:
        s += x
        if s == 9:
            s = 34
        if s == 40:
            s = 64
        if s == 67:
            s = 86
        if s == 54:
            s = 19
        if s == 90:
            s = 48
        if s == 99:
            s = 77     
    print("You are now on square " + str(s))
print("You Win!")
sys.exit()