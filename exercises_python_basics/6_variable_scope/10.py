b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

'''
This will print '[10, 2, 3]' because of two things—
1. Global variables are in scope in method definitions: b is in scope within my_function
2. Lists are mutable: on line 4, we are reassigning 10 to the 1st element of list b, which mutates the list object itself.
'''