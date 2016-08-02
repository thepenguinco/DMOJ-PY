import sys
s="ABCDE"
while (True) :
    a=int(input())
    b=int(input())
    if a==1:
        for i in range(b):s=s[1:5]+s[0]
    if a==2:
        for i in range(b):s=s[4]+s[0:4]
    if a==3:
        for i in range(b%2):s=s[1]+s[0]+s[2:5]
    if a==4:
        for i in s:print(i+" ",end="")
        sys.exit()