# tuple class
# Immutable
# Ordered collection

T = (10, 12.5,'python', ['a','b'], (10,20))

print (T)
print (T[0])
print (T[1:])

i = T.index('python')
c = T.count('python')

print (f'Index is {i} and Count is {c}')

# Can convert from list to tuple, tuple to list, etc..
L = list(T)
print ('L = ', L)

L[2].append(30)

M = [10, 20]
T1 = tuple (M)
print ('Tuple T1 = ', T1)