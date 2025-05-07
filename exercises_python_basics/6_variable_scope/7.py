a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

'''
What this program does:
1. Define global variable 'a' with value 1
2. Read my_function's definition into memory
3. Call my_function
    a. Python will register that the variable 'a' within my_function is global in scope
    b. Global variable 'a' is assigned value 2 (previously 1)
    c. Return None from my_function
4. Print global variable 'a', which has value 2
'''