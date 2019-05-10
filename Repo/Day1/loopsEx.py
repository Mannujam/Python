a = 20

if a == 10:
    print ('a=10')
elif a > 10:
    print ('a>10')
else:
    print ('a<10')

# =============================================
a = 'python'

if a != 'java':
    print ('Not java')
elif not a.startswith('C++'):
    print ('Not C++')
elif 'th' in a:
    print ('Substring found')

# ================List=======================
L1 = [10,20]
L2=L1
L3 = L1.copy()

if L1 is L2:
    print ('Both refer same object')
if L1 == L3:
    print ('Contents are equal')
if 20 in L1:
    print ('20 found')

# ================Dictionary=======================
D1 = {'A':10,'B':20}

if 'B' in D1:
    print ('Both refer same object')
if 20 in D1.values():
    print ('Contents are equal')
if ('A',10) in D1.items():
    print ('20 found')

''' 
==========================================================
    FOR and WHILE
    FOR - works on any collection
    WHILE - boolean 
==========================================================
'''
S='python'
b = 'java'

for a in S:
    print ('a=',a)

L = [10,20,30]
for b in L:
    print ('b = ', b)

print ("Now 'a' & 'b'", a,b)

# ================Dictionary=======================
# helpful in reading json file, will return dictionary object

D = {'A':10,'B':20}
for k in D:     # D.keys()
    print (k, D[k], sep=' = ')

for v in D.values():
    print('Value = ', v)

for i in D.items():
    print('Items (tuple) = ', i)
    print('Items (value) = ', i[0])
    print('Items (value) = ', i[1])

for k,v in D.items():
    print('Items (key) = ', k)
    print('Items (value) = ', v)

hosts=['h1','h2','h3']
ips=['ip1','ip2']

z = zip(hosts, ips)
print (list(z))


# ================Range=======================
r1 = range(10)
r2 = range(1,10)
r3 = range(1,10,2)

print (r1,r2,r3)
print (list(r1),list(r2),list(r3))

for i in range(2,10,2):
    print ('i = ',i)

for h in range(len(hosts)):
    print('host = ', h)


# ================Lists=======================
comp = ['ibm', 'syn1', 'sap', 'saap', 'syn2']

for c in comp:
    if c.startswith('syn'):
        print('syn Found')
        #break
    elif c.startswith('sa'):
        print('sa Found')
        #break
    else:
        print('Not found')
#else:              # for else
#    print ('Not found')



# ================WHILE=======================
# similar to for
L=[10,20]

while L:
    print('Processed = ', L.pop())


# ========================================================================
# ========================================================================

a = input ('Enter number')
b = int(a)
print (a)
print (b)

c = eval(a)
print (c)
