# Core data types
# Numbers   - Immutable
# String    - Immutable
'''
List        - Mutable
tuples      - Immutable
'''
"""
Dictionaries    - Mutable
Sets            - Mutable
"""
"""
Referances are always mutable
Objects can be mutable / immutable
"""

a = 10      # class int
b = 12.5    # class float
c = 0x12    # class hex
d = 0b1010  # class bin
e = 0o12    # class oct

print (" Test Program ")
'''
Default separator is space. [change by argument 'sep' in print]
Default line end is end of line. [change by argument 'end' in print]
Few more arguments can be added as 'file' and 'flush' 
'''
print ('a = ',a, 'b = ',b,'c = ',c, 'd = ',d, 'e = ',e, sep=' $ ')

print ('a = ',id(a), 'b = ',b,'c = ',id(c), 'd = ',d, 'e = ',e, sep=' $ ', end='@')
print ('test')

print (type(a).__name__)
print (type(0x12).__name__)
