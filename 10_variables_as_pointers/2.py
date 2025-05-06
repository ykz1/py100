set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

print("on line 2, we create set2 to point at the same set object as set1")
print("on line 3, we add an element to set1, which mutates set1")
print("line 4 should print a set containing this new element")