import copy

orig = [1, 2, [3, 4]]
assigned = orig
s_copy = copy.copy(orig)
d_copy = copy.deepcopy(orig)

# initial
print('Initial IDs')

print()
print('IDs of list objects:')

print(f'Orig: {id(orig)}')
print(f'Assigned: {id(assigned)}')
print(f'Shallow: {id(s_copy)}')
print(f'Deep: {id(d_copy)}')

print()
print('IDs of index 0:')

print(f'Orig: {id(orig[0])}')
print(f'Assigned: {id(assigned[0])}')
print(f'Shallow: {id(s_copy[0])}')
print(f'Deep: {id(d_copy[0])}')

print()
print('IDs of index 1:')

print(f'Orig: {id(orig[1])}')
print(f'Assigned: {id(assigned[1])}')
print(f'Shallow: {id(s_copy[1])}')
print(f'Deep: {id(d_copy[0])}')


print()
print('IDs of index 2:')

print(f'Orig: {id(orig[2])}')
print(f'Assigned: {id(assigned[2])}')
print(f'Shallow: {id(s_copy[2])}')
print(f'Deep: {id(d_copy[0])}')

# change index 0
orig[0] = 11

print()
print('After changing index 0 of original')

print()
print('IDs of list objects:')

print(f'Orig: {id(orig)}')
print(f'Assigned: {id(assigned)}')
print(f'Shallow: {id(s_copy)}')
print(f'Deep: {id(d_copy)}')

print()
print('IDs of index 0:')

print(f'Orig: {id(orig[0])}')
print(f'Assigned: {id(assigned[0])}')
print(f'Shallow: {id(s_copy[0])}')
print(f'Deep: {id(d_copy[0])}')

print()
print('IDs of index 1:')

print(f'Orig: {id(orig[1])}')
print(f'Assigned: {id(assigned[1])}')
print(f'Shallow: {id(s_copy[1])}')
print(f'Deep: {id(d_copy[0])}')


print()
print('IDs of index 2:')

print(f'Orig: {id(orig[2])}')
print(f'Assigned: {id(assigned[2])}')
print(f'Shallow: {id(s_copy[2])}')
print(f'Deep: {id(d_copy[0])}')

# change index 2's index 1


print()
print('After changing index 0 of nested list in original')

orig[2][0] = 33

print()
print('IDs of list objects:')

print(f'Orig: {id(orig)}')
print(f'Assigned: {id(assigned)}')
print(f'Shallow: {id(s_copy)}')
print(f'Deep: {id(d_copy)}')

print()
print('IDs of index 0:')

print(f'Orig: {id(orig[0])}')
print(f'Assigned: {id(assigned[0])}')
print(f'Shallow: {id(s_copy[0])}')
print(f'Deep: {id(d_copy[0])}')

print()
print('IDs of index 1:')

print(f'Orig: {id(orig[1])}')
print(f'Assigned: {id(assigned[1])}')
print(f'Shallow: {id(s_copy[1])}')
print(f'Deep: {id(d_copy[0])}')


print()
print('IDs of index 2:')

print(f'Orig: {id(orig[2])}')
print(f'Assigned: {id(assigned[2])}')
print(f'Shallow: {id(s_copy[2])}')
print(f'Deep: {id(d_copy[0])}')
