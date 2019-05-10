# class used is list
# Mutable
# Ordered collection

import copy     # For deepcopy

l = [10, 12.5, 'python', ['a','b']]

# similar to string slicing all options are available in list
print (l)
print (l[1])
print (l[1:])

print (l[2][3])     # will print forth char from third element

l.append(100)       # will append at the last position of list
print ('L = ',l)

l.insert(2, "Gattu")    # will insert at the position of list
print ('L = ',l)

s1 = 'wel'
s2 = 'come'
s3 = s1+s2
s4 = s1*10
print (s4)
line = '_'*40
print (line)

l1 = [10,20]
l2 = ['a','b']
l3 = l1+l2
print ('L3 = ',l3)
l1.extend(l2)
print ('L1 = ',l1)

#Remove
r1 = l.pop()                # perticular index can also be removed. "l.pop(2)"
print ('L=',l, 'R1=',r1)
r1 = l.remove(12.5)         # perticular value can also be removed. "l.remove(12.5)". does not return anything, returns NONE
print ('L=',l, 'R1=',r1)

l4 = ['z','s','w']
l4.sort()                   # default is asending order. for decending use l4.sort (reverse = True)

l4.clear()                  # clears the list.

'''
Deep Copy and Shallow copy
'''
L1 = [10,['a','b']]
L2 = L1.copy()               # shallow copy
print (id (L1[0]), id(L2[0]))       # both should be same

L3 = copy.deepcopy(L1)       # deep copy - use library "copy" and its member function deepcopy
print (id (L1[1]), id(L3[1]))       # both should be different

# Update - assign the value
L1[0] = "Ç++"
