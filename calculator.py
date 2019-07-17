def getfirst():
    global a
    try:
        a = int(input(" enter the first number"))
    except NameError:
        print(" enter a integer value")
        getfirst()
    except ValueError:
        print("only integer values")
        getfirst()
    except SyntaxError:
        print ("please enter only numbers")
        getfirst()
def getsecond():
    global b
    try:
        b = int(input(" enter the second numbers"))
    except NameError:
        print(" enter a integer value")
        getsecond()
    except ValueError:
        print("only integer values")
        getsecond()
    except SyntaxError:
        print ("please enter only numbers")
        getsecond()
def choice():
    global c
    try:
        c = int(input(" enter your choice 1.add 2.sub 3.multiply 4.div 5.modulos"))
    except NameError:
        print(" enter a integer value")
        choice()
    except ValueError:
        print("only integer values")
        choice()
    except SyntaxError:
        print ("please enter only numbers")
        choice()
def add():
    print "the sum is",a + b
def subtract():
    print "the answer is ",a - b
def multiplication():
    print "the product is",a*b
def division():
    try:
        print "the answer is",a/b
    except ZeroDivisionError:
        print (" denominator should not be zero")
        getsecond()
def modulos():
    try:
        print "the answer is ", a%b
    except ZeroDivisionError:
        print (" denominator should not be zero")
        getsecond()
def choiceexecute():
    if(c == 1):
        add()
    elif(c==2):
        subtract()
    elif(c==3):
        multiplication()
    elif(c==4):
        division()
    elif():
        modulos()
    else:
        print(" please enter a number in given choices")
        choice()
def replay():
    getfirst()
    getsecond()
    choice()
    choiceexecute()
getfirst()
getsecond()
choice()
choiceexecute()
rp = raw_input("do you want to continue : enter  yes  or no")
if (rp == 'yes'):
    replay()













