# Comprehensions - generate expression in lists

L1 = [i for i in range(10)]
print('L1 = ',L1)

L2 = [i*i for i in L1 if i%2 == 0]
print('L2 = ',L2)

# Removing '\n' from readline
f=open('test.txt','r')
L3 = [line.strip() for line in f]

#
keys = ['k1', 'k2']
values = [10,20]
L4 = {k:v for k,v in zip(keys,values)}

