n = raw_input()
array = raw_input()
a = n.split(" ")
b = array.split(" ")
N = a[0]
K = a[1]
sum = 0
for x in range(0,int(K)):
    sum = sum + int(b[x])
print sum
