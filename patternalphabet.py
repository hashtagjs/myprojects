i = input()
sum = 0
x = i - 1
revsum = i - 1
space = i - 1
revspace = 1
for z in range(0,i):
    j = 65 + z
    c = chr(j)
    sum+=1
    bs = sum*c
    print " "* space,
    print bs
    space = space - 1
while (x>=0):
    t = 64 + x
    d = chr(t)
    bs2 = revsum * d
    print " "*revspace,
    print bs2
    revspace += 1
    revsum = revsum - 1
    x = x - 1
