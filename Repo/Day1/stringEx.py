# using string class is 'str'

b = "person's"
c = ''' Person's height xyz" '''
d = """ Person's height xyz" """
e = 'person\'s'
f = 'C:\\training\\file.py'
g = r'C:\training\file.py'      # raw string

print (d)
print (f)
print (g)

h = 'WEL COME'
print (h)
print (id(h))
print (id('WEL COME'))
print (len(h))
print (h[2])
print (h[3:6])
print (h[3:])
print (h[:4])
print (h[-4:])

print (h[0:7:1])    # last parameter is step
print (h[0:7:2])    # last parameter is step
print (h[::-1])     # last parameter is step. Traverse R to L

print (h[7:0:-1])   # last parameter is step
print (h[7:0])

# String substring
r1 = h.startswith('WEL')
print ('r1 = ',r1)
r1 = h.startswith('WEL',0,3)
print ('r1 = ',r1)
r1 = h.endswith('COME')
print ('r1 = ',r1)

# String upper
r1 = h.isupper()        # islower(), lower(), istitle(), title(), isdigit(), isalpha(), isalphanum(), index(), find(), count(), replace(), strip(), lstrip(), rstrip()
print ('r1 = ',r1)
r2 = h.upper()
print ('r1 = ',r2)
r2 = h[-3:].isupper()
print ('r2 = ',r2)

r3 = h.index('C')       # index gives error if the value is not found
print ('r3 = ',r3)
r4 = h.find('K')        # index gives -1 if the value is not found
print ('r4 = ',r4)
r5 = h.index('C',2,8)     # finds char from position 2
print ('r5 = ',r5)

s = '[wel[come][]'
r6 = s.lstrip('][e')
print ('r6 = ',r6)

x=10
y=20
z=x+y

print (f'add of {x} and {y} is {z}')