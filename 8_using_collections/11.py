print('johnson' in 'Joe Johnson')
print("False")
print()

print('sen' not in 'Joe Johnson')
print('True')
print()

print('Joe J' in 'Joe Johnson')
print('True')
print()

print(5 in range(5))
print('False')
print()

print(5 in range(6))
print('True')
print()

print(5 not in range(5, 10))
print('False')
print()

print(0 in range(10, 0, -1))
print('False')
print()

print(4 in {6, 5, 4, 3, 2, 1})
print('True')
print()

print({1, 2, 3} in {1, 2, 3})
print("False sets can't be contained in other sets")
print()

print({3, 2} in {1, frozenset({2, 3})})
print('True?')
