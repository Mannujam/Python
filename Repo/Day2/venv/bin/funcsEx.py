def add():
    a=10
    b=20
    c=a+b

    print('C = ',c)

def add2():
    a=10
    b=20
    c=a+b
    #return c
    #return
    #return a,b,c
    #return [a, b, c]
    #return {a, b, c}
    return (a+b)

# Positional Arguments
def add3(a,b):
    return a+b

def add4(a,b=10):
    return a+b

# *c is Packing of arguments
def add5(a,b=10,*c):
    print('Remaining Args: ', c)
    r = a+b
    for i in c:
        r+=i
    return r

# keyword only arguments
# arguments post '*c' are keyword arguments. argument order doesnt matter here..
def add6(a,b=10,*c,d,e=10):
    print('Remaining Args: ', c)
    r = a+b+d+e
    for i in c:
        r+=i
    return r

# keyword only arguments
def add7(a,b=10,*c,d,e,**f):
    print('Remaining Args: ', c)
    r = a+b+d+e
    for i in c:
        r+=i
    for j in f.values():
        r+=j
    return r


add()
r1 = add2()
print('R1 = ',r1)

r2 = add3(22,21)
print('R2 = ',r2)

r3 = add4(22)
print('R3 = ',r3)

r4 = add5(22)
print('R4 = ',r4)
r4 = add5(22,20)
print('R4 = ',r4)
r4 = add5(22,15,18,19,23)
print('R4 = ',r4)


r6 = add6(22,15,18,43,d=19,e=23)
print('R6 = ',r6)

# Unpacking of list --> *c = 45,56,67,78
L = [12,23,45,56,67,78]
r5 = add5(*L)
print('R5 = ',r5)

# Unpacking of dictionary --> *c = 45,56,67,78
# For unpacking dictionary, function should have keyword argument.
D = {'d':60, 'e':33}
r7 = add6(*L, **D)
print('R7 = ',r7)

r8 = add7(10,20,30,40,e=80,v=23,y=33,d=87)
print('R8 = ',r8)

