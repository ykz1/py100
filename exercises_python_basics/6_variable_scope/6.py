a = 1

def my_function():
    a = 2

my_function()
print(a)

'''
What this program does:
1. initiatlize and assign global variable 'a' to value 1
2. store my_function's definition into memory
3. call my_function
    a. initialize and assign local variable 'a' to value 2
    b. exit from my_function
4. print global variable 'a' which prints '1'
'''