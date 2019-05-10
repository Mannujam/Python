#map
def disc(P):
    return P-10

L=[100,200,300,400]

r1=map(disc,L)
print('r1 = ', list(r1))

# filter - Filtering out some values
def filt(P):
    return P>100 and P<400

L=[100,200,300,400]

r2=filter(filt,L)
print('r2 = ', list(r2))

# reduce - Reduce the computation
def red(P,Q):
    return P+Q

L=[100,200,300,400]

from functools import reduce
r3=reduce(red,L)
print('r3 = ', r3)


#Lambda - single line expression of builtin functions
r4 = map(lambda P:P-1, L)
r5 = filter(lambda P:P>100 and P<400, L)
r6 = reduce(lambda P,Q:P+Q, L)

print('r4 = ', list(r4))
print('r5 = ', list(r5))
print('r6 = ', r3)

# Lambda for list comprehensions
L = [(lambda i:i*i)(a) for a in range(10)]
print('L = ', L)