pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

'''
The original assignment on line 3 replaces the existing list of 2 dogs with the new dog. 

What we actually want is to append our new dog to the existing list of dogs.

Fixed in line 3 above
'''