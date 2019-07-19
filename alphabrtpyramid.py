n = int(input())
for a in range(0,n+1):
    print (n)*" ",
    v = chr(64+a)
    for x in range(0,a):
        print v,
    print "\r"
    n = n - 1
