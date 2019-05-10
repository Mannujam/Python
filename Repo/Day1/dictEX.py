# dict class
# Mutable
# UnOrdered collection

D = {'course': 'python', 'dur': 5, 'loc': 'Pune'}
print (D["course"])

# Add or Update
D["course"] = ["C++", "Java"]
print (D["course"])

r1 = D.get('abc', 'No such key!')        # Searches for key, if not present returns message 'No such Key!'
print ('r1 = ', r1)

E = D.copy()

# Remove
r2 = D.pop("course")

# Del
del D['dur']
print (D)

# poping
r3 = D.popitem()        # default D is keys, else have to use values/items
print (r3)


K = E.keys()
I = E.items()
V = E.values()

print (K, I, V, sep = '\n')