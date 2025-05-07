if True:
    my_value = 20

print(my_value)

'''
Will print 20 because True is True and my_value was set to 20 and is accessible outside of the if statement
'''

if False:
    my_new_value = 42

print(my_new_value)

'''
This one will raise an exception because my_new_value was never defined.
'''