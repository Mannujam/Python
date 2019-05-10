# Varibale scoping in functions

x=10                    #global
def f1():
    x=20                #enclosed
    def f2():
        nonlocal x      #if variable defined as 'nonlocal'/'global', local veriable is treated as enclosed/global variable
        x=30            #local
        print('F2 = ',x)
        global y        #if global variable is not available, it will create new, else will assign existing global variable
        y = 200
    f2()
    print('F1 = ', x)
f1()
print('Global = ',x, y)

# checking variable name available sequence is --> local, enclosed, global, builtins, else exception
print(dir(__builtins__))

L=[]
print(dir(L))
print(help(L.append))