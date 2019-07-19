n = int(input())
for a in range(1,n):
    print (n)*" ",
    for x in range(0,a):
        print str(a),
    print "\r"
    n = n - 1
