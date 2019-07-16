a = input()
if(a%4 == 0):
    if(a%100==0):
        if(a%400):
            print ("no")
        else:
            print("yes")
    else:
        print("yes")
else:
    print("no")
