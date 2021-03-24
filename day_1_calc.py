def m(a,b):
    return a*b
def d(a,b):
    return a/b
def s(a,b):
    return a-b
def add(a,b):
    return a+b
a=float(input('enter first number: '))
b=float(input('enter second number: '))
while True:
    c=int(input('enter choices from 1. multiplication 2. division 3. substraction 4. addition '))
    if c==1:
        print( m(a,b))
    elif c==2:
        print( d(a,b))
    elif c==3:
        print( s(a,b))
    elif c==4:
        print( add(a,b))
    else:
        print('Inavlid choice.......exited ')
        break