# set class
# Unordered
# Mutable
# No key, No index
# Always unique values

S = {10, 10, 'python'}
print ('S = ', S)

S.add(20)
S.add(30)
print ('S = ', S)
print (id(S))

t = S.copy()

#remove
r1 = S.remove(10)
r2 = S.pop()

print (r1, r2, S)

L = list(t)
M = [10,10,20,20]

S2 = set(M)
print (S2)
