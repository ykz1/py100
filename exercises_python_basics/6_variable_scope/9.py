a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

'''
What this program does:
1. Initialize global variable 'a' and assign it value 7
2. Call my_function and pass it global variable 'a''s value, which is 7, as argument 'b'
    a. b is incremented 10 to be come 17
3. Global variable 'a' is printed, its value is still 7 and that is what's printed. 'a''s value remains unchanged because it was passed by object reference as an argument to my_function, and on line 4, we re-assigned the local variable b to value 17 instead of mutating the underlying object.
'''