
# Decorator function pattern - to avoid repeated / common lines in the function
def mydec (funcs_to_be_decorated):
    def decorated_func(x,y):
        print('Result is: ')
        funcs_to_be_decorated(x,y)
        print('End of result')
    return decorated_func

@mydec
def add(a,b):
    #print('Result is: ')
    print(a+b)
    #print('End of result')

@mydec
def sub(a,b):
    #print('Result is: ')
    print(a-b)
    #print('End of result')


add(10,20)
sub(10,20)

# working of decorator function - Function object
def addS(a,b):
    print(a-b)

f = mydec(addS)
print (f(5,20))