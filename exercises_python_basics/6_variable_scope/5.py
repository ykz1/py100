a = 1

def my_function():
    print(a)
    a = 2

my_function()


'''
This program will:
1. Initiate global variable a and assign the value 1 to it
2. Read my_function's definition
3. Call my_function:
    a. Python will classify a as a local variable, which makes global variable a not accessible
    b. On line 4, an error will be raised because local variable a has not yet been initiated
'''