def my_function():
    a = 1

    if True:
        print(a)

my_function()

'''
1 will be printed.
a is a local variable that is in scope in our if statement because the block within an if statement shares the same scope as the if's outer scope.
'''