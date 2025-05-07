x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

'''
This will raise an exception on line 4.
The global variable x is out-of-scope in my_function.
On line 4, the x on the right side of = operator has no value yet, which raises an exception.


'''