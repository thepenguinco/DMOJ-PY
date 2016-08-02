import sys
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
step=0
ni=0
by=0
while (step!=s):
    for i in range(a):
        ni += 1
        step += 1
        if step == s:
            break
    if (step==s):
        break
    for i in range(b):
        ni -= 1
        step += 1
        if step == s:
            break
step=0
while (step!=s):
    for i in range(c):
        by += 1
        step += 1
        if step == s:
            break
    if (step==s):
        break
    for i in range(d):
        by -= 1
        step += 1
        if step == s:
            break
if ni > by:
    print ("Nikky")
elif by > ni:
    print ("Byron")
else:
    print ("Tied")
sys.exit()